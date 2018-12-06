from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_auth_info

class ZabbixLogin(JSRPCQuery):

    def get_token(self,payload=zabbix_auth_info.auth_payload):
        return self.zabbix_jsrpc_query(payload).get('result')
