import pymysql
from flask import Flask, request, render_template,send_from_directory
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
    path1='/home/zhaozheng/code/python/python web/uploadfile'
    path2='/home/zhaozheng/code/python/python web'
    os.chdir(path1)
    flist=os.listdir()
    os.chdir(path2)
    return flist

def isHavefile(filename):
    path1='/home/zhaozheng/code/python/python web/uploadfile'
    path2='/home/zhaozheng/code/python/python web'
    os.chdir(path1)
    flag=os.path.isfile(filename)
    os.chdir(path2)
    return flag





@app.route('/dosomething', methods=['POST'])
def dosomething():
    user=request.form['user']
    something = request.form['dosomething']
    insert(user,something)
    return render_template('1.html')


@app.route('/upload', methods=['POST','get'])
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
        return render_template('1.html')

@app.route('/testdown', methods=['GET'])
def testdown():
    if request.method=='GET':
        #if os.path.isfile(filename):
        filename='read.txt'
        return send_from_directory('uploadfile',filename,as_attachment=True)
    else:
        abort(404)

@app.route('/downloadpage', methods=['GET'])
def downloadpage():
    if request.method=='GET':
        flist=getfile()
        print (flist)
        return render_template('downloadpage.html',fl=flist)

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
    app.run(host='0.0.0.0')