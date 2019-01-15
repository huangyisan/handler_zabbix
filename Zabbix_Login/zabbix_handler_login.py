from Zabbix_JSRPC.zabbix_jsrpc_query import JSRPCQuery
from Zabbix_Payloads import zabbix_auth_info
from ztools.sqlit_tool import Sqlite
import sys

class ZabbixLogin(JSRPCQuery):

    def get_token_via_api(self):
        payload = zabbix_auth_info.auth_payload
        result = self.zabbix_jsrpc_query(payload)
        if result.get('error'):
            print("Login Failed!")
            sys.exit(1)
        return result.get('result')

    def get_token(self):

        _select_token_table_sql = '''SELECT count(*) FROM sqlite_master WHERE type='table' AND name=\'{TABLE_NAME}\';'''.format(TABLE_NAME=Sqlite().get_table_name)
        print(_select_token_table_sql)
        _create_table_sql = '''CREATE TABLE TOKEN (ID INT PRIMARY KEY NOT NULL, TOKEN TEXT NOT NULL);'''
        _insert_token_sql = '''INSERT INTO TOKEN (ID,TOKEN) VALUES (1, \'{TOKEN}\')'''.format(TOKEN=self.get_token_via_api())
        _select_token_sql = '''SELECT TOKEN from TOKEN'''

        token_sqlite = Sqlite()
        conn = token_sqlite.sqlite_conn()
        if token_sqlite.sqlite_select(conn=conn, sql=_select_token_table_sql) != 1:
            token_sqlite.sqlite_execute(conn=conn, sql=_create_table_sql)
            token_sqlite.sqlite_execute(conn=conn, sql=_insert_token_sql)

        elif token_sqlite.sqlite_select(conn=conn, sql=_select_token_table_sql) == 1 and token_sqlite.sqlite_select(conn=conn, sql=_select_token_sql) is None:
            token_sqlite.sqlite_execute(conn=conn, sql=_insert_token_sql)

        token = token_sqlite.sqlite_select(conn=conn, sql=_select_token_sql)
        token_sqlite.sqlite_close(conn)
        return token
