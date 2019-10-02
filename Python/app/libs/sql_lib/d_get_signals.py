
from Python.app.libs.sql_lib.connect_to_mssql import get_connect_ms_sql

def update_sig():
    connect = get_connect_ms_sql()
    cursor = connect.cursor()
    sql_select_query = """select * from  hackaton.dbo.alert_history where is_sent = 0"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()

    for row in record:
        id = row[0]
        cursor.execute("""update hackaton.dbo.alert_history set is_sent = 1 where alert_id = {}""".format(id))
        cursor.commit()


def get_last_signals():
    connect = get_connect_ms_sql()
    cursor = connect.cursor()
    answer_dict = dict()
    for i in ('light', 'micro', 'sonar', 'humidity', 'temperature', 'fatigue'):
        sql = """select top 1 * from  hackaton.dbo.alert_history where is_sent = 0 and dev_name='{}'""".format(i)
        cursor.execute(sql)
        for row in cursor.fetchall():
            answer_dict[i] = {"timestamp": str(row[1]), "val": row[3]}
    update_sig()
    return answer_dict


def get_all_signals():
    connect = get_connect_ms_sql()
    cursor = connect.cursor()
    sql_select_query = """select * from  hackaton.dbo.alert_base where alert_time >= cast(GETDATE() as date) order by id desc"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    answer_list = list()

    for row in record:
        answer_dict = dict()
        answer_dict["id"] = row[0]
        answer_dict["head"] = row[1]
        answer_dict["body"] = row[2]
        answer_dict["img"] = row[3]
        answer_dict["level"] = row[4]
        answer_dict["datetime"] = str(row[5])
        answer_list.append(answer_dict)
    return answer_list