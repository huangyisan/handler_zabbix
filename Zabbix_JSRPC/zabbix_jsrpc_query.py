from Zabbix_Payloads import zabbix_auth_info
import requests
import json


class JSRPCQuery(object):

    def __init__(self):
        self.username = zabbix_auth_info.authinfo.get('username')
        self.password = zabbix_auth_info.authinfo.get('password')
        self.jsrpc_url = '{0}api_jsonrpc.php'.format(zabbix_auth_info.authinfo.get('url'))
        self.header = {"Content-Type": "application/json"}

    def zabbix_jsrpc_query(self, payload):
        payload = json.dumps(payload).encode('utf-8')
        r = requests.post(url=self.jsrpc_url, data=payload, headers=self.header)
        return r.json()



