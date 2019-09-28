from app.libs.sql_lib import connect_to_mssql
import json


def insert_to_alert_history(record, dt):
    print(record, dt)
    return {'status': 'ok'}
    # with connect_to_mssql() as connect: 
    #     cursor = connect.cursor()
    #     cursor.execute("hackaton.dbo.alert_history values (?, ?, ?)", (json.dumps(record),))
    #     cursor.commit()