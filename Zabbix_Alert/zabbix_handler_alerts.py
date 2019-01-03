from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_alerts_info

class ZabbixAlerts(JSRPCQuery):

    def get_all_Alerts(self,payload):
        return self.zabbix_jsrpc_query(payload).get("result","")


c = ZabbixAlerts()
print(c.get_all_Alerts(payload=zabbix_alerts_info.all_alerts_payload))