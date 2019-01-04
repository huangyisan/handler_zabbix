from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def count_alerts_payload(maintenance=0, countoutput=0):
    '''

    :param maintenance:
    :param countoutput:
    :return: json type
    '''
    count_alerts_payload = {
        "jsonrpc": "2.0",
        "method": "trigger.get",
        "params": {
            "countOutput":1,
            # "output": [
            #     "triggerid",
            #     "description",
            #     "priority"
            # ],
        "filter": {
                "value": 1
                  },
        "selectHosts": ['host'],
        "monitored":"True",
        "active":"True",
        "maintenance":"{maintenance}".format(maintenance=maintenance),
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return count_alerts_payload

def detail_alerts_payload(maintenance):
    detail_alerts_payload = {
        "jsonrpc": "2.0",
        "method": "trigger.get",
        "params": {
            # "countOutput":"{countoutput}".format(countoutput=countoutput),
            "output": [
                "triggerid",
                "description",
                "priority"
            ],
        "filter": {
                "value": 1
                  },
        "selectHosts": ['host'],
        "monitored":"True",
        "active":"True",
        "maintenance":"{maintenance}".format(maintenance=maintenance),
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return detail_alerts_payload
