from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def zabbix_hostgroups_info(name,output_data):
    zabbix_hostgroups_info = {
        "jsonrpc": "2.0",
        "method": "hostgroup.get",
        "params": {
            "output": output_data,
            "filter": {
                "name": name,
            }
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return zabbix_hostgroups_info