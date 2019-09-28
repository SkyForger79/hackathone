from app.libs.sql_lib.connect_to_mssql import get_connect_ms_sql
import json
from datetime import datetime

def insert_to_alert_history(**kwargs):    
    with get_connect_ms_sql() as connect: 
        cursor = connect.cursor()
        for k, v in kwargs.items():
            cursor.execute("""
                insert into hackaton.dbo.alert_history 
                (atime, aname, val)
                values (?, ?, ?)
            """, (datetime.now(), k, v))
        cursor.commit()
    return {'status': 'ok'}