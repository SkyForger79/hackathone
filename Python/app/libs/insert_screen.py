from app.libs.sql_lib.connect_to_mssql import get_connect_ms_sql
import json
from datetime import datetime


def insert_to_alert_history(name, eye):
    with get_connect_ms_sql() as connect:
        cursor = connect.cursor()
        sql = """
                insert into hackaton.dbo.screen_history (stime, sname, max_eye) values 
                (convert(varchar, getdate(), 120), '{}', {});
            """.format(name, eye)
        cursor.execute(sql)
        cursor.commit()


def get_fatigue_signal():
    with get_connect_ms_sql() as connect:
        cursor = connect.cursor()
        sql = """
            select 
                count(max_eye) as count_eve
            from hackaton.dbo.screen_history
            where 1 = 1
                and stime >= dateadd(MINUTE, -1,  GETDATE())   
                and max_eye > 0.5    
        """
        cursor.execute(sql)
        result = cursor.fetchone()
        if result >= 15:
            cursor.execute(
                """
                    
                    INSERT INTO hackaton.dbo.alert_history
                    ( 
                     [alert_time], [dev_name], [val], [is_sent]
                    )
                    VALUES
                    ( 
                     GETDATE(), 'fatigue', '{}', 0
                    )
                """.format(result)
            )
        cursor.commit()