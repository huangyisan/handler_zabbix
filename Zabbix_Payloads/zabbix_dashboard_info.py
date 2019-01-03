from Zabbix_Login.zabbix_handler_login import ZabbixLogin

all_dashboards_payload = {
    "jsonrpc": "2.0",
    "method": "dashboard.get",
    "params": {
        # "output": "extend",
        "selectWidgets": "extend",
        "filter":{
            'private': '0'
        },
        "dashboardids": [
            "1"
        ]
    },
    "auth": "{0}".format(ZabbixLogin().get_token()),
    "id": 1
}