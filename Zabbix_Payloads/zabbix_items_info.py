from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def get_customer_items_payload(output_data,**kwargs):
    get_customer_items_payload = {
        "jsonrpc": "2.0",
        "method": "item.get",

        "params": {
            'selectHosts': ['hostids', 'proxy_hostid'],
            "search":{"name":['*To-charge_cucc_beijing_sjqlt_01*Bits received',"*To-charge_ctcc_fujian_qzdx_01*Bits received"]},
            "searchWildcardsEnabled":"true",
            "searchByAny":"true",
            # "hostids": "10638",
            "output": output_data,
            "filter": kwargs
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return get_customer_items_payload

def search_items_payload(selecthosts, searchwildcardsenabled, searchbyany,output_data,**kwargs):
    '''

    :param selecthosts:
    :param searchwildcardsenabled:
    :param searchbyany:
    :param output_data:
    :param kwargs:
    :return:
    '''
    search_items_payload = {
        "jsonrpc": "2.0",
        "method": "item.get",

        "params": {
            'selectHosts': selecthosts,
            "search":kwargs,
            "searchWildcardsEnabled":searchwildcardsenabled,
            "searchByAny":searchbyany,
            "output": output_data,
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return search_items_payload
