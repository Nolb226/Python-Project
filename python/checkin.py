import connect
import datetime

class Checkin():
    def __init__(self, staffId, checkInTime):
        self.staffId = staffId
        self.checkInTime = checkInTime

    def insert(self):
        connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
        connector.connect()
        sql = "INSERT INTO `checkin` (`staffId`, `checkInTime`) VALUES (%s,%s)"
        connector.cursor.execute(sql, (self.staffId, self.checkInTime))
        connector.connection.commit()
        connector.disconnect()

