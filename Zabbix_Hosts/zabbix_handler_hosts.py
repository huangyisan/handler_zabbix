from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hosts_info
from ztools import format_print

class ZabbixHosts(JSRPCQuery):

    _output_data = ["hostid", "host", "status"]

    def _action_hosts(self,payload):
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
        return self._action_hosts(payload)

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
            return len(self._action_hosts(payload))

        return self._action_hosts(payload)

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
            return len(self._action_hosts(payload))

        return self._action_hosts(payload)

    def add_hosts(self,host,groupid,templateid,_type=1,main=1,useip=1,ip='127.0.0.1',dns="",port="10050",check=True):
        groupid = list(map(lambda x:{"groupid":x},groupid))
        templateid = list(map(lambda x:{"templateid":x},templateid))


        if isinstance(ip,str) and isinstance(dns,str) and isinstance(port, str):

            interfaces = {
                "type": _type,
                "main": main,
                "useip": useip,
                "ip": ip,
                "dns": dns,
                "port": port,
            }

            payload = zabbix_hosts_info.add_hosts_payload(host=host,groupid=groupid,interfaces=interfaces,templateid=templateid)
            if check:
                title = 'Check Mode will not make any changes on remote systems!\nSet check=False will disable Check Mode!'
                content = 'The payload is: \n{payload}'.format(payload=payload)
                status = "warning"
                format_print.print_load(title=title, content=content,status=status)
            else:
                recall = self._action_hosts(payload)
                try:
                    if recall.get('hostids',None):
                        title = 'Add host [{0}] success!'.format(host)
                        content = "{0}".format(recall)
                        status = "success"
                        format_print.print_load(title=title, content=content, status=status)
                        return recall
                except Exception as e:
                    title = 'Add host [{0}] failure!'.format(host)
                    content = 'The host may already exists or other fault!\nThe payload is:\n{0}'.format(payload)
                    status = "error"
                    format_print.print_load(title=title, content=content, status=status)

a = ZabbixHosts()
host = 'test-zabbix'
# groupid = "320"
groupid = ["320","123"]
# templateid = ["10778","10248"]
templateid = ["10778","10832"]
print(a.add_hosts(host=host,groupid=groupid,check=False,templateid=templateid))