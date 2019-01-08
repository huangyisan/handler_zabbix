from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info


class ZabbixHosts(JSRPCQuery):

    _output_data = ["hostid","host"]


    def get_all_hosts(self,payload=zabbix_hosts_info.get_all_hosts_payload()):
        '''
        
        :param payload: default all
        :return: list
        '''
        return self.zabbix_jsrpc_query(payload).get("result","")

    def get_customer_hosts(self,output_data=_output_data, **kwargs):
        '''
        
        :param output_data: default hostid and host.
        :param kwargs:  Return only those results that exactly match the given. hostid=10084
        :return: list
        '''

        payload = zabbix_hosts_info.get_customer_hosts_payload(output_data, **kwargs)
        return self.get_all_hosts(payload)

# c = ZabbixHosts()
# output_data = ["hostid","host"]
# kwargs = {}
# print(c.get_customer_hosts(avaliable=1))
