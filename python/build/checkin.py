import connect

class Checkin():
    def __init__(self, staffId=None, checkInTime=None):
        self.staffId = staffId
        self.checkInTime = checkInTime

    def insert(self):
        connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
        connector.connect()
        sql = "INSERT INTO `checkin` (`staffId`, `checkInTime`) VALUES (%s,%s)"
        connector.cursor.execute(sql, (self.staffId, self.checkInTime))
        connector.connection.commit()
        connector.disconnect()

def select_by_date(date):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    if date == "":
        sql = "SELECT * FROM `checkin`"
        connector.cursor.execute(sql)
    else: 
        sql = "SELECT * FROM `checkin` where DATE(checkInTime) = %s"
        connector.cursor.execute(sql,(date,))
    result = connector.cursor.fetchall()
    return result

def select_by_id(code):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    if code == "":
        sql = "SELECT * FROM `checkin`"
        connector.cursor.execute(sql)
    else: 
        sql = "SELECT * FROM `checkin` where staffId = %s"
        connector.cursor.execute(sql,(code,))
    result = connector.cursor.fetchall()
    return result

def select(code, date):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    if code == "":
        sql = "SELECT * FROM `checkin`"
        connector.cursor.execute(sql)
    else: 
        sql = "SELECT * FROM `checkin` where staffId = %s and DATE(checkInTime) = %s"
        connector.cursor.execute(sql,(code,date))
    result = connector.cursor.fetchall()
    return result

