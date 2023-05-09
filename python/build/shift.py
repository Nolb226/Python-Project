import connect

class Shift():
    def __init__(self, staffId, date, inTime, outTime):
        self.staffId = staffId
        self.date = date
        self.inTime = inTime
        self.outTime = outTime
    
    def insert(self):
        connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
        connector.connect()
        try:
            sql = "INSERT INTO `shift` (`staffId`, `date`, `inTime`, `outTime`) VALUES (%s,%s,%s,%s)"
            connector.cursor.execute(sql, (self.staffId, self.date, self.inTime, self.outTime))
        except:
            sql = "UPDATE `shift` SET `inTime`= %s,`outTime`= %s WHERE `staffId` = %s and `date` = %s"
            connector.cursor.execute(sql, ( self.inTime, self.outTime, self.staffId, self.date))
        connector.connection.commit()
        connector.disconnect()

def select(start, end):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT * FROM `shift` where date >= %s and date <= %s"
    connector.cursor.execute(sql, (start, end))
    result = connector.cursor.fetchall()
    return result

def select_day(start, end):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT date FROM `shift` where date >= %s and date <= %s group by date"
    connector.cursor.execute(sql, (start, end))
    result = connector.cursor.fetchall()
    return result

def select_in_time(id, date):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT inTime FROM `shift` WHERE staffId = '{}' and date = '{}'".format(id,date)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()
    if result is not None:
        return result[0]
    else: 
        return None

def select_out_time(id, date):
    connector = connect.MySQLConnector("localhost", "root", "", "qlnv")
    connector.connect()
    sql = "SELECT outTime FROM `shift` WHERE staffId = '{}' and date = '{}'".format(id,date)
    connector.cursor.execute(sql)
    result = connector.cursor.fetchone()
    if result is not None:
        return result[0]
    else: 
        return None
    
def select_shift(id, date):
    start = select_in_time(id, date)
    end = select_out_time(id,date)
    if start is not None and end is not None:
        return "{} - {}".format(start, end)
    else:
        return "OFF"

