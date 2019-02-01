import pandas as pd
import numpy as np
import platform
import os
import sys
from enum import Enum,unique

@unique
class HostInterfaceMain(Enum):
    agent = 1
    SNMP = 2
    IPMI = 3
    JMX = 4

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
        print(df.columns)
        for i in df.index:
            try:
                hostname = df['hostname'][i]
                groupname = df['groupname'][i]
                templatename = df['templatename'][i]
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

            # s = pd.Series([2, 3, np.nan, 7, "The Hobbit"])
            # print(s.isnull())

            ex_list = [hostname, groupname, templatename, interface_type, maint_ype, useip, ip, dns, port, check]

            # yield ex_list
            print(ex_list)

a = Excel(exname='my.xlsx')
a.get_multi_hosts_values()