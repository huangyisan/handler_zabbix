from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_triggers_info

class ZabbixTrigger(JSRPCQuery):

    def get_count_trigger(self,payload):
        return self.zabbix_jsrpc_query(payload).get("result","")


c = ZabbixTrigger()
print(c.get_count_trigger(payload=zabbix_triggers_info.count_alerts_payload))