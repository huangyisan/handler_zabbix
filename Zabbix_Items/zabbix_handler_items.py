from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_items_info

class ZabbixItems(JSRPCQuery):

    _output_data = "extend"
    def _get_items(self, payload):
        return self.zabbix_jsrpc_query(payload).get("result", "")

    def get_customer_items(self, output_data=_output_data, **kwargs):

        payload = zabbix_items_info.get_customer_items_payload(output_data, **kwargs)
        return self._get_items(payload)

a = ZabbixItems()
print(a.get_customer_items())