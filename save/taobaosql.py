import pymysql

class SavePhone:
    def __init__(self):
        db = {
            "host": "localhost",
            "port": 3306,
            "user": 'root',
            "passwd": '123',
            "db": "taobao",
            "charset": "utf8"
        }
        self.conn = pymysql.Connect(**db)
        self.cur = self.conn.cursor()
    def maxindex(self):
        sql = 'select max(id) from goods'
        self.cur.execute(sql)
        res = self.cur.fetchall()
        # print(type(res))
        if res[0][0]:
            return res[0][0]
        else:
            return -1
    def insert(self,data):
        try:
            sql = 'insert into goods value{}'.format(data)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_sql(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    conn = SavePhone()
    # conn.insert((0, '1加5T', '￥2500.0', '￥3500.0', 'jd自营', '10000'))
    n = conn.maxindex()
    print(n)
    conn.close_sql()