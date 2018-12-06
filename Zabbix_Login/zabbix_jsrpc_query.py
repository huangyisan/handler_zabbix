import login_info
from abc import ABCMeta, abstractmethod
import requests
import json


class JSRPCQuery(metaclass=ABCMeta):

    def __init__(self):
        self.username = login_info.logininfo.get('username')
        self.password = login_info.logininfo.get('password')
        self.jsrpc_url = '{0}api_jsonrpc.php'.format(login_info.logininfo.get('url'))
        self.header = {"Content-Type": "application/json"}

    @abstractmethod
    def zabbix_jsrpc_query(self, payload):
        payload = json.dumps(payload).encode('utf-8')
        r = requests.post(url=self.jsrpc_url, data=payload, headers=self.header)
        return r.json()



