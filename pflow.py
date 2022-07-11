import pymysql
import pandas as pd
import math
import toolfun
from datetime import datetime

db = pymysql.connect("localhost", "root", "renshuaichen", "firstdatabase")
cursor = db.cursor()
p_pdata = pd.read_csv("static/data/station_flow.csv")
sta_ID = p_pdata.columns
sta_ID = sta_ID.values
sta_ID = list(sta_ID)
sta_ID.remove('time')
final_data = [[], []]
# print(sta_ID)
for i in sta_ID:
    all = 0
    order = 0
    final_data[0].append(i)
    line_data = p_pdata[str(i)]
    line_data = line_data.values
    line_data = list(line_data)
    # print(line_data)
    for j in line_data:
        if order > 143:
            break
        order = order + 1
        all = all + j
    final_data[1].append(all)
# print(final_data[0][0],final_data[1][0])
final_list = []
file = open('站点客流2.txt', 'w+', encoding='UTF-8')
file.write("[")
for i in range(len(final_data[0])):
    sql = "select * from 13路站点 where 线路名称='13路' and 站点ID='" + str(final_data[0][i]) + "'"
    cursor.execute(sql)
    one_d = cursor.fetchall()
    if one_d != ():
        one_d = one_d[0]
        one_d = list(one_d)
        # dict={
        #     "weidu":one_d[8],
        #     "jingdu":one_d[7],
        #     "stopName":one_d[1]
        # }
        # final_list.append(dict)
        file.write(
            "{\"weidu\":" + one_d[8] + ",\"jingdu\":" + one_d[7] + ",\"stopName\":\"" + one_d[1] + "\",\"ss\":" + str(
                final_data[1][i]) + ",\"sl\":0" + "},")

for i in range(len(final_data[0])):
    sql = "select * from 13路站点 where 线路名称='16路' and 站点ID='" + str(final_data[0][i]) + "'"
    cursor.execute(sql)
    one_d = cursor.fetchall()
    if one_d != ():
        one_d = one_d[0]
        one_d = list(one_d)
        # dict={
        #     "weidu":one_d[8],
        #     "jingdu":one_d[7],
        #     "stopName":one_d[1]
        # }
        # final_list.append(dict)
        file.write("{\"weidu\":" + one_d[8] + ",\"jingdu\":" + one_d[7] + ",\"stopName\":\"" + one_d[
            1] + "\",\"ss\":0" + ",\"sl\":" + str(final_data[1][i]) + "},")
file.write("]")
print(final_list)
