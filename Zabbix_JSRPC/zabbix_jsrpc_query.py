from Zabbix_Payloads import zabbix_auth_info
import requests
import json
import sys


class JSRPCQuery(object):

    def __init__(self):
        self.username = zabbix_auth_info.authinfo.get('username')
        self.password = zabbix_auth_info.authinfo.get('password')
        self.jsrpc_url = '{0}api_jsonrpc.php'.format(zabbix_auth_info.authinfo.get('url'))
        self.header = {"Content-Type": "application/json"}

    def zabbix_jsrpc_query(self, payload):

        payload = json.dumps(payload).encode('utf-8')
        try:
            r = requests.post(url=self.jsrpc_url, data=payload, headers=self.header, timeout=(0.5, 5))
        except requests.exceptions.ConnectTimeout:
            print("Request {0} timeout!".format(self.jsrpc_url))
            sys.exit(1)
        except requests.exceptions.ReadTimeout:
            print("Receive data from {0} timeout".format(self.jsrpc_url))
            sys.exit(1)
        return r.json()