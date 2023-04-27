import pymysql

# 打开数据库链接
db = pymysql.connect(host='localhost', user='root', password='123456', database='TESTDB')

# 使用cursor方法创建一个游标对象
cursor = db.cursor()

# 使用excute方法执行SQL查询
cursor.execute('SELECT VERSION()')

# 使用fetchone()方法获取单条数据
data = cursor.fetchone()

print("database version:%s" % data)

# SQL插入
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

db.close()
