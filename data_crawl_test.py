# @时间 2024/6/13 9:45
# @Author：郑摇2021210510
# @File : data_crawl_test.py
import pyecharts.options as opts
from pyecharts.charts import Map3D, Bar, Line, Pie, Radar, Page
from pyecharts.faker import Faker
from pyecharts.globals import ChartType, ThemeType

# 标题
def title() -> Pie():
    title = (
        Pie(
            init_opts=opts.InitOpts(
                chart_id='view_title',
                width='100vw',
                theme='dark',
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="基于爬取拉钩网python工作岗位数据可视化大屏",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=32,
                    color='white'
                ),
                # 标题居中
                pos_left='center'
            ),
            legend_opts=opts.LegendOpts(
                is_show=False
            )
        )
    )
    return title

# 中间地图
def map3d() -> Map3D:
    data_pair = [
        [(113.2700, 23.1300), (118.8062, 31.9208)], [(125.8154, 44.2584), (87.9236, 43.5883)],
        [(117.4219, 39.4189), (108.3843, 30.4397)], [(91.1100, 29.9700), (103.9526, 30.7617)],
        [(108.4790, 23.1152), (117.2900, 32.0581)], [(113.0823, 28.2568), (110.3893, 19.8516)],
        [(101.4038, 36.8207), (119.4543, 25.9222)], [(116.0046, 28.6633), (110.3467, 41.4899)],
    ]
    data_pair1 = [
        [(110.3653, 21.2662), (106.2428, 38.4731)], [(114.5395, 38.0364), (108.2733, 22.7812)]
    ]
    map3d = (
        # 3D地图
        Map3D(
            # 初始化配置项
            init_opts=opts.InitOpts(
                theme='dark',  # 图表主题 white dark
                chart_id='view_map3d'
            )
        )
        # !!!!全局配置项!!!!
        .set_global_opts(
            # 标题配置项
            title_opts=opts.TitleOpts(
                title="",  # 主标题
            ),
            legend_opts=opts.LegendOpts(
                border_width=0,
                pos_bottom='50px',
                pos_left='500px'
            )
        )
        .add_schema(
            # 地图类型
            maptype='china',
            # 图元样式配置项
            itemstyle_opts=opts.ItemStyleOpts(
                # 图形的颜色
                color="#1661AB",
                # 描边宽度，默认不描边。
                border_width=0.8,
                # 图形的描边颜色。支持的颜色格式同 color，不支持回调函数。
                border_color="rgb(62,215,213)"
            ),
        )
        # 数据配置
        .add(
            # 系列名称，用于 tooltip 的显示，legend 的图例筛选
            series_name='类型1',
            # 数据项 (坐标点名称，坐标点值)
            data_pair=data_pair,
            # 叠加图的类型（目前只支持 Bar3D，Line3D，Lines3D，Scatter3D）
            type_=ChartType.LINES3D,
            # 仅在 Lines3D 起作用
            # 飞线的尾迹特效，参考 `series_options.Line3DEffectOpts`
            effect=opts.Lines3DEffectOpts(
                # 是否显示尾迹特效，默认不显示。
                is_show=True,
                # 尾迹特效的周期。
                period=4,
                # 尾迹的宽度。
                trail_width=3,
                # 尾迹的长度，范围从 0 到 1，为线条长度的百分比
                trail_length=0.5,
                # 尾迹的颜色，默认跟线条颜色相同。
                trail_color="white",
                # 尾迹的不透明度，默认跟线条不透明度相同
                trail_opacity=1,
            ),
            # 仅在 Line3D，Lines3D 起作用
            # 飞线的线条样式，参考 `series_options.LineStyleOpts`
            linestyle_opts=opts.LineStyleOpts(
                # 是否显示
                is_show=True,
                # 线宽
                width=3,
                # 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形
                opacity=0.5,
                # 线的颜色
                color="#00ad5c",
            ),
        )
        .add(
            # 系列名称，用于 tooltip 的显示，legend 的图例筛选
            series_name='类型2',
            # 数据项 (坐标点名称，坐标点值)
            data_pair=data_pair1,
            # 叠加图的类型（目前只支持 Bar3D，Line3D，Lines3D，Scatter3D）
            type_=ChartType.LINES3D,
            # 仅在 Lines3D 起作用
            # 飞线的尾迹特效，参考 `series_options.Line3DEffectOpts`
            effect=opts.Lines3DEffectOpts(
                # 是否显示尾迹特效，默认不显示。
                is_show=True,
                # 尾迹特效的周期。
                period=4,
                # 尾迹的宽度。
                trail_width=3,
                # 尾迹的长度，范围从 0 到 1，为线条长度的百分比
                trail_length=0.5,
                # 尾迹的颜色，默认跟线条颜色相同。
                trail_color="white",
                # 尾迹的不透明度，默认跟线条不透明度相同
                trail_opacity=1,
            ),
            # 仅在 Line3D，Lines3D 起作用
            # 飞线的线条样式，参考 `series_options.LineStyleOpts`
            linestyle_opts=opts.LineStyleOpts(
                # 是否显示
                is_show=True,
                # 线宽
                width=3,
                # 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形
                opacity=0.5,
                # 线的颜色
                color="yellow",
            ),
        )
    )
    return map3d

# 左边折线图
def line() -> Line():
    line = (
        # 折线图
        Line(
            # 初始化配置项
            init_opts=opts.InitOpts(
                theme='dark',  # 图表主题 white dark
                chart_id='view_lines'
            )
        )
        # !!!!全局配置项!!!!
        .set_global_opts(
            # 标题配置项
            title_opts=opts.TitleOpts(
                title="航班延误数",  # 主标题
            ),
            legend_opts=opts.LegendOpts(
                border_width=0,
                pos_right='30px'
            ),
            # 区域缩放配置项
            # datazoom_opts=opts.DataZoomOpts(
            #     is_show=False,  # 是否显示 组件。如果设置为 false，不会显示，但是数据过滤的功能还存在
            #     type_="slider",  # 组件类型，可选 "slider", "inside"
            #     orient="horizontal"  # 可选值为：'horizontal', 'vertical'
            # )
        )
        # X轴配置
        .add_xaxis(Faker.week)
        # Y轴配置
        .add_yaxis("FA293", Faker.values())
        .add_yaxis("Y6T28", Faker.values())
        # 颜色配置
        .set_colors(['red', 'lightblue'])
    )
    return line

# 左边条形图
def bar() -> Bar():
    x_data = ['航班1', '航班2', '航班3', '航班4', '航班5', '航班6', '航班7']
    bar = (
        # 条形图
        Bar(
            # 初始化配置项
            init_opts=opts.InitOpts(
                theme='dark',  # 图表主题 white dark
                chart_id='view_bar'
            )
        )
        # !!!!全局配置项!!!!
        .set_global_opts(
            # 标题配置项
            title_opts=opts.TitleOpts(
                title="各航班人数",  # 主标题
            ),
            legend_opts=opts.LegendOpts(
                border_width=0,
                pos_right='30px'
            ),
            # # 区域缩放配置项
            # datazoom_opts=opts.DataZoomOpts(
            #     is_show=True,  # 是否显示 组件。如果设置为 false，不会显示，但是数据过滤的功能还存在
            #     type_="slider",  # 组件类型，可选 "slider", "inside"
            #     orient="horizontal"  # 可选值为：'horizontal', 'vertical'
            # )
        )
        # X轴配置
        .add_xaxis(xaxis_data=x_data)
        # Y轴配置
        .add_yaxis("经济舱", Faker.values(), stack='all', is_realtime_sort=True)
        .add_yaxis("商务舱", Faker.values(), stack='all')
        .add_yaxis("头等舱", Faker.values(), stack='all')
        # 颜色配置
        .set_colors(['lightblue', 'lightgreen', 'yellow'])
        .set_series_opts(
            label_opts=opts.LabelOpts(
                is_show=False
            ),
        )
    )
    return bar

# 右边饼图
def pie() -> Pie():
    x_data = ['头等舱', '商务舱', '经济舱']
    y_data = [7652, 10293, 20376]
    pie = (
        # 饼图
        Pie(
            # 初始化配置项
            init_opts=opts.InitOpts(
                theme='dark',  # 图表主题 white dark
                chart_id='view_pie'
            )
        )
        # !!!!全局配置项!!!!
        .set_global_opts(
            # 标题配置项
            title_opts=opts.TitleOpts(
                title="今日舱位人数占比",  # 主标题
            ),
            legend_opts=opts.LegendOpts(
                border_width=0,
                pos_left='right'
            )
        )
        # 数据配置
        .add(
            # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
            series_name="所有航班",
            # 系列数据项，格式为 [(key1, value1), (key2, value2)]
            data_pair=[list(z) for z in zip(x_data, y_data)],
            radius=['35%', '60%'],
            # center=['50%', '50%'],
            # rosetype="radius"
        )
        #颜色配置
        .set_colors(Faker.visual_color)
    )
    return pie


# 右边雷达图
def radar() -> Radar():
    radar = (
        # 雷达图
        Radar(
            # 初始化配置项
            init_opts=opts.InitOpts(
                theme='dark',  # 图表主题 white dark
                chart_id='view_radar'
            )
        )
        # !!!!全局配置项!!!!
        .set_global_opts(
            # 标题配置项
            title_opts=opts.TitleOpts(
                title="实时天气预报",  # 主标题
            ),
            legend_opts=opts.LegendOpts(
                pos_left='right',
                border_width=0,
                # orient='vertical'
            )
        )

        # 指示器配置
        .add_schema(
            shape='circle',
            center=['50%', '55%'],
            radius='70%',
            schema=[
                opts.RadarIndicatorItem(name="云量"),
                opts.RadarIndicatorItem(name="气温"),
                opts.RadarIndicatorItem(name="气压"),
                opts.RadarIndicatorItem(name="辐射"),
                opts.RadarIndicatorItem(name="湿度"),
                opts.RadarIndicatorItem(name="风速"),
                opts.RadarIndicatorItem(name="能见度")
            ]
        )
        # 数据配置
        .add(
            # 系列名称，用于 tooltip 的显示，legend 的图例筛选
            series_name='现在',
            # 系列数据项
            data=[Faker.values(0, 100)],
            # 系列颜色
            color="yellow",
            areastyle_opts=opts.AreaStyleOpts(
                color='yellow',
                opacity=0.4
            )
        )
        .add(
            series_name='一个小时后',
            data=[Faker.values(1, 100)],
            color="aqua",
            areastyle_opts=opts.AreaStyleOpts(
                color='aqua',
                opacity=0.3
            )
        )
        .add(
            series_name='两个小时后',
            data=[Faker.values(1, 100)],
            color="chartreuse",
            areastyle_opts=opts.AreaStyleOpts(
                color='chartreuse',
                opacity=0.3
            )
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(
                is_show=False
            )
        )
    )
    return radar

# 合并页面
def page() -> Page():
    page = (
        Page(
            # 页面标题
            page_title='基于爬取拉钩网python工作岗位数据可视化大屏',
            # 布局配置项
            layout=Page.DraggablePageLayout
        )
        .add(title(), map3d(), bar(), line(), pie(), radar())
    )
    page.render(path='visual.html')

    # 用于 DraggablePageLayout 布局重新渲染图表
    # page.save_resize_html(
    #     # Page 第一次渲染后的 html 文件
    #     source="visual.html",
    #     # 布局配置文件
    #     cfg_file="visual.json",
    #     # 重新生成的 .html 存放路径
    #     dest="visual_new.html"
    # )
    # return page


if __name__ == '__main__':
    # 全局设置主题颜色
    theme_config = ThemeType.CHALK  # 颜色方案
    # 表格和标题的颜色
    table_color = ""
    if theme_config == ThemeType.DARK:
        table_color = '#333333'
    elif theme_config == ThemeType.CHALK:
        table_color = '#293441'
    elif theme_config == ThemeType.PURPLE_PASSION:
        table_color = '#5B5C6E'
    elif theme_config == ThemeType.ROMANTIC:
        table_color = '#F0E8CD'
    elif theme_config == ThemeType.ESSOS:
        table_color = '#FDFCF5'
    else:
        table_color = ''
    page()
