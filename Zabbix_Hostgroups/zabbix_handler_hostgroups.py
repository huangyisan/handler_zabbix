from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_hostgroups_info

class ZabbixHostGroups(JSRPCQuery):
    _output_data = ["groupid", "name"]

    def _action_hostgroup(self,payload):
        '''

        :param payload: 通用方法
        :return:
        '''
        result = self.zabbix_jsrpc_query(payload)
        result = result.get("result",result.get("error",""))
        return result

    def get_customer_hostgroups(self,name,output_data=_output_data):
        '''

        :param name: 待查询组名，list
        :param output_data: 输出过滤内容
        :return:
        '''

        payload = zabbix_hostgroups_info.zabbix_hostgroups_info(name,output_data)

        return self._action_hostgroup(payload)

zabbix_hostgroups = ZabbixHostGroups()
name = ['test-zabbix','DNS-lts']
print(zabbix_hostgroups.get_customer_hostgroups(name=name))
