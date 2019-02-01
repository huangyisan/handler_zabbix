from Zabbix_Login.zabbix_handler_login import ZabbixLogin

def get_template_payload(templatename,output_data):
    get_template_payload = {
        "jsonrpc": "2.0",
        "method": "template.get",
        "params": {
            "output": output_data,
            "filter": {
                "host": templatename,
            }
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
        }
    return get_template_payload


def mass_add_templates_hosts_payload(templateid,hosts_list):

    mass_add_templates_hosts_payload = {
        "jsonrpc": "2.0",
        "method": "template.massadd",
        "params": {
            "templates": [
                {
                    "templateid": templateid
                }
            ],
            "hosts": hosts_list
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return mass_add_templates_hosts_payload

def mass_add_templates_group_payload(templateid):
    mass_add_templates_group_payload = {
        "jsonrpc": "2.0",
        "method": "template.massadd",
        "params": {
            "templates": [
                {
                    "templateid": templateid
                }
            ],
            "groups": [
                {
                    "groupid": "10106"
                },
                {
                    "groupid": "10104"
                }
            ]
        },
        "auth": "{0}".format(ZabbixLogin().get_token()),
        "id": 1
    }
    return mass_add_templates_group_payload