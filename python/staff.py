import connect
    
def search(id):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT * FROM `staff` WHERE id = '{}'".format(id)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()
    return result

def select_id():
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT staff.id FROM `staff`"
    connector.cursor.execute(sql)
    result = connector.cursor.fetchall()
    id = []
    for i in range(0, len(result)):
        id.append(result[i][0])
    return id



