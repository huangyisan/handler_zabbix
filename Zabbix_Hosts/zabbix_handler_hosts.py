from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info


class ZabbixHosts(JSRPCQuery):

<<<<<<< HEAD
    def _get_hosts(self,payload):
        return self.zabbix_jsrpc_query(payload).get("result", "")

    def get_all_hosts(self):
        '''

        :param output_data:
        :return:
        '''
        payload = zabbix_hosts_info.get_all_hosts_payload("extend")
        return self._get_hosts(payload)
=======
    _output_data = ["hostid","host"]

>>>>>>> bb48dc68fad5cd1a0776477fbfb3290134b525ef

    def get_all_hosts(self,payload=zabbix_hosts_info.get_all_hosts_payload()):
        '''
        
        :param payload: default all
        :return: list
        '''
        return self.zabbix_jsrpc_query(payload).get("result","")

    def get_customer_hosts(self,output_data=_output_data, **kwargs):
        '''
<<<<<<< HEAD
        payload = zabbix_hosts_info.get_all_hosts_payload(output_data)
        return self._get_hosts(payload)

# c = ZabbixHosts()
# output_data = ["hostid","host"]
# # print(c.get_customer_info(output_data=output_data))
# print(c.get_all_hosts())
=======
        
        :param output_data: default hostid and host.
        :param kwargs:  Return only those results that exactly match the given. hostid=10084
        :return: list
        '''

        payload = zabbix_hosts_info.get_customer_hosts_payload(output_data, **kwargs)
        return self.get_all_hosts(payload)


'''
Example:
c = ZabbixHosts()
output_data = ["hostid","host"]
kwargs = {}
print(c.get_customer_hosts(avaliable=1))
'''
>>>>>>> bb48dc68fad5cd1a0776477fbfb3290134b525ef
