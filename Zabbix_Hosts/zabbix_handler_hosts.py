from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info


class ZabbixHosts(JSRPCQuery):

    _output_data = ["hostid","host"]

    def _get_hosts(self,payload):
        '''

        :param payload: 通用方法
        :return:
        '''
        return self.zabbix_jsrpc_query(payload).get("result","")

    def get_all_hosts(self):
        '''

        :param payload: default all
        :return: list
        '''
        payload = zabbix_hosts_info.get_all_hosts_payload()
        return self._get_hosts(payload)

    def get_customer_hosts(self,output_data=_output_data, **kwargs):
        '''

        :param output_data: default hostid and host.
        :param kwargs:  Return only those results that exactly match the given. hostid=10084
        :return: list
        '''

        payload = zabbix_hosts_info.get_customer_hosts_payload(output_data, **kwargs)
        return self._get_hosts(payload)
zabbix_hosts = ZabbixHosts()
# output_data = ["hostid","host"]
output_data = "extend"
host = ["FuJian-QZDX-Gateway","BeiJing-TZLT-Gateway"]
print(zabbix_hosts.get_customer_hosts(output_data=output_data,host=host))
