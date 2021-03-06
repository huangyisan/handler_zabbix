from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def get_all_hosts_payload(visiable):
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


def get_customer_hosts_payload(limit, proxy_hosts, monitored_hosts, output_data, **kwargs):

    get_customer_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.get",

        "params": {
            "output": output_data,
            "filter": kwargs,
            "limit":limit,

        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }


    get_proxy_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.get",

        "params": {
            "proxy_hosts":"true",
            "output": output_data,
            "filter": kwargs,
            "limit":limit
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }

    monitored_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.get",

        "params": {
            "monitored_hosts":monitored_hosts,
            "output": output_data,
            "filter": kwargs,
            "limit":limit,

        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    if proxy_hosts:
        return get_proxy_hosts_payload
    if monitored_hosts:
        return monitored_hosts_payload
    return get_customer_hosts_payload

def search_hosts_payload(limit, output_data, **kwargs):
    search_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.get",

        "params": {
            "output": output_data,
            "search": kwargs,
            "limit":limit,
            "searchWildcardsEnabled":"true",
            "searchByAny":"true"

        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return search_hosts_payload

def add_host_payload(host,groupid,templateid,interfaces):
    add_host_payload = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": host,
            "interfaces": [
                {
                    "type": interfaces.get('type'),
                    "main": interfaces.get('main'),
                    "useip": interfaces.get('useip'),
                    "ip": interfaces.get('ip'),
                    "dns": interfaces.get('dns'),
                    "port": interfaces.get('port'),
                }
            ],
            "groups": groupid,
            "templates": templateid,
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return add_host_payload

def delete_hosts_payload(hostsids):
    delete_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "host.delete",
        "params": hostsids,
         "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return delete_hosts_payload
