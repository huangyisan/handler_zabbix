import pandas as pd
import platform
import os
import sys
from ztools.format_print import print_load
from Zabbix_Hostgroups.zabbix_handler_hostgroups import ZabbixHostGroups
from Zabbix_Templates.zabbix_handler_templates import ZabbixTemplates

class Excel(object):

    def __init__(self,exname):
        self.exname = exname
        self.expath = self.get_excel_path()

    def get_excel_path(self):
        expath = os.path.abspath(os.path.dirname(__file__))
        osplatform = platform.system()
        if osplatform == "Windows":
            return expath  + '\\' + 'excels' + '\\' + self.exname
        else:
            return expath + '/' + 'excels' + '/' + self.exname

    def get_multi_hosts_values(self):

        # Interface type
        _type = {
            'agent': 1,
            'SNMP': 2,
            'IPMI': 3,
            'JMX' : 4
        }

        # Whether the interface is used as default on the host. Only one interface of some type can be set as default on a host.
        _main = {
            'notdefault': 0,
            'default': 1
        }

        # Whether the connection should be made via IP.
        _useip = {
            'dns': 0,
            'ip': 1
        }

        df = pd.read_excel(self.expath,sheet_name='Sheet1')

        # 判断excel中是否存在空
        if df.isnull().any().sum():
            title = "Read excel content error!"
            content = "Some cells are not filled in"
            status = "error"
            print_load(title, content, status)
            sys.exit(1)

        for i in df.index:
            try:
                hostname = df['hostname'][i]
                groupname = df['groupname'][i].split("|")
                templatename = df['templatename'][i].split("|")
                interface_type = _type[df['interface type'][i]]
                maint_ype = _main[df['main'][i]]
                useip = _useip[df['useip'][i]]
                ip = df['ip'][i]
                dns = df['dns'][i]
                port = df['port'][i]
                check = df['check'][i]
            except KeyError as e:
                print(e)
                sys.exit(1)

            # get groupid via groupname
            zhg = ZabbixHostGroups()
            output_data = ["groupid"]
            # print(templatename)
            groupid = zhg.get_customer_hostgroups(name=groupname,output_data=output_data)
            groupname = [i.get("groupid") for i in groupid]

            # get templateid via templatename
            zt = ZabbixTemplates()
            output_data = ["templateid"]
            templateid = zt.get_template_id(templatename=templatename,output_data=output_data)
            templatename = [i.get('templateid') for i in templateid]

            ex_list = [hostname, groupname, templatename, interface_type, maint_ype, useip, ip, dns, port, check]

            print(ex_list)

            # yield ex_list

a = Excel(exname='my.xlsx')
a.get_multi_hosts_values()