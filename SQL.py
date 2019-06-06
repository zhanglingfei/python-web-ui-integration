import pymssql


server = "54.200.20.76"    # 连接服务器地址
user = "sa"       # 连接帐号
password = "nomura@@8341"      # 连接密码
charset='utf8'

conn = pymssql.connect(server, user, password, "SQL_Test",charset)  #获取连接

cursor = conn.cursor()


