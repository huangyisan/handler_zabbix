from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_items_info

class ZabbixItems(JSRPCQuery):

    _output_data = "extend"
    def _get_items(self, payload):
        return self.zabbix_jsrpc_query(payload).get("result", "")

    def get_customer_items(self, output_data=_output_data, host="Zabbix Server",visiable=None,**kwargs):

        payload = zabbix_items_info.get_customer_items_payload(output_data,host, visiable, **kwargs)
        if visiable:
            print("The payload is:\n" + "{0}".format(payload))
        return self._get_items(payload)

    def search_customer_items(self,selecthosts="false", searchwildcardsenabled="false", searchbyany="false", output_data=_output_data,visiable=None, **kwargs):

        payload = zabbix_items_info.search_items_payload(selecthosts, searchwildcardsenabled, searchbyany,output_data,visiable, **kwargs)
        if visiable:
            print("The payload is:\n" + "{0}".format(payload))
        return self._get_items(payload)

a = ZabbixItems()
# output_data = ["hostid",'name','lastvalue']
host = "ShangHai-SJ-L3-MP-Zabbix-01"
name = ["Interface Eth-Trunk1(To-charge_cucc_beijing_sjqlt_01): Bits received","Interface Eth-Trunk10(To-charge_ctcc_fujian_qzdx_01): Bits received"]
print(a.get_customer_items(host=host))
# print(a.search_customer_items(output_data=output_data,hostid=hostid,name=name))