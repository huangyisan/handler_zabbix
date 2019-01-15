import sqlite3

class Sqlite(object):
    def __init__(self):
        self._db = 'token.db'

    @property
    def get_db_name(self):
        return self._db.upper()

    def sqlite_conn(self):
        conn = sqlite3.connect(self.get_db_name)
        return conn

    def sqlite_execute(self,conn,sql):
        c = conn.cursor()
        c.execute(sql)
        conn.commit()

    def sqlite_select(self,conn,sql):
        row_list = []
        c = conn.cursor()
        cursor = c.execute(sql)
        for row in cursor:
            row_list.append(row[0])
        return row_list[0]

    def sqlite_close(self,conn):
        return conn.close()


