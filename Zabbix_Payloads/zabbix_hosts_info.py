from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def get_all_hosts_payload(output_data):
    '''

    :param output_data: 需要回写的数据
    :return:
    '''
    get_all_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": output_data,
            # "filter": {
            #     "host": [
            #         "ShangHai-SJ-L3-MP-Zabbix-01"
            #     ]
            # }
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return get_all_hosts_payload