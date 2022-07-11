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

#------------------------------------------第一次的测试----------------------------
# @app.route('/',methods=['GET','POST'])
# def update_page():
#     err="请填写条件"
#     data="数据为空"
#     bustime_p = []
#     bustime_f = []
#     turn=[]
#     if request.method=='POST':
#         input1 = request.form.get('input1')
#         input2 = request.form.get('input2')
#         if not all([input1,input2]):
#             err='消息不完整'
#         elif input1=='2'and input2=='1':
#             sql = "select * from 到离站201812 where 趟次ID='149959264' and 线路ID='2576' and 线路名称='34路' and 进出站='2'"
#             cursor.execute(sql)
#             data=cursor.fetchall()
#             time_a,sta_a=toolfun.by_time(data)
#             print(time_a)
#             return render_template("index.html",time_a=json.dumps(time_a),sta_a=json.dumps(sta_a))
#         else:
#             err=""
#             sql = "select 排班时间 from 行车计划201812 where 线路名称='81路' and 排班时间 like '2018-12-02%'"
#             cursor.execute(sql)
#             data=cursor.fetchall()
#             bustime_p=toolfun.get_time_plan(data)
#             turn=toolfun.turn(data)
#             print(data)
#             sql="select 运营日期 from 趟次201812 where 线路名称='81路' and 运营日期 like '2018/12/2 %'"
#             cursor.execute(sql)
#             data = cursor.fetchall()
#             print(data)
#             bustime_f=toolfun.get_time(data)
#             print(bustime_f)
#             # return render_template('index.html',err=json.dumps(err),bustime_f=json.dumps(bustime_f),bustime_p=json.dumps(bustime_p),turn=json.dumps(turn))
#     # return render_template('index.html')
#     # sql = "select * from 趟次201811"
#     # cursor.execute(sql)
#     # data = cursor.fetchall()
#     # jsonify(data)
#     return render_template('on-schedule.html', err=json.dumps(err), bustime_f=json.dumps(bustime_f),
#                            bustime_p=json.dumps(bustime_p), turn=json.dumps(turn))
#     # return render_template('index.html', err=json.dumps(err))
#---------------------------------------------------------------------------------------------

#----------------------------测试2-----------------------------------------
@app.route('/',methods=['GET','POST'])
def update_page():
    err="请填写条件"
    data="数据为空"
    bustime_p = []
    bustime_f = []
    turn=[]
    if request.method=='POST':
        select1 = request.values.get('s1')
        select2 = request.values.get('s2')
        if select1=='0000-00-00' and select2=='0000-00-00':
            err='消息不完整'
        else:
            err=""
            sql = "select 排班时间 from 行车计划201812 where 线路名称='"+select1+"' and 排班时间 like '"+select2+"%'"
            cursor.execute(sql)
            data=cursor.fetchall()
            bustime_p=toolfun.get_time_plan(data)
            turn=toolfun.turn(data)
            print(data)
            sql="select 运营日期 from 趟次201812 where 线路名称='"+select1+"' and 运营日期 like '"+toolfun.change_data_from(select2)+" %'"
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
    return render_template('on-schedule.html', err=json.dumps(err), bustime_f=json.dumps(bustime_f),
                           bustime_p=json.dumps(bustime_p), turn=json.dumps(turn))
    # return render_template('index.html', err=json.dumps(err))
#----------------------------------------------------------------------------




# @app.route('/',methods=['GET','POST'])
# def update_page():
#     err="请填写条件"
#     data="数据为空"
#     bustime_p = []
#     bustime_f = []
#     turn=[]
#     print('1')
#     if request.method=='POST':
#         select1 = request.values.get('s1')
#         select2 = request.values.get('s2')
#         print(select1)
#         print(select2)
#         if select1=='0000-00-00' and select2=='0000-00-00':
#             err='消息不完整'
#         else:
#             err=""
#             sql = "select 排班时间 from 行车计划201812 where 线路名称='"+str(select2)+"' and 排班时间 like '"+str(select1)+"%'"
#             cursor.execute(sql)
#             data=cursor.fetchall()
#             bustime_p=toolfun.get_time_plan(data)
#             turn=toolfun.turn(data)
#             print(data)
#             sql="select 运营日期 from 趟次201812 where 线路名称='"+str(select1)+"' and 运营日期 like '2018/12/2 %'"
#             cursor.execute(sql)
#             data = cursor.fetchall()
#             print(data)
#             bustime_f=toolfun.get_time(data)
#             print(bustime_f)
#     return render_template('on-schedule.html',err=json.dumps(err), bustime_f=json.dumps(bustime_f),bustime_p=json.dumps(bustime_p), turn=json.dumps(turn))


@app.route('/t_point',methods=['GET','POST'])
def t_point():
    err="请填写条件"
    data="数据为空"
    time_a_1 = []
    time_a_2 = []
    time_a_3 = []
    sta_a = []
    turn=[]
    if request.method=='POST':
        select1 = request.values.get('s1')
        select2 = request.values.get('s2')
        if select1 == '0000-00-00' and select2 == '0000-00-00':
            err='消息不完整'
        else:

            sql = "select 始发站名称 from 行车计划201812 where 线路名称='"+select1+"'"
            cursor.execute(sql)
            f_stop = cursor.fetchone()
            print(f_stop[0])
            sql="select 趟次ID from 到离站201812 where 线路名称='"+select1+"'and 到站时间 like '"+toolfun.change_data_from(select2)+" 7:0%' and 进出站='2' and 站点名称='"+f_stop[0]+"'"
            # sql = "select * from 到离站201812 where 趟次ID='149959264' and 线路ID='2576' and 线路名称='34路' and 进出站='2'"
            cursor.execute(sql)
            trip_1=cursor.fetchone()
            print(trip_1[0])
            # sql="select 趟次ID from 到离站201812 where 线路名称='"+select1+"'and 到站时间 like '"+toolfun.change_data_from(select2)+" 12:0%' and 进出站='2' and 站点名称='"+f_stop[0]+"'"
            # cursor.execute(sql)
            # trip_2 = cursor.fetchone()
            #
            # sql = "select 趟次ID from 到离站201812 where 线路名称='" + select1 + "'and 到站时间 like '" + toolfun.change_data_from(select2) + " 18:0%' and 进出站='2' and 站点名称='" +f_stop[0] + "'"
            # cursor.execute(sql)
            # trip_3 = cursor.fetchone()
            sql = "select * from 到离站201812 where 趟次ID='"+trip_1[0]+"' and 进出站='2'"
            cursor.execute(sql)
            data_1 = cursor.fetchall()
            time_a_1,sta_a = toolfun.by_time(data_1)
            # sql = "select * from 到离站201812 where 趟次ID='"+trip_2[0]+"'"
            # cursor.execute(sql)
            # data_2 = cursor.fetchone()
            # time_a_2,sta_a = toolfun.by_time(data_2)
            # sql = "select * from 到离站201812 where 趟次ID='"+trip_3[0]+"'"
            # cursor.execute(sql)
            # data_3 = cursor.fetchone()
            # time_a_3,sta_a = toolfun.by_time(data_3)
    return render_template("t_point.html", time_a_1=json.dumps(time_a_1), sta_a=json.dumps(sta_a), time_a_2=json.dumps(time_a_2), time_a_3=json.dumps(time_a_3))
    # return render_template('t_point.html', err=json.dumps(err), bustime_f=json.dumps(bustime_f),
    #                        bustime_p=json.dumps(bustime_p), turn=json.dumps(turn))
    # return render_template('index.html', err=json.dumps(err))






@app.route('/page_one',methods=['GET','POST'])
def page_one():
    return render_template('站点客流.html')

@app.route('/page_two',methods=['GET','POST'])
def page_two():
    num,name=toolfun.sta_co_data()
    return render_template('客流柱状图.html',num=json.dumps(num),name=json.dumps(name))

if __name__ == '__main__':
     app.run()
