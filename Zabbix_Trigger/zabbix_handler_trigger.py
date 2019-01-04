from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_triggers_info

VALID_STATUS_BOOLEAN = {0, 1}

class ZabbixTrigger(JSRPCQuery):

    # 获取当前告警信息数量
    def get_count_trigger(self,maintenance):
        '''

        :param maintenance: 1 只显示维护  0 不显示维护
        :return:
        '''
        if maintenance not in VALID_STATUS_BOOLEAN:
            raise ValueError("results: status must be one of {0}.".format(VALID_STATUS_BOOLEAN))

        payload = zabbix_triggers_info.count_alerts_payload(maintenance=maintenance)
        return self.zabbix_jsrpc_query(payload).get("result","")

    # 获取详细告警信息
    def get_detail_trigger(self,maintenance):
        '''

        :param maintenance:  1 只显示维护  0 不显示维护
        :return:
        '''
        if maintenance not in VALID_STATUS_BOOLEAN:
            raise ValueError("results: status must be one of {0}.".format(VALID_STATUS_BOOLEAN))

        payload = zabbix_triggers_info.detail_alerts_payload(maintenance=maintenance)
        return self.zabbix_jsrpc_query(payload).get("result","")

c = ZabbixTrigger()
print(c.get_count_trigger(maintenance=0))
print(c.get_detail_trigger(maintenance=0))