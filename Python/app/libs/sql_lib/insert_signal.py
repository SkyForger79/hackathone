from Python.app.libs.sql_lib.connect_to_mssql import get_connect_ms_sql
import json
from datetime import datetime

def insert_to_alert_history(**kwargs):    
    with get_connect_ms_sql() as connect: 
        cursor = connect.cursor()
        for k, v in kwargs.items():
            cursor.execute("""
                insert into hackaton.dbo.alert_history 
                (alert_time, dev_name, val, is_sent)
                values (?, ?, ?, ?)
            """, (datetime.now(), k, v, 0))
        cursor.commit()
    return {'status': 'ok'}


# def insert_alert_to_database(**kwargs):
#     with get_connect_ms_sql() as connect:
#         cursor = connect.cursor()
#         for k, v, n in kwargs.items():
#             cursor.execute("""
#                 insert into hackaton.dbo.alert_base (head,body,img,level)
#                 values ('?', '?', '?', '?')
#             """, (k, v, n, 'danger'))
#         cursor.commit()
#     return {'status': 'ok'}

def insert_alert_to_database(k, v, n):
    with get_connect_ms_sql() as connect:
        cursor = connect.cursor()

        sql = "use hackaton; insert into hackaton.dbo.alert_base (head,body,img,level) values ('{}','{}','{}','{}')".format(k, v, n, 'danger')
        cursor.execute(sql)
        cursor.commit()
    return {'status': 'ok'}