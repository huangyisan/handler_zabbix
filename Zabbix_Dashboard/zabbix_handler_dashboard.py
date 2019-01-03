from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_dashboard_info

class ZabbixDashboards(JSRPCQuery):

    def get_all_Dashboards(self,payload):
        return self.zabbix_jsrpc_query(payload).get("result","")


c = ZabbixDashboards()
print(c.get_all_Dashboards(payload=zabbix_dashboard_info.all_dashboards_payload))