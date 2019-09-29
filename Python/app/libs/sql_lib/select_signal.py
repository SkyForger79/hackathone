
from app.libs.sql_lib.connect_to_mssql import get_connect_ms_sql

def get_last_signals():
    with get_connect_ms_sql as connect:
        cursor = connect.cursor()
        sql_select_query = """select * from laptop where id = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchall()

        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("Join Date = ", row[2])
            print("Salary  = ", row[3], "\n")