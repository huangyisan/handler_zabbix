from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_auth_info
import sys

class ZabbixLogin(JSRPCQuery):

    def get_token(self,payload=zabbix_auth_info.auth_payload):
        result = self.zabbix_jsrpc_query(payload)
        if result.get('error'):
            print("Login Failed!")
            sys.exit(1)
        return self.zabbix_jsrpc_query(payload).get('result')
