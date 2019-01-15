from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def get_all_hosts_payload():
    '''

    :param output_data: 需要回写的数据
    :return:
    '''
    get_all_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": "extend",
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return get_all_hosts_payload

def get_customer_hosts_payload(output_data,**kwargs):
    '''

    :param output_data: 需要回写的数据
    :return:
    '''
    get_customer_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": output_data,
            "filter": kwargs
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    print(get_customer_hosts_payload)
    return get_customer_hosts_payload