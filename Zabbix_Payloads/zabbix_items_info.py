from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def get_customer_items_payload(output_data,host,visiable, **kwargs):
    get_customer_items_payload = {
        "jsonrpc": "2.0",
        "method": "item.get",
        "params": {
            "host": host,
            "output": output_data,
            "filter": kwargs
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }

    if visiable:
        print("The payload is:\n" + "{0}".format(get_customer_items_payload))

    return get_customer_items_payload

def search_items_payload(selecthosts, searchwildcardsenabled, searchbyany,output_data, visiable,**kwargs):
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

    if visiable:
        print("The payload is:\n" + "{0}".format(search_items_payload))

    return search_items_payload
