import connect

def select_all():
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT dutyName FROM `duty`"
    connector.cursor.execute(sql)
    result = connector.cursor.fetchall()
    name = []
    for i in range(0, len(result)):
        name.append(result[i][0])
    return name

def select_id(code):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT dutyName FROM `duty` where dutyCode = '{}'".format(code)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()[0]
    return result

def select_name(name):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT dutyCode FROM `duty` where dutyName = '{}'".format(name)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()[0]
    return result
