from datetime import datetime
import pymysql
import pandas as pd
import math

def del_rep(data):
    return 0




def get_time_plan(data):
    bustime = []
    stop = ""
    addstr = ":00"
    for ele in data:
        stop = ele[0]
        bustime.append(stop + addstr)
    bustime = sorted(bustime)
    return bustime


def get_time(data):
    bustime = []
    addstr = "2018-12-02 "
    stop = ""
    for ele in data:
        stop = ele[0]
        stop = stop.split(' ')[1]
        stop = stop.split(':')[0] + ":" + stop.split(':')[1]
        bustime.append(addstr + stop)
        bustime.sort(key=lambda date: datetime.strptime(date, '%Y-%m-%d %H:%M'))
    return bustime


def turn(data):
    turn = []
    i = 1
    for ele in data:
        turn.append("第" + str(i) + "班次")
        i = i + 1
    return turn


def by_time(data):
    timet = []
    sta = []
    for ele in data:
        print(ele[7])
        timet.append(ele[7])
    timet.sort(key=lambda date: datetime.strptime(date, '%Y/%m/%d %H:%M:%S'))
    for ti in timet:
        for ele in data:
            if ele[7] == ti:
                sta.append(ele[4])
    return timet, sta


def sta_co_data():
    db = pymysql.connect("localhost", "root", "renshuaichen", "firstdatabase")
    cursor = db.cursor()
    final_num=[]
    final_num_new=[]
    final_id_new=[]
    p_pdata = pd.read_csv("../static/data/station_flow.csv")
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


    for i in final_data[1]:
        final_num.append(i)
    final_num.sort(reverse=True)
    final_num=list(final_num)
    final_num.remove(10019)
    final_num.remove(7625)
    final_num.remove(4718)

    for i in range(10):
        final_num_new.append(final_num[i])

    for i in final_num_new:
        for j in range(len(final_data[0])):
            if i==final_data[1][j]:
                final_id_new.append(final_data[0][j])
    print(final_id_new)
    final_name_new=[]
    for i in final_id_new:
        sql="select 站点名称 from 13路站点 where 站点ID='"+i+"'"
        cursor.execute(sql)
        j = cursor.fetchall()
        final_name_new.append(j[0][0])
    print(final_name_new)
    print(final_num_new)
    return final_num_new,final_name_new

def change_data_from(date):
    date=date.replace('-','/')
    date=date.replace('/0','/')
    return date


    
    
    
    
    #
    # final_list = []
    # file = open('站点客流2.txt', 'w+', encoding='UTF-8')
    # file.write("[")
    # for i in range(len(final_data[0])):
    #     sql = "select * from 13路站点 where 线路名称='13路' and 站点ID='" + str(final_data[0][i]) + "'"
    #     cursor.execute(sql)
    #     one_d = cursor.fetchall()
    #     if one_d != ():
    #         one_d = one_d[0]
    #         one_d = list(one_d)
    #         # dict={
    #         #     "weidu":one_d[8],
    #         #     "jingdu":one_d[7],
    #         #     "stopName":one_d[1]
    #         # }
    #         # final_list.append(dict)
    #         file.write(
    #             "{\"weidu\":" + one_d[8] + ",\"jingdu\":" + one_d[7] + ",\"stopName\":\"" + one_d[
    #                 1] + "\",\"ss\":" + str(
    #                 final_data[1][i]) + ",\"sl\":0" + "},")
    #
    # for i in range(len(final_data[0])):
    #     sql = "select * from 13路站点 where 线路名称='16路' and 站点ID='" + str(final_data[0][i]) + "'"
    #     cursor.execute(sql)
    #     one_d = cursor.fetchall()
    #     if one_d != ():
    #         one_d = one_d[0]
    #         one_d = list(one_d)
    #         # dict={
    #         #     "weidu":one_d[8],
    #         #     "jingdu":one_d[7],
    #         #     "stopName":one_d[1]
    #         # }
    #         # final_list.append(dict)
    #         file.write("{\"weidu\":" + one_d[8] + ",\"jingdu\":" + one_d[7] + ",\"stopName\":\"" + one_d[
    #             1] + "\",\"ss\":0" + ",\"sl\":" + str(final_data[1][i]) + "},")
    # file.write("]")
    # print(final_list)

if __name__ == "__main__":
    sta_co_data()