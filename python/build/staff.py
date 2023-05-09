import connect
    
def search(id):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT * FROM `staff` WHERE id = '{}' and status = 1".format(id)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()
    return result

def search2(id):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT * FROM `staff` WHERE id = '{}'".format(id)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()
    return result

def select_all():
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT * FROM `staff` where status = 1 order by isduty"
    connector.cursor.execute(sql)
    result = connector.cursor.fetchall()
    return result

def select_id():
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT staff.id FROM `staff` where status = 1"
    connector.cursor.execute(sql)
    result = connector.cursor.fetchall()
    id = []
    for i in range(0, len(result)):
        id.append(result[i][0])
    return id

def select_name():
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT staff.name FROM `staff` where status = 1"
    connector.cursor.execute(sql)
    result = connector.cursor.fetchall()
    name = []
    for i in range(0, len(result)):
        name.append(result[i][0])
    return name

def insertStaff(id, username, birthDay, isDuty):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "INSERT INTO staff (`id`,`name`,`birthday`,`isDuty`,`status`) VALUES (%s, %s, %s, %s,1)"
    val = (id, username, birthDay, isDuty)
    connector.cursor.execute(sql, val)
    connector.connection.commit()
    connector.disconnect()

def select_one_name(id):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT name FROM `staff` WHERE id = '{}' and status = 1".format(id)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()
    return result[0]

def update(id, username, birthDay, isDuty):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "UPDATE staff SET name = %s, birthday = %s, isDuty = %s where id = %s"
    val = ( username, birthDay, isDuty, id)
    connector.cursor.execute(sql, val)
    connector.connection.commit()
    connector.disconnect()

def delete(id):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "UPDATE staff SET status = 0 where id = {}".format(id)
    connector.cursor.execute(sql)
    connector.connection.commit()
    connector.disconnect()