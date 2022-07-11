import pymysql
import numpy
import toolfun
# # import pyhdfs
# # fs = pyhdfs.connect("10.10.0.180", 9000)
# # content=pyhdfs.get(fs, "/user/hadoop/icdata/shuka201812.csv")
# # print(content)
#
# from hdfs.client import Client
#
# client = Client("http://10.10.0.180:9000")
#
# lines = []
# with client.read("/user/hadoop/icdata/shuka201812.csv", encoding='utf-8') as reader:
#     print(reader)
#     for line in reader:
#         lines.append(line.strip())

db = pymysql.connect("localhost", "root", "renshuaichen", "firstdatabase")
cursor=db.cursor()
sql="select 始发站名称 from 行车计划201812 where 线路名称='34路'"
cursor.execute(sql)
f_stop=cursor.fetchone()
print(f_stop[0])
sql="select * from 到离站201812 where 线路名称='34路'and 到站时间 like '2018/12/1 7:0%' and 站点名称='"+f_stop[0]+"'and 进出站='2'"
sql = "select * from 到离站201812 where 趟次ID='150048981' and 进出站='2' and 站点名称='福园街'"
cursor.execute(sql)
data=cursor.fetchall()
print(data)
if data[0]==data[1]
# data=list(data)
# data=numpy.unique(data)


