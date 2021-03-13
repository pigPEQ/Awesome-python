import socket
import threading
import  sys

class HttpWebServer(object):
    def __init__(self,port):
        # 创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        tcp_server_socket.bind(('', port))
        # 设置最大监听
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def new_socket_deal(new_socket):
        # 接收数据
        recv_data = new_socket.recv(4096)
        # 如果没有接收请求的内容，关闭服务于客户端的套接字
        if len(recv_data) == 0:
            new_socket.close()
            return
        # 获取请求字符串
        recv_data_str = recv_data.decode('UTF-8')
        # 获取请求的资源路径
        request_list = recv_data_str.split(' ', maxsplit=2)
        request_path = request_list[1]
        # 判断访问文件是否存在 1.os.path.exists('static' + request.path) 2.异常
        # 如果访问的为根路径，指定默认访问路径
        if request_path == '/':
            request_path = '/index.html'
        # 判断访问文件是否存在 1.os.path.exists('static' + request.path) 2.异常try-except-else-finally
        try:
            # 打开文件读取数据,操作模式加上二进制模式兼容图片的读取
            with open('static' + request_path, 'rb') as file:
                file_content = file.read()
        # 如果没有对应的请求资源路径
        except Exception:
            # 响应行
            response_line = 'HTTP/1.1 404 No such file\r\n'
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'
            # 响应体
            with open('static/error.html', 'rb') as file:
                error_content = file.read()
            response_body = error_content
            # 将数据封装为 http响应请求报文
            response = (response_line + response_header + '\r\n').encode('UTF-8') + response_body
            # 发送数据
            new_socket.send(response)
        else:
            # 响应头
            response_header = 'Server: PWS/1.0\r\n'
            # 响应行
            response_line = 'HTTP/1.1 200 OK\r\n'
            # 响应体
            response_body = file_content
            # 将数据封装为 http响应请求报文
            response = (response_line + response_header + '\r\n').encode('UTF-8') + response_body
            # 发送数据
            new_socket.send(response)
        finally:
            # 关闭服务于客户端的套接字
            new_socket.close()

    def run(self):
        # 循环等待连接
        while True:
            # 接收连接请求，新的套接字
            new_socket, port = self.tcp_server_socket.accept()
            # 创建子线程，处理客户端消息
            sub_thread = threading.Thread(target=self.new_socket_deal, args=(new_socket,))
            # 设置守护主线程
            sub_thread.setDaemon(True)
            # 启动子线程
            sub_thread.start()


def main():
    # 获取终端命令行参数
    params = sys.argv
    # 参数格式校验
    if len(params) != 2:
        print('请输入正确的命令，格式如python3 xxx.py 1000 ')
        return
    if not params[1].isdigit():
        print('请输入正确的命令，格式如python3 xxx.py 1000 ')
        return
    # 从命令行中获取端口号
    port = int(params[1])
    # 创建HttpWebServer对象
    httpwebserver = HttpWebServer(port)
    # 启动服务器
    httpwebserver.run()

#判断是否为主模块
if __name__ == '__main__':
    main()