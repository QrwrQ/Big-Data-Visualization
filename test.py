import pymysql

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
sql="select * from 趟次201811"
cursor.execute(sql)
data=cursor.fetchall()
for row in data:
    if row[3]== '16路':
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])
        print(row[7])
        print(row[8])
        print(row[9])
        print(row[10])
        print(row[11])
        input("aa")




<script type="text/javascript">
                                            function table1()
                                            {
                                                // 基于准备好的dom，初始化echarts实例
                                                var myChart = echarts.init(document.getElementById('table'), 'chalk');
                                                option = {
                                                    title: {
                                                        text: '折线图堆叠'
                                                    },
                                                    tooltip: {
                                                        trigger: 'axis'
                                                    },
                                                    legend: {
                                                        data: ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎']
                                                    },
                                                    grid: {
                                                        left: '3%',
                                                        right: '4%',
                                                        bottom: '3%',
                                                        containLabel: true
                                                    },
                                                    toolbox: {
                                                        feature: {
                                                            saveAsImage: {}
                                                        }
                                                    },
                                                    xAxis: {
                                                        type: 'category',
                                                        boundaryGap: false,
                                                        data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                                                    },
                                                    yAxis: {
                                                        type: 'value'
                                                    },
                                                    series: [{
                                                        name: '邮件营销',
                                                        type: 'line',
                                                        stack: '总量',
                                                        data: [120, 132, 101, 134, 90, 230, 210],
                                                        color: "#F58080",
                                                        lineStyle: {
                                                            normal: {
                                                                width: 5,
                                                                color: {
                                                                    type: 'linear',

                                                                    colorStops: [{
                                                                        offset: 0,
                                                                        color: '#FFCAD4' // 0% 处的颜色
                                                                    }, {
                                                                        offset: 0.4,
                                                                        color: '#F58080' // 100% 处的颜色
                                                                    }, {
                                                                        offset: 1,
                                                                        color: '#F58080' // 100% 处的颜色
                                                                    }],
                                                                    globalCoord: false // 缺省为 false
                                                                },
                                                                shadowColor: 'rgba(245,128,128, 0.5)',
                                                                shadowBlur: 10,
                                                                shadowOffsetY: 7
                                                            }
                                                        },
                                                        itemStyle: {
                                                            normal: {
                                                                color: '#F58080',
                                                                borderWidth: 10,
                                                                /*shadowColor: 'rgba(72,216,191, 0.3)',
                                                                 shadowBlur: 100,*/
                                                                borderColor: "#F58080"
                                                            }
                                                        },
                                                        smooth: true
                                                    },
                                                        {
                                                            name: '联盟广告',
                                                            type: 'line',
                                                            stack: '总量',
                                                            data: [220, 182, 191, 234, 290, 330, 310],
                                                            lineStyle: {
                                                                normal: {
                                                                    width: 5,
                                                                    color: {
                                                                        type: 'linear',

                                                                        colorStops: [{
                                                                            offset: 0,
                                                                            color: '#AAF487' // 0% 处的颜色
                                                                        },
                                                                            {
                                                                                offset: 0.4,
                                                                                color: '#47D8BE' // 100% 处的颜色
                                                                            }, {
                                                                                offset: 1,
                                                                                color: '#47D8BE' // 100% 处的颜色
                                                                            }
                                                                        ],
                                                                        globalCoord: false // 缺省为 false
                                                                    },
                                                                    shadowColor: 'rgba(71,216,190, 0.5)',
                                                                    shadowBlur: 10,
                                                                    shadowOffsetY: 7
                                                                }
                                                            },
                                                            itemStyle: {
                                                                normal: {
                                                                    color: '#AAF487',
                                                                    borderWidth: 10,
                                                                    /*shadowColor: 'rgba(72,216,191, 0.3)',
                                                                     shadowBlur: 100,*/
                                                                    borderColor: "#AAF487"
                                                                }
                                                            },
                                                            smooth: true
                                                        },
                                                        {
                                                            name: '视频广告',
                                                            type: 'line',
                                                            stack: '总量',
                                                            data: [150, 232, 201, 154, 190, 330, 410],
                                                            lineStyle: {
                                                                normal: {
                                                                    width: 5,
                                                                    color: {
                                                                        type: 'linear',

                                                                        colorStops: [{
                                                                            offset: 0,
                                                                            color: '#F6D06F' // 0% 处的颜色
                                                                        },
                                                                            {
                                                                                offset: 0.4,
                                                                                color: '#F9A589' // 100% 处的颜色
                                                                            }, {
                                                                                offset: 1,
                                                                                color: '#F9A589' // 100% 处的颜色
                                                                            }
                                                                        ],
                                                                        globalCoord: false // 缺省为 false
                                                                    },
                                                                    shadowColor: 'rgba(249,165,137, 0.5)',
                                                                    shadowBlur: 10,
                                                                    shadowOffsetY: 7
                                                                }
                                                            },
                                                            itemStyle: {
                                                                normal: {
                                                                    color: '#F6D06F',
                                                                    borderWidth: 10,
                                                                    /*shadowColor: 'rgba(72,216,191, 0.3)',
                                                                     shadowBlur: 100,*/
                                                                    borderColor: "#F6D06F"
                                                                }
                                                            },
                                                            smooth: true

                                                        },
                                                        {
                                                            name: '直接访问',
                                                            type: 'line',
                                                            stack: '总量',
                                                            data: [320, 332, 301, 334, 390, 330, 320],
                                                            lineStyle: {
                                                                normal: {
                                                                    width: 5,
                                                                    color: {
                                                                        type: 'linear',

                                                                        colorStops: [{
                                                                            offset: 0,
                                                                            color: '#9932CC' // 0% 处的颜色
                                                                        }, {
                                                                            offset: 1,
                                                                            color: '#48D8BF' // 100% 处的颜色
                                                                        }],
                                                                        globalCoord: false // 缺省为 false
                                                                    },
                                                                    shadowColor: 'rgba(72,216,191, 0.3)',
                                                                    shadowBlur: 10,
                                                                    shadowOffsetY: 20
                                                                }
                                                            },
                                                            itemStyle: {
                                                                normal: {
                                                                    color: '#fff',
                                                                    borderWidth: 10,
                                                                    /*shadowColor: 'rgba(72,216,191, 0.3)',
                                                                    shadowBlur: 100,*/
                                                                    borderColor: "#A9F387"
                                                                }
                                                            },
                                                            smooth: true
                                                        },
                                                        {
                                                            name: '搜索引擎',
                                                            type: 'line',
                                                            stack: '总量',
                                                            data: [820, 932, 901, 934, 1290, 1330, 1320],
                                                            lineStyle: {
                                                                normal: {
                                                                    width: 5,
                                                                    color: {
                                                                        type: 'linear',

                                                                        colorStops: [{
                                                                            offset: 0,
                                                                            color: '#EEEE00' // 0% 处的颜色
                                                                        }, {
                                                                            offset: 1,
                                                                            color: '#FF7F00' // 100% 处的颜色
                                                                        }],
                                                                        globalCoord: false // 缺省为 false
                                                                    },
                                                                    shadowColor: 'rgba(255,255,0, 0.3)',
                                                                    shadowBlur: 10,
                                                                    shadowOffsetY: 20
                                                                }
                                                            },
                                                            itemStyle: {
                                                                normal: {
                                                                    color: '#fff',
                                                                    borderWidth: 10,
                                                                    /*shadowColor: 'rgba(72,216,191, 0.3)',
                                                                    shadowBlur: 100,*/
                                                                    borderColor: "#A9F387"
                                                                }
                                                            },
                                                            smooth: true
                                                        }
                                                    ]
                                                };


                                                // 使用刚指定的配置项和数据显示图表。
                                                myChart.setOption(option);
                                            }
                                        </script>

{ %
for message in get_flashed_messages() %}
{{message}}
{ % endfor %}


<script>
                            function error() {
                                err = eval('{{ err|safe }}');
                                if (err != "") {
                                    alert(err);
                                }

                            }
                        </script>



function table1() {
                                                err = eval('{{ err|safe }}');
                                                if (err!=""){
                                                    alert(err);
                                                }
                                                if(err=="") {
                                                    busdata = eval('{{ result|safe }}');
                                                // 基于准备好的dom，初始化echarts实例
                                                var myChart = echarts.init(document.getElementById('table'), 'chalk');
                                                option = {
                                                    backgroundColor: '#001120',
                                                    tooltip: {
                                                        trigger: 'axis',
                                                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                                            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                                                        }
                                                    },
                                                    legend: {
                                                        data: ['邮件营销', '联盟广告'],
                                                        textStyle: {
                                                            color: 'rgba(55,255,249,1)'
                                                        }
                                                    },
                                                    grid: {
                                                        left: '3%',
                                                        right: '4%',
                                                        bottom: '3%',
                                                        containLabel: true
                                                    },
                                                    xAxis: [
                                                        {
                                                            type: 'category',
                                                            data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
                                                            splitLine: {
                                                                show: false
                                                            },
                                                            axisLine: {
                                                                lineStyle: {
                                                                    color: 'rgba(55,255,249,1)',
                                                                }
                                                            },
                                                            axisLabel: {
                                                                color: 'rgba(55,255,249,1)'
                                                            }
                                                        }
                                                    ],
                                                    yAxis: [
                                                        {
                                                            type: 'value',
                                                            splitLine: {
                                                                show: false
                                                            },
                                                            axisLine: {
                                                                lineStyle: {
                                                                    color: 'rgba(55,255,249,1)',
                                                                }
                                                            }
                                                        }
                                                    ],
                                                    series: [
                                                        {
                                                            name: '邮件营销',
                                                            type: 'bar',
                                                            barWidth: 20,
                                                            itemStyle: {
                                                                barBorderRadius: 20,
                                                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                                                    offset: 0,
                                                                    color: "rgba(55,255,249,1)"
                                                                },
                                                                    {
                                                                        offset: 1,
                                                                        color: "rgba(0,222,215,0.2)"
                                                                    }
                                                                ])
                                                            },
                                                            data: [120, 132, 101, 134, 90, 230, 210]
                                                        },
                                                        {  // 替代柱状图 默认不显示颜色，是最下方柱图（邮件营销）的value值 - 20
                                                            type: 'bar',
                                                            barWidth: 20,
                                                            barGap: '-100%',
                                                            stack: '广告',
                                                            itemStyle: {
                                                                color: 'transparent'
                                                            },
                                                            data: [100, 102, 81, 114, 70, 210, 190]
                                                        },
                                                        {
                                                            name: '联盟广告',
                                                            type: 'bar',
                                                            barWidth: 20,
                                                            barGap: '-100%',
                                                            stack: '广告',
                                                            itemStyle: {
                                                                barBorderRadius: 20,
                                                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                                                    offset: 0.4,
                                                                    color: "rgba(255,252,0,1)"
                                                                },
                                                                    {
                                                                        offset: 1,
                                                                        color: "rgba(8,228,222,0.2)"
                                                                    }
                                                                ])
                                                            },
                                                            data: [220, 182, 191, 234, 290, 330, 310]
                                                        }

                                                    ]
                                                };

                                                myChart.setOption(option);
                                                }
                                            }