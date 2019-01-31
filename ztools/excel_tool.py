import xlwings as xw
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
        wb = xw.Book(self.expath)
        sht = wb.sheets['Sheet1']
        A1 = sht.range('A1').value
        print(A1)

