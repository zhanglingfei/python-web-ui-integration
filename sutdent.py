from flask import Flask,request,url_for,render_template,redirect
import SQL



app=Flask(__name__)
app.config.from_object(SQL)

@app.route('/')                                            #这里是根目录，也就是打开链接第一个访问的页面
def index():
    SQL.cursor.execute('SELECT * FROM student ')
    row= SQL.cursor.fetchall()
    return render_template('index.html',student=row)   #这里的student=student，等号左边是要传给html文件的变量，右边是上面定义的二维列表

@app.route('/delstu',methods=['GET','POST'])               #这里是删除模块，对应的页面是/delstu
def delstu():
    if request.method=='POST':
        delid = request.form.get('delid')
        SQL.cursor.execute('SELECT * FROM student WHERE id=%d ',delid)
        row = SQL.cursor.fetchall()
        if row==[]:
            return '您输入的学号不存在'
        else:
            SQL.cursor.execute('DELETE FROM student WHERE id=%d ', delid)
            SQL.conn.commit()
            return redirect(url_for('index'))              #如果找到了输入的学号执行删除操作，并重定向到首页
    return render_template('delstu.html')

@app.route('/addstu',methods=['GET','POST'])               #这里是添加模块
def addstu():
    if request.method=='POST':
        addid = request.form.get('addid')
        SQL.cursor.execute('SELECT * FROM student WHERE id=%d',addid)
        row = SQL.cursor.fetchall()
        if row!=[]:
            return "您输入的学号已存在"
        else:
            addname = request.form.get('addname')
            adddepartment = request.form.get('adddepartment')
            if addname != None and adddepartment and addid != None:            #不为空则添加
                SQL.cursor.execute('INSERT INTO student VALUES (%d, %s, %s)',(addid,addname,adddepartment))
                SQL.conn.commit()
                return redirect(url_for('index'))
    return render_template('addstu.html')                     #添加成功则重定向到首页

@app.route('/updatestu',methods=['GET','POST'])                  #这里是修改模块，先要找ggg到要修改的学号，如果找到了进行操作
def updatestu():
    if request.method=='POST':
        updateid = request.form.get('updateid')
        updatedep = request.form.get('updatedepartment')
        updatename = request.form.get('updatename')
        SQL.cursor.execute('SELECT * FROM student WHERE id=%d', updateid)
        row = SQL.cursor.fetchall()
        if row==[]:
            return '您输入的学号不存在'
        else:
                if updatedep !='':                              #这里的一对单引号里什么都没有，表示如果输入框里为空，不进行修改
                    SQL.cursor.execute('UPDATE  student SET name=%s WHERE id=%d ', updatename,updateid)
                    SQL.conn.commit()
                if updatename!='':
                    SQL.cursor.execute('UPDATE  student SET department=%s WHERE id=%d ', updatedep,updateid)
                    SQL.conn.commit()
                return render_template('index.html')


    return render_template('updatestu.html')

@app.route('/searchstu',methods=['GET','POST'])
def searchstu():
    if request.method=='POST':
        id = request.form.get('id')
        SQL.cursor.execute('SELECT * FROM student WHERE id=%d', id)
        row = SQL.cursor.fetchall()
        if row==[]:
            return '没有您要找的学号'
        else:
            find=row
            return render_template('searchstu.html',find=find)      #如果找到了学号，把该学生信息传给html
    return render_template('searchstu.html')

if __name__ == '__main__':
    app.run(debug=True)
