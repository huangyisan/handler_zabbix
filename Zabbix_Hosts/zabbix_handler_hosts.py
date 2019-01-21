from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info
from ztools import format_print

class ZabbixHosts(JSRPCQuery):

    _output_data = ["hostid", "host", "status"]


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

    def search_customer_hosts(self,limit=None,countoutput=None,visiable=None,output_data=_output_data, **kwargs):
        '''
        已开启searchWildcardsEnabled,searchByAny参数
        :param limit: 限制输出条目数，默认50
        :param countoutput: 输出匹配条目数
        :param visiable: 是否打印输出payload
        :param output_data: 指定输出内容
        :param kwargs: 搜索规则
        :return: 
        '''

        if not limit:
            limit = 50

        payload = zabbix_hosts_info.search_hosts_payload(limit=limit, output_data=output_data, **kwargs)
        if visiable:
            print("The payload is:\n" + "{0}".format(payload))

        if countoutput:
            return len(self._get_hosts(payload))

        return self._get_hosts(payload)

    def add_hosts(self,host,groupid,type=1,main=1,useip=1,ip='127.0.0.1',dns="",port=10050,check=True):

        interfaces = {
            "type": type,
            "main": main,
            "useip": useip,
            "ip": ip,
            "dns": dns,
            "port": port,
        }

        payload = zabbix_hosts_info.add_hosts_payload(host=host,groupid=groupid,interfaces=interfaces)
        if check:
            title = 'Check Mode will not make any changes on remote systems!\nSet check=False will disable Check Mode!'
            conetent = 'The payload is: \n{payload}'.format(payload=payload)
            format_print.print_load(title=title, content=conetent)
        else:
            return self._get_hosts(payload)



a = ZabbixHosts()
host = 'test-zabbix'
groupid = 123

a.add_hosts(host=host,groupid=groupid)