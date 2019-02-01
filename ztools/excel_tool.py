import pandas as pd
import platform
import os

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
        df = pd.read_excel(self.expath,sheet_name='Sheet1')
        # print(df.columns)
        print(df['hostname'][0])
        for i in df.index:
            print(df['hostname'][i])




a = Excel(exname='my.xlsx')
a.get_multi_hosts_values()