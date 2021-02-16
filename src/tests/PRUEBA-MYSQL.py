import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='djruber',
            password='Ericsson2018@',
            db='djangochannels'
        )

        self.cursor = self.connection.cursor()
        print("Coneccion exitosa")

    def select_all(self):
        sql = "SELECT * FROM alert_alert"

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            print(user)
        except Excetion as e:
            False

database = Database()
database.select_all()