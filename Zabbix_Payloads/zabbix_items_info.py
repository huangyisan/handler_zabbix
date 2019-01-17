from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def get_customer_items_payload(output_data,**kwargs):
    get_customer_items_payload = {
        "jsonrpc": "2.0",
        "method": "item.get",

        "params": {
            "hostids": "10638",
            "output": output_data,
            "filter": kwargs
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }

    return get_customer_items_payload