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

    def get_customer_hosts(self,countoutput=None,limit=None,visiable=None,proxy_hosts=None,monitored_hosts=None,output_data=_output_data, **kwargs):
        '''

        :param countoutput: 输出匹配条目数
        :param limit: 限制输出条目数，默认50
        :param visiable: 是否打印输出payload
        :param proxy_hosts: 是否只输出proxy_host
        :param monitored_hosts: 是否只输出监控中的机器
        :param output_data: 指定输出内容
        :param kwargs: 过滤规则
        :return:
        '''
        if not limit:
            limit = 50

        payload = zabbix_hosts_info.get_customer_hosts_payload(limit=limit, proxy_hosts=proxy_hosts, monitored_hosts=monitored_hosts, output_data=output_data,
                                                                   **kwargs)
        if visiable:
            print("The payload is:\n" + "{0}".format(payload))

        if countoutput:
            return len(self._get_hosts(payload))

        return self._get_hosts(payload)

    def search_customer_hosts(self):
        pass

zabbix_hosts = ZabbixHosts()
output_data = ["hostid","host"]
# output_data = "extend"
host = ["FuJian-QZDX-Gateway","BeiJing-TZLT-Gateway"]
print(zabbix_hosts.get_customer_hosts(countoutput=True,limit=40,visiable=1,output_data=output_data,monitored_hosts="true",host=host))
# print(len(zabbix_hosts.get_customer_hosts(proxy_hosts=True,visiable=1,output_data=output_data)))
# print(zabbix_hosts.get_customer_hosts(host=host))
