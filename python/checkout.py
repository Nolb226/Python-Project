import connect

class Checkout():
    def __init__(self, staffId, checkOutTime):
        self.staffId = staffId
        self.checkOutTime = checkOutTime

    def insert(self):
        connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
        connector.connect()
        sql = "INSERT INTO `checkout` (`staffId`, `checkOutTime`) VALUES (%s,%s)"
        connector.cursor.execute(sql, (self.staffId, self.checkOutTime))
        connector.connection.commit()
        connector.disconnect()

def select(date):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    if date == "":
        sql = "SELECT * FROM `checkout`"
        connector.cursor.execute(sql)
    else: 
        sql = "SELECT * FROM `checkout` where DATE(checkOutTime) = %s"
        connector.cursor.execute(sql,(date,))
    result = connector.cursor.fetchall()
    return result

# print(select())
