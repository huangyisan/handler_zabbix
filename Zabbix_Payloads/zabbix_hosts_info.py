from Zabbix_Login.zabbix_handler_login import ZabbixLogin

all_hosts_payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "filter": {
            "host": [
                "Zabbix server",
                "Linux server"
            ]
        }
    },
    "auth": "{0}".format(ZabbixLogin().get_token()),
    "id": 1
}