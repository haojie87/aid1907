'''
mysql.py
pymysql 操作数据库基本流程
'''
import pymysql


db = pymysql.connect(host='localhost', port=3306, user='root', password='123456',database= 'stu',charset='utf8')
# 获取游标(操作数据库,执行sql语句,得到执行结果)
cur = db.cursor()
cur1 = db.cursor()
cur2 = db.cursor()
# 执行语句
sql = "insert into interest values (6, 'Elit', 'draw','C',1480,'xxx');"
sql1 = "insert into interest values (4, 'Jam', 'sing','A',1880,'xxx');"
sql2 = "insert into interest values (3, 'Tony', 'draw','C',1480,'xxx');"
cur.execute(sql)
cur1.execute(sql1)
cur2.execute(sql2)
# 提交到数据库
db.commit()
# 关闭游标
cur.close()
cur1.close()
cur2.close()
# 关闭数据库
db.close()