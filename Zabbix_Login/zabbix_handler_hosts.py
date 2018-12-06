from zabbix_handler_login import ZBXLogin
import requests
import json



class ZBXHosts(object):
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
            "auth": "{0}".format(ZBXLogin().get_token()),
            "id": 1
        }


c = ZBXHosts()
print(c.get_hosts())