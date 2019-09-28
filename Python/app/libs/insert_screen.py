from app.libs.sql_lib.connect_to_mssql import get_connect_ms_sql
import json
from datetime import datetime


def insert_to_alert_history(name, left_eye, right_eye):
    with get_connect_ms_sql() as connect:
        cursor = connect.cursor()
        cursor.execute("insert into hackaton.dbo.screen_history values (convert(varchar, getdate(), 120), '{}',{},{});".format(name, left_eye, right_eye))
        cursor.commit()
