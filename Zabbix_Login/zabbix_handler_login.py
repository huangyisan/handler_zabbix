from zabbix_jsrpc_query import JSRPCQuery
from login_info import payload
import requests
import json

class ZabbixLogin(JSRPCQuery):

    def zabbix_jsrpc_query(self, payload):
        payload = json.dumps(payload).encode('utf-8')
        r = requests.post(url=self.jsrpc_url, data=payload, headers=self.header)
        return r.json()

    def get_token(self,payload=payload):
        return self.zabbix_jsrpc_query(payload).get('result')

