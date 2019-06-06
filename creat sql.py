#-*- coding:utf-8 -*
import  SQL

SQL.cursor.execute("""
IF OBJECT_ID('student', 'U') IS NOT NULL
    DROP TABLE student
CREATE TABLE student (
    id INT NOT NULL,
    name NVARCHAR(100),
    department NVARCHAR(100),
    PRIMARY KEY(id)
)
""")


# 插入多行数据
SQL.cursor.executemany(
    "INSERT INTO student VALUES (%d, %s, %s)",
    [('001','杨桃','生科院'),
     ('002','高风','文学院'),
     ('003','刘想','计科院'),
     ('005','李林','数学院'),
     ('008','张之林','物理院')
     ])
# 你必须调用 commit() 来保持你数据的提交如果你没有将自动提交设置为true
SQL.conn.commit()