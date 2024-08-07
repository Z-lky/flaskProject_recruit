# -*- coding: utf-8 -*-
# @Author: 李超权
# @Date: 2024/6/16
from datetime import datetime

from flask import Flask, render_template, jsonify
from show import bar_base, bar_salary, pie_degree, pie_title, geo_base, get_treatments,datashow
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']##中文乱码问题！
plt.rcParams['axes.unicode_minus']=False#横坐标负号显示问题！

app = Flask(__name__)

#
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/datashow')
def database():
    data_dicts = datashow()
    return render_template('datashow.html',data_dicts=data_dicts)
#
@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()
#
@app.route("/salaryChart")
def get_galary_chart():
    b = bar_salary()
    return b.dump_options_with_quotes()

@app.route("/degreeChart")
def get_degree_chart():
    p = pie_degree()
    return p.dump_options_with_quotes()
#
@app.route("/titleChart")
def get_title_chart():
    t = pie_title()
    return t.dump_options_with_quotes()

@app.route("/ddtChart")
def get_ddt_chart():
    g = get_treatments()
    return g.dump_options_with_quotes()

@app.route("/geoChart")
def get_geo_chart():
    g = geo_base()
    return g.dump_options_with_quotes()

@app.route('/get_server_time', methods=['GET'])
def get_server_time():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'server_time': now})

if __name__ == '__main__':
    app.run(debug=True)