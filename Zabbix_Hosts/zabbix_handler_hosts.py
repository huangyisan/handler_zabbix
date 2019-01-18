from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info



class ZabbixHosts(JSRPCQuery):
    _output_data = ["hostid", "host"]

    def _get_hosts(self,payload):
        '''

        :param payload: 通用方法
        :return:
        '''
        return self.zabbix_jsrpc_query(payload).get("result","")

    def get_all_hosts(self, visiable=None):
        '''

        :param visiable: payload是否打印输出
        :return:
        一般不会直接用到，但可基于该方法扩展。
        '''
        payload = zabbix_hosts_info.get_all_hosts_payload(visiable)
        if visiable:
            print("The payload is:\n" + "{0}".format(payload))
        return self._get_hosts(payload)

    def get_customer_hosts(self,visiable=None,proxy_hosts=None,monitored_hosts=None,output_data=_output_data, **kwargs):
        '''

        :param output_data: 指定输出内容。type list
        :param visiable: payload是否打印输出
        :param kwargs: 过滤规则 type list
        :return:
        指定输出内容，默认输出hostid,host信息，可自定义过滤规则。
        '''
        payload = zabbix_hosts_info.get_customer_hosts_payload(proxy_hosts,monitored_hosts,output_data, **kwargs)

        if visiable:
            print("The payload is:\n" + "{0}".format(payload))
        return self._get_hosts(payload)

    def search_customer_hosts(self):

        pass

zabbix_hosts = ZabbixHosts()
output_data = ["hostid","host"]
# output_data = "extend"
host = ["FuJian-QZDX-Gateway","BeiJing-TZLT-Gateway"]
# print(zabbix_hosts.get_customer_hosts(visiable=1,output_data=output_data))
print(len(zabbix_hosts.get_customer_hosts(proxy_hosts=True,visiable=1,output_data=output_data)))
# print(zabbix_hosts.get_customer_hosts(host=host))
