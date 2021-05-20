import pymysql


class MySqlCom(object):
    def __init__(self, host='localhost', user='root', password='muzili', database='ApiTool', port=3306,
                 charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.db = None

    def __del__(self):
        try:
            self.db.close()
        except AttributeError as e:
            print(e)

    def to_connected(self):
        try:
            self.db = pymysql.Connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                      port=self.port, charset=self.charset)
            return True
        except pymysql.err.OperationalError:
            return False
