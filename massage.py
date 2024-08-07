import time
import pymysql
import requests
from bs4 import BeautifulSoup

# MySQL 数据库连接配置
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'database': 'lagou',
    'charset': 'utf8mb4',
}

# 创建 MySQL 连接对象
conn = pymysql.connect(**db_config)
cursor = conn.cursor()

# 创建一个名为的表
create_table_sql = '''CREATE TABLE positions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        experience VARCHAR(255) ,
        salary VARCHAR(255) NOT NULL,
        degre VARCHAR(255) NOT NULL,
        company_name VARCHAR(255) NOT NULL,
        address VARCHAR(255),
        company_scale VARCHAR(255),
        treatment VARCHAR(255)   
    );
    '''
# 检查表是否已存在的SQL语句
check_table_sql = "SHOW TABLES LIKE 'positions';"

# 执行SQL语句检查表是否存在
cursor.execute(check_table_sql)
table_exists = cursor.fetchone() is not None

# 如果表不存在，则创建它
if not table_exists:
    cursor.execute(create_table_sql)
    conn.commit()
    print("表 'positions' 已创建")
else:
    print("表 'positions' 已存在，未创建新表")



def get_lagou_jobs():
    # url = 'https://www.lagou.com/wn/zhaopin?fromSearch=true&kd=python&pn={}'
    url ='https://www.lagou.com/wn/jobs?pn={}&cl=false&fromSearch=true&kd=python&needAddtionalResult=true'
    # 设置headers以模拟浏览器请求（可能需要根据实际情况进行调整）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Cookie':'index_location_city=%E5%85%A8%E5%9B%BD; RECOMMEND_TIP=1; user_trace_token=20240613100105-302bc954-a68a-4d7a-a5a8-745349149312; _ga=GA1.2.446348378.1718244068; LGUID=20240613100108-09356abb-a8e2-400c-b85d-866bb872c75d; gate_login_token=v1####97349bfbdfe9c661858d47f9a99830176f7f85a8affdb3d232eb852f223358fe; LG_HAS_LOGIN=1; hasDeliver=0; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1718244068,1718266062,1718275624; _ga_DDLTLJDLHH=GS1.2.1718275623.4.0.1718275623.60.0.0; __lg_stoken__=8f3c25270b00be799c21e84bc9303b64073e5d9e53fbbd1173d4a5a7c83b5675f3cd629c12bd3bff1a812b9678e274044488ab477e1b35e1d72fbdbd04082eeb3fb797194d19; _putrc=5883B8D1AFBEBCE0123F89F2B170EADC; JSESSIONID=ABAACCCABGDAAAAA89D560E549C39A992BAC115DF3E38EB; login=true; unick=%E7%94%A8%E6%88%B78028; WEBTJ-ID=20240617230010-19026b676ef4c4-0c8182b59538fd-4c657b58-1327104-19026b676f091f; sensorsdata2015session=%7B%7D; X_HTTP_TOKEN=0072a2b1fa2948f99256368171414fc9cfb2b386eb; X_MIDDLE_TOKEN=29d4ebf52ac3de952fcd60cd4b2d1938; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2227085389%22%2C%22%24device_id%22%3A%221900f53ca4e278-0c1b02f29c1d56-4c657b58-1327104-1900f53ca4f14d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22pctop618_jljx%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22121.0.0.0%22%7D%2C%22first_id%22%3A%221900f53ca4e278-0c1b02f29c1d56-4c657b58-1327104-1900f53ca4f14d%22%7D'}
    # fieldnames = ['title', 'salary', 'company_name', 'experience', 'degree', 'address', 'company_scale','treatment']
    # with open('jobs1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #
    #     # 写入字段名（表头）
    #     writer.writeheader()
    for page in range(1, 31):
        try:
            # 发送网络请求
            response = requests.get(url.format(page), headers=headers)
            # response.raise_for_status()  # 如果请求失败，抛出HTTPError异常

            # 解析HTML内容
            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)

            # 这里需要根据实际的HTML结构来定位你想要的信息
            # 假设每个职位信息都在一个class为"job-list-content"的div中
            job_list = soup.find_all('div', class_="item__10RTO")
            for job in job_list:
                # 提取职位标题，这里假设标题在class为"position-name"的span中
                title = job.find('a', id="openWinPostion").get_text(strip=True).split('[')[0]
                # 提取其他信息，如公司名、地址、薪资等...
                salary = job.find('span', class_="money__3Lkgq").get_text(strip=True)
                #
                company_name = job.find('div', class_="company-name__2-SjF").get_text(strip=True)
                #
                experience = job.find('div', class_="p-bom__JlNur").get_text(strip=True).split()[0].split('k')[-1]

                #
                degree = job.find('div', class_="p-bom__JlNur").get_text(strip=True).split()[-1]
                #
                address = \
                job.find('a', id="openWinPostion").get_text(strip=True).split('[')[-1].split(']')[0].split('·')[0]
                #
                industry_div = job.find('div', class_="industry__1HBkr")
                if industry_div is not None:
                    company_scale = industry_div.get_text(strip=True).split()[-1]
                else:
                    # 处理没有找到元素的情况，例如设置默认值或记录错误
                    company_scale = "未找到公司规模信息"
                treatment = job.find('div', class_="il__3lk85").get_text(strip=True).split('“')[-1].split('”')[0]
                print(treatment)
                # 构建商品信息字典
                message = {
                    'title': title,
                    'salary': salary,
                    'company_name': company_name,
                    'experience': experience,
                    'degree': degree,
                    'address': address,
                    'company_scale': company_scale,
                    'treatment': treatment
                }
                # 将职位信息写入CSV文件
                # writer.writerow(message)
                save_to_mysql(message)
                print(message)
            time.sleep(30)


        except requests.RequestException as e:
            print(f"Error occurred: {e}")


def save_to_mysql(result):
    try:
        sql = "INSERT INTO {} (title, salary, company_name, experience, degre, address, company_scale,treatment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(
            'positions')
        print("sql语句为:  " + sql)
        cursor.execute(sql, (result['title'], result['salary'], result['company_name'], result['experience'], result['degree'], result['address'], result['company_scale'], result['treatment']))
        conn.commit()
        print('存储到MySQL成功: ', result)
    except Exception as e:
        print('存储到MYsql出错: ', result, e)
        # 示例URL（请替换为实际的拉钩招聘网职位列表页面URL）


#
if __name__ == '__main__':
    # 调用函数爬取职位信息
    get_lagou_jobs()
