import time
import pymysql


def index():
    # 状态信息,响应头
    status = "200 ok"
    headers = [('server', 'BWS1.2')]
    # 1.获取模板文件
    with open('temple/index.html', 'r') as file:
        file_data = file.read()
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='cl102646',
                           database='python',
                           charset='utf8'
                           )
    # 获取游标对象
    cursor = conn.cursor()
    # 准备sql
    sql = 'select * from student;'
    # 执行sql并保存结果
    cursor.execute(sql)
    result = cursor.fetchall()
    # 关闭游标、连接对象
    cursor.close()
    conn.close()
    # web处理后的数据
    data = ''
    for row in result:
        data += '''<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>''' % row

    response_body= file_data.replace('{%content%}', data)
    return status, headers, response_body


def center():
    pass


# 处理动态资源请求
def notfound():
    status = '404 not found'
    headers = [('server', 'BWS1.2')]
    data = 'not found'
    return status, headers, data


# 路由列表
route_list = [
    ('/index.html', index),
    ('/center.html', center)
]


def get_content(env):
    # 获取到请求资源路径
    request_path = env['request_path']
    # 根据请求路径的类型，为其指定相应处理函数
    # 对路由列表进行遍历，执行相应函数
    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        result = notfound()
        return result
