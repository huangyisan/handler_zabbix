from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_templates_info


class ZabbixTemplates(JSRPCQuery):

    # 获取templateid
    def get_template_id(self,templatename):
        payload = zabbix_templates_info.get_template_payload(templatename)
        return self.zabbix_jsrpc_query(payload).get("result", "")[0].get('templateid')

    # 批量添加模板，和hosts关联
    def mass_add_templates(self,templatename, hosts_list):
        '''
        
        :param templatename: 
        :param hosts_list:   hosts_list = [{'hostid': '10423'}, {'hostid': '10433'}]
        :return: 
        '''
        templateid = self.get_template_id(templatename)
        payload = zabbix_templates_info.mass_add_templates_hosts_payload(templateid, hosts_list)
        return self.zabbix_jsrpc_query(payload).get("result","")