# -*- coding: utf-8 -*-
# @Author: 李超权
# @Date: 2024/6/14

import random
import pymysql
from pyecharts.charts import Bar, Pie, Line, Geo, WordCloud, Map
from pyecharts import options as opts
import matplotlib.pyplot as plt
import pandas as pd
from pyecharts.globals import ThemeType, ChartType, SymbolType

plt.rcParams['font.sans-serif'] = ['SimHei']  ##中文乱码问题！
plt.rcParams['axes.unicode_minus'] = False  # 横坐标负号显示问题！


# 函数用于计算薪资范围的中值
def parse_salary_range(salary_range):
    low, high = map(int, salary_range.replace('k', '').split('-'))
    return (low + high) / 2 * 1000  # 转换为元


# 函数用于过滤薪资范围
def filter_salaries_by_lowpoint(experience, salary_ranges, low_threshold):
    filtered_ranges = []
    for salary_range in salary_ranges:
        midpoint = parse_salary_range(salary_range)
        if midpoint >= low_threshold:
            filtered_ranges.append(salary_range)
    return filtered_ranges


def filter_salaries_by_highpoint(experience, salary_ranges, high_threshold):
    filtered_ranges = []
    for salary_range in salary_ranges:
        count = parse_salary_range(salary_range)
        if count <= high_threshold:
            filtered_ranges.append(salary_range)
    return filtered_ranges


# 打印所有title
# ------------------------城市条形图---------------------
def bar_base():
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='lagou')
    # 渲染图表为HTML文件
    cursor = conn.cursor()
    sql_city = "SELECT address, COUNT(*) as count FROM positions GROUP BY address ORDER BY count DESC"
    cursor.execute(sql_city)
    result = cursor.fetchall()
    cities = [row[0] for row in result]
    counts = [row[1] for row in result]
    print(cities)
    print(counts)
    # 创建城市top15图表
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(cities[:15])
        .add_yaxis("City Count", counts[:15])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="城市岗位数量TOP15"),
            xaxis_opts=opts.AxisOpts(name="城市"),
            yaxis_opts=opts.AxisOpts(name="数量"))
        # legend_opts=opts.LegendOpts(is_show=False),  # 图例显示设置
        # tooltip_opts=opts.TooltipOpts(trigger="axis"),  # 提示框设置
        # datazoom_opts=[opts.DataZoomOpts()],
    )
    return c


# ______________________文化饼图____________________________
def pie_degree() -> Pie:
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='lagou')
    # 渲染图表为HTML文件
    cursor = conn.cursor()
    # 读取数据
    sql = "SELECT degre FROM positions"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    data = [item[0] for item in result]
    degre_list = [i for item in data for i in item.split(',')]
    degre_series = pd.Series(data=degre_list)
    degre_value_counts = degre_series.value_counts()
    degres = list(degre_value_counts.index)
    print(degre_value_counts)
    pie = (
        Pie()
        .add("", [list(z) for z in zip(degres, degre_value_counts)], radius=["50%", "70%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="招聘方学历情况"),
                         legend_opts=opts.LegendOpts(is_show=False, pos_left="35%")
                         )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d})%"))
    )
    cursor.close()
    conn.close()
    return pie


# ——————————————————————————薪资柱状图—————————————————————
def bar_salary() -> Bar:
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='lagou')
    # 渲染图表为HTML文件
    cursor = conn.cursor()
    # 创建salary和experience关系图
    sql = "SELECT experience, salary FROM positions"
    # print(sql_relation)
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    # 使用字典来分组数据
    grouped_data = {}
    for experience, salary_range in result:
        if experience not in grouped_data:
            grouped_data[experience] = []
        grouped_data[experience].append(salary_range)
        # 将字典转换成你想要的列表格式，同时去重（如果需要）
    result_salary = []
    for experience, salary_ranges in grouped_data.items():
        # 如果你想要去除重复的薪资范围，可以使用集合再转换回列表
        # unique_salary_ranges = list(set(salary_ranges))
        unique_salary_ranges = salary_ranges
        result_salary.append((experience, unique_salary_ranges))
        # 打印结果
    print(result_salary)
    # 计算每个经验级别的薪资平均值
    experience_salaries = {}
    for experience, salary_ranges in result_salary:
        if experience == '经验10年以上':
            filtered_ranges = filter_salaries_by_lowpoint(experience, salary_ranges, 2500)
            salary_sums = [parse_salary_range(range_) for range_ in filtered_ranges]
            if salary_sums:
                experience_salaries[experience] = int(sum(salary_sums) / len(salary_sums))
        elif experience == '经验5-10年':
            filtered_ranges = filter_salaries_by_highpoint(experience, salary_ranges, 25000)
            salary_sums = [parse_salary_range(range_) for range_ in filtered_ranges]
            if salary_sums:
                experience_salaries[experience] = int(sum(salary_sums) / len(salary_sums))
        elif experience == '经验1年以下':
            filtered_ranges = filter_salaries_by_highpoint(experience, salary_ranges, 16000)
            salary_sums = [parse_salary_range(range_) for range_ in filtered_ranges]
            if salary_sums:
                experience_salaries[experience] = int(sum(salary_sums) / len(salary_sums))
        elif experience == '经验3-5年':
            # 过滤薪资高于24k的
            filtered_ranges = filter_salaries_by_highpoint(experience, salary_ranges, 24000)
            salary_sums = [parse_salary_range(range_) for range_ in filtered_ranges]
            if salary_sums:
                experience_salaries[experience] = int(sum(salary_sums) / len(salary_sums))
        elif experience == '经验在校/应届':
            # 过滤薪资高于20k的
            filtered_ranges = filter_salaries_by_highpoint(experience, salary_ranges, 20000)
            salary_sums = [parse_salary_range(range_) for range_ in filtered_ranges]
            if salary_sums:
                experience_salaries[experience] = int(sum(salary_sums) / len(salary_sums))
        else:
            # 其他情况，不需要过滤
            salary_sums = [parse_salary_range(range_) for range_ in salary_ranges]
            if salary_sums:
                experience_salaries[experience] = int(sum(salary_sums) / len(salary_sums))
    # 打印经验级别和薪资平均值
    print(experience_salaries)
    # 提取x轴和y轴的数据
    x_data = list(experience_salaries.keys())
    y_data = list(experience_salaries.values())
    # 创建salary和experience折线图
    line = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add_xaxis(x_data)
        .add_yaxis("Salary", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="招聘方薪资与经验关系"),
                         xaxis_opts=opts.AxisOpts(name="经验"),
                         yaxis_opts=opts.AxisOpts(name="薪资"))
    )
    cursor.close()
    conn.close()
    return line


# #______________________职业饼图____________________________
def pie_title() -> Pie:
    # data = pd.read_csv('jobs1.csv')
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='lagou')
    # 渲染图表为HTML文件
    cursor = conn.cursor()
    # 创建salary和experience关系图
    sql = "SELECT title FROM positions"
    # print(sql_relation)
    cursor.execute(sql)
    result = cursor.fetchall()
    top = 5
    data = [item[0] for item in result]
    industry_list = [i for item in data for i in item.split(',')]
    industry_series = pd.Series(data=industry_list)
    industry_value_counts = industry_series.value_counts()
    industrys = list(industry_value_counts.head(top).index)
    industry_counts = list(industry_value_counts.head(top))
    print(industry_counts)
    pie = (
        Pie()
        .add("", [list(z) for z in zip(industrys, industry_counts)])
        .set_global_opts(title_opts=opts.TitleOpts(title="招聘方所属行业"),
                         legend_opts=opts.LegendOpts(is_show=False, pos_left="30%"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    cursor.close()
    conn.close()
    return pie


# ---------------城市地理坐标图--------------
def geo_base() -> Geo:
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='lagou')
    # 渲染图表为HTML文件
    cursor = conn.cursor()
    sql_city = "SELECT address, COUNT(*) as count FROM positions GROUP BY address ORDER BY count DESC"
    cursor.execute(sql_city)
    result = cursor.fetchall()
    cities = [row[0] for row in result]
    counts = [row[1] for row in result]
    # 城市位置地理坐标图表
    data = [[cities, counts] for cities, counts in zip(cities, counts)]
    print(f"这是地图数据：{data}")

    # 初始化Geo对象
    c = (
        Geo()
        .add_schema(maptype="china")  # 设置地图类型为中国地图
        .add("城市数据", data, type_=ChartType.EFFECT_SCATTER)  # 添加数据，使用散点图效果
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 设置标签不显示
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=200),  # 设置视觉映射配置项，最大值为200（根据实际数据调整）
            title_opts=opts.TitleOpts(title="中国城市数据分布图"),  # 设置标题
        )
    )
    cursor.close()
    conn.close()
    return c


def get_treatments() -> WordCloud:
    # 词云图
    # TODO: 实现词云图功能
    conn = pymysql.connect(host='localhost', user='root', password='123456', db='lagou')
    cursor = conn.cursor()
    sql_position = "SELECT treatment FROM positions "
    cursor.execute(sql_position)
    results = cursor.fetchall()
    treatment = [item[0].replace('“', '').replace('”', '') for item in results if item[0] != '无']
    print(f"这是待遇数据：{treatment}")
    word_freq_dict = [(word, random.randint(50, 500)) for word in treatment]
    print(word_freq_dict)

    w = (
        WordCloud(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .add(series_name="", data_pair=word_freq_dict, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title="薪资待遇cloud图"))
    )
    cursor.close()
    conn.close()
    return w


def datashow():
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='123456', database='lagou')
    # 创建游标
    cursor = db.cursor()
    # 执行SQL语句
    data = "SELECT * FROM positions"
    cursor.execute(data)
    # 获取结果集
    datas = cursor.fetchall()
    # 定义字典的键
    keys = ['id', 'title', 'experience', 'salary', 'degre', 'company_name', 'address', 'company_scale',
            'treatment']

    # 转换元组列表为字典列表
    data_dicts = [dict(zip(keys, item)) for item in datas]

    # 打印结果
    for data_dict in data_dicts:
        print(data_dict)

    return data_dicts
