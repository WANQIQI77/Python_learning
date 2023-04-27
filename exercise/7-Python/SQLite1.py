import sqlite3

#链接到SQLite数据库
#数据库是test.db
#如果文件不存在，会自动在当前目录创建
coon=sqlite3.connect('test.db')

#创建一个Cursor
cursor=coon.cursor()

#执行一条SQL语句，创建user表：
cursor.execute('CREATE table user (id varchar(20) primary key ,name varchar(20))')

#插入一条记录
cursor.execute('insert into user (id,name) values (\'1\',\'Michael\')')

#通过rowcount获得行数
row=cursor.rowcount
print(row)

cursor.close()
coon.commit()
coon.close()