import pymysql

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='mrchoidb', password='qlqjs112!', db='class01')
        self.cur = self.db.cursor()
        print("DB good!!")

    def selectAllJson(self):
        sql = "select * from recordled;"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result

    def insertJson(self, status):
        val = ('{{"status":"{}"}}'.format(status))
        sql = "insert into recordled(data) values(%s);"
        self.cur.execute(sql, val)
        self.db.commit()
        return "good"
