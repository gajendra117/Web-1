import pymysql
from flask import Flask, request, render_template,send_from_directory,url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)





def insert(user ,idea):
    db=pymysql.connect("localhost","root","root","test3")
    cursor=db.cursor()
    sql="insert into dosomething (user,idea) values ('{}','{}')".format(user,idea)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def getfile():
    path1='/data/app/flask_file_share_app/Web/share-file-server/flask-server/uploadfile'
    path2='/data/app/flask_file_share_app/Web/share-file-server/flask-server'
    os.chdir(path1)
    flist=os.listdir()
    os.chdir(path2)
    return flist

def isHavefile(filename):
    path1='/data/app/flask_file_share_app/Web/share-file-server/flask-server/uploadfile'
    path2='/data/app/flask_file_share_app/Web/share-file-server/flask-server'
    os.chdir(path1)
    flag=os.path.isfile(filename)
    os.chdir(path2)
    return flag

@app.route('/uploadfile', methods=['POST','get'])
def upload():
    if request.method=='GET':
        return '<h3>get 222 </h3>'
    if request.method=='POST':
        relativepath='./uploadfile/'
        upfilename=request.form['upfilename']
        f=request.files['file']
        fname=secure_filename(f.filename)
        f.save(os.path.join(relativepath,fname))
        print(upfilename)
        print(fname)
        return '<p> port yesh</p>'

#显示上传页面 同时也是主页面
@app.route('/up', methods=['POST','get'])
def up():
    mycss=url_for('static', filename='style.css')
    return render_template('upload.html',mycss=mycss)


@app.route('/file', methods=['POST','get'])
def file():
    mycss=url_for('static', filename='style.css')
    return render_template('upload.html',mycss=mycss)

#main页面
@app.route('/')
def hello():
    return '<p> port 5002</p>'

#显示下载文件的界面
@app.route('/down', methods=['GET'])
def downloadpage():
    mycss=url_for('static', filename='style.css')
    flist=getfile()
    return render_template('downloadpage.html',mycss=mycss,fl=flist)


#下载要下载的文件，要下载的文件是通过get方法来传递的
@app.route('/downloadfile', methods=['GET'])
def downloadfile():
    if request.method=='GET':
        downloadfilename=request.args.get('filename')
        flist=getfile()
        print ()
        if isHavefile(downloadfilename):
            return send_from_directory('uploadfile',downloadfilename,as_attachment=True)
        else:
            abort(404)

if __name__ == '__main__':
    app.run(debug=True,port=5002)
