import sqlite3

class Sqlite(object):
    def __init__(self):
        self._db = 'token.db'
        self._table = 'token'

    @property
    def get_db_name(self):
        return self._db.upper()

    @property
    def get_table_name(self):
        return self._table.upper()

    def sqlite_conn(self):
        conn = sqlite3.connect(self.get_db_name)
        return conn

    def sqlite_execute(self,conn,sql,args=None):
        c = conn.cursor()
        if args:
            c.execute(sql,args)
        else:
            c.execute(sql)
        conn.commit()

    def sqlite_select(self,conn,sql,args=None):
        row_list = []
        c = conn.cursor()
        if args:
            cursor = c.execute(sql,args)
        else:
            cursor = c.execute(sql)
        for row in cursor:
            row_list.append(row[0])
            return row_list[0]

    def sqlite_close(self,conn):
        return conn.close()


a = Sqlite()