from Zabbix_JSRPC import zabbix_jsrpc_query
from Zabbix_Login.zabbix_handler_login import ZabbixLogin
import requests
import json



class ZabbixHosts(object):
    def __init__(self):
        pass

    def get_hosts(self):
        payload = {
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
        return payload

c = ZabbixHosts()
print(c.get_hosts())