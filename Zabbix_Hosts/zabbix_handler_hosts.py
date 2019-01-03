from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info

class ZabbixHosts(JSRPCQuery):

    def get_all_hosts(self,payload):
        return self.zabbix_jsrpc_query(payload).get("result","")


c = ZabbixHosts()
print(c.get_all_hosts(payload=zabbix_hosts_info.all_hosts_payload))