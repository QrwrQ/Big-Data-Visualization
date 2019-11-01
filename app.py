import sqlalchemy
from flask import Flask, request, render_template,flash
import pymysql
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
import toolfun

app = Flask(__name__)

db = pymysql.connect("localhost", "root", "renshuaichen", "firstdatabase")
cursor = db.cursor()
app.secret_key='aaa'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:renshuaichen@127.0.0.1/firstdatabase'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS ']=False
# db1=SQLAlchemy(app)


# @app.route('/')
# def get_data():
#     db = pymysql.connect("localhost", "root", "renshuaichen", "firstdatabase")
#     cursor=db.cursor()
#     sql="select * from 1table"
#     print(cursor.execute(sql))
# @app.route('/getdata')
# def get_data():
#     sql = "select * from 趟次201811"
#     cursor.execute(sql)
#     data = cursor.fetchall()
#     jsonify(data)


@app.route('/',methods=['GET','POST'])
def update_page():
    err="请填写条件"
    data="数据为空"
    bustime_p = []
    bustime_f = []
    turn=[]
    if request.method=='POST':
        input1 = request.form.get('input1')
        input2 = request.form.get('input2')
        if not all([input1,input2]):
            err='消息不完整'
        elif input1=='2'and input2=='1':
            sql = "select * from 到离站201812 where 趟次ID='149959264' and 线路ID='2576' and 线路名称='34路' and 进出站='2'"
            cursor.execute(sql)
            data=cursor.fetchall()
            time_a,sta_a=toolfun.by_time(data)
            print(time_a)
            return render_template("index.html",time_a=json.dumps(time_a),sta_a=json.dumps(sta_a))
        else:
            err=""
            sql = "select 排班时间 from 行车计划201812 where 线路名称='81路' and 排班时间 like '2018-12-02%'"
            cursor.execute(sql)
            data=cursor.fetchall()
            bustime_p=toolfun.get_time_plan(data)
            turn=toolfun.turn(data)
            print(data)
            sql="select 运营日期 from 趟次201812 where 线路名称='81路' and 运营日期 like '2018/12/2 %'"
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            bustime_f=toolfun.get_time(data)
            print(bustime_f)
            # return render_template('index.html',err=json.dumps(err),bustime_f=json.dumps(bustime_f),bustime_p=json.dumps(bustime_p),turn=json.dumps(turn))
    # return render_template('index.html')
    # sql = "select * from 趟次201811"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # jsonify(data)
    return render_template('index.html', err=json.dumps(err), bustime_f=json.dumps(bustime_f),
                           bustime_p=json.dumps(bustime_p), turn=json.dumps(turn))
    # return render_template('index.html', err=json.dumps(err))



if __name__ == '__main__':
     app.run()
