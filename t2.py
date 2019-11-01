import pymysql
import  toolfun
from datetime import datetime
db = pymysql.connect("localhost", "root", "renshuaichen", "firstdatabase")
cursor = db.cursor()
route1="81路"
i=0
# # sql="select 排班时间 from 行车计划201812 where 线路名称='81路' and 排班时间 like '2018-12-02%'"
# sql="select * from 趟次201812 where 趟次ID='149959264' and 线路ID='2576' and 线路名称='34路'"
# cursor.execute(sql)
# data=cursor.fetchall()
# print(data)
# sql="select * from 到离站201812 where 趟次ID='149959264' and 线路ID='2576' and 线路名称='34路' and 进出站='2'"
# cursor.execute(sql)
# data=cursor.fetchall()
# for stop in data:
#     print(stop)
#     i=i+1
# print(i)
# # bustime=[]
# # stop=""
# # for ele in data:
# #     stop=ele[0]
# #     bustime.append(stop.split(' ')[1])
# # bustime.sort(key=lambda date: datetime.strptime(date, '%H:%M:%S'))
# # print(bustime)

sql = "select * from 到离站201812 where 趟次ID='149959264' and 线路ID='2576' and 线路名称='34路' and 进出站='2'"
cursor.execute(sql)
data = cursor.fetchall()
print(data)
time_a, sta_a = toolfun.by_time(data)
print(sta_a)
