import connect
import datetime

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

