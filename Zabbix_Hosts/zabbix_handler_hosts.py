from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info


class ZabbixHosts(JSRPCQuery):

    def _get_hosts(self,payload):
        return self.zabbix_jsrpc_query(payload).get("result", "")

    def get_all_hosts(self):
        '''

        :param output_data:
        :return:
        '''
        payload = zabbix_hosts_info.get_all_hosts_payload("extend")
        return self._get_hosts(payload)

    def get_customer_info(self,output_data):
        '''

        :param output_data: 自定义要输出的内容
        :return:
        '''
        payload = zabbix_hosts_info.get_all_hosts_payload(output_data)
        return self._get_hosts(payload)

# c = ZabbixHosts()
# output_data = ["hostid","host"]
# # print(c.get_customer_info(output_data=output_data))
# print(c.get_all_hosts())
