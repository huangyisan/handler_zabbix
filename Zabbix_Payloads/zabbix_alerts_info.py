from Zabbix_Login.zabbix_handler_login import ZabbixLogin

all_alerts_payload = {
    "jsonrpc": "2.0",
    "method": "trigger.get",
    "params": {
        "output": [
            "triggerid",
            "description",
            "priority"
        ],
    "filter": {
            "value": 1
              },
     "only_true": 4,
"selectHosts": ['host'],
    },
    "auth": "{0}".format(ZabbixLogin().get_token()),
    "id": 1
}