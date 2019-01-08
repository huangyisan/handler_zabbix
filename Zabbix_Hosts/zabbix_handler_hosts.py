from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info


class ZabbixHosts(JSRPCQuery):

    def get_all_hosts(self,payload):
        return self.zabbix_jsrpc_query(payload).get("result","")

    def get_customer_info(self,output_data):
        '''

        :param output_data: 自定义要输出的内容
        :return:
        '''
        payload = zabbix_hosts_info.get_all_hosts_payload(output_data)
        return self.get_all_hosts(payload)

# c = ZabbixHosts()
# output_data = ["hostid","host"]
# print(c.get_custmer_info(output_data=output_data))
