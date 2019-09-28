from app.libs.sql_lib.connect_to_mssql import get_connect_ms_sql

def get_last_signals():
    with get_connect_ms_sql as connect:
        cursor = connect.cursor()
        cursor
