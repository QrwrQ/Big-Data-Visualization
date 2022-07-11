import pymysql
import math
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


# import pandas as pd
# # data = pd.read_csv("static/data/station_flow.csv")
# # data3=data.columns
# # lll=data3.values
# # ll=list(lll)
# # ll.remove('time')
# # print(ll)
# # for ele in ll:
# #     print(ele)
# #     sql = "select 站点名称 from 到离站201812 where 站点ID='%s'"
# #     cursor.execute(sql%(str(ele)))
# #     getdata = cursor.fetchall()
# #     print(getdata)
# #
# # final=[[],[]]
# # data1=data['21834']
# # data2=data['time']
# # fi1=data1.values.tolist()
# # fi2=data2.values.tolist()

# sql="select 站点名称 from 到离站201812 where 站点ID=''"
# cursor.execute(sql)
# data=cursor.fetchall()
# for i in fi1:
#     final[1].append(i)
# for i in fi2:
#     final[0].append(i)
# print(final)







# import math
# def gcj02_To_Bd09(gg_lon,gg_lat):
#     pi = 3.141592653589793 * 3000.0 / 180.0;
#     x = gg_lon;
#     y = gg_lat;
#     z = math.sqrt(x * x + y * y) + 0.00002* math.sin(y * pi);
#     theta = math.atan2(y, x) + 0.000003 * math.cos(x * pi);
#     bd_lon = z * math.cos(theta) + 0.0065;
#     bd_lat = z * math.sin(theta) + 0.006;
#     return bd_lon, bd_lat;
#
# def bd09_To_Gcj02(bd_lon,bd_lat):
#     pi = 3.141592653589793 * 3000.0 / 180.0;
#     x = bd_lon - 0.0065;
#     y = bd_lat - 0.006;
#     z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * pi);
#     theta = math.atan2(y, x) - 0.000003 * math.cos(x * pi);
#     gg_lon = z * math.cos(theta);
#     gg_lat = z * math.sin(theta);
#     return gg_lon, gg_lat;
# data=bd09_To_Gcj02(118.4677120,32.0250170);
# print(data);


date='2018-12-02'
date=date.replace('-','/')
date=date.replace('/0','/')
print(date)