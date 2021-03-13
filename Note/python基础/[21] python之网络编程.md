<details>
<summary>思维导图</summary>
</br>



![](/Note/python基础/res/python之网络编程.png)

</details>

### 创建TCP客户端

```python
import socket

if __name__ == '__main__':
    # 创建套接字对象  socket.AF_INET:IPV4  socket.SOCK_STREAM:tcp
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    tcp_server_socket.connect(("192.168.12.2", 8080))
    # 发送数据 send()
    content1 = input('请输入发送数据:')
    tcp_server_socket.send(content1.encode('UTF-8'))
    # 接收数据
    content2 = tcp_server_socket.recv(1024)
    print("客户端接收数据为:", content2.decode('UTF-8'))
    # 关闭连接 close()
    tcp_server_socket.close()
```

### 创建TCP服务端

```python
import socket
import threading


def deal_thread(new_client, port):
    print("客户端与服务器建立连接成功！")
    print("当前接入的客服端端口号为:", port)
    # 循环接收客户端消息
    while True:
        # 接收数据 recv()
        content1 = new_client.recv(1024)
        if content1:
            print("接收的数据长度为:", len(content1))
            print("服务端接收到的数据为：", content1.decode('UTF-8'))
            # 发送数据 send()
            content2 = input('请输入发送数据:')
            new_client.send(content2.encode('UTF-8'))
        else:
            print('客服端下线了!')
            break
    # 关闭连接 close()
    new_client.close()


if __name__ == '__main__':
    # 创建套接字对象  socket.AF_INET:IPV4  socket.SOCK_STREAM:tcp
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 复用端口号 socket.SOL_SOCKET:当前套接字 socket.SO_REUSEADDR端口号复用选项
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口 bind((ipAdress,port)) IP地址一般不用指定，表示本机的任一IP即可
    tcp_server_socket.bind(("", 8080))
    # 设定监听 listen() 最大等待建立连接的个数
    tcp_server_socket.listen(128)
    # 循环等待客户端的连接请求
    while True:
        # 等待请求 accept()  接收到新请求时返回一个新socket，以后的通信使用新的socket通信
        # tcp_socket_client这个监听之后的套接字以后仅用于接收客户端请求，
        # 新的套接字new_client收发数据
        new_client, port = tcp_server_socket.accept()
        # 当一个客户端和服务端建立连接时，创建一个子线程去执行数据的收发
        sub_thread = threading.Thread(target=deal_thread, args=((new_client, port)))
        # 守护主线程
        sub_thread.setDaemon(True)
        sub_thread.start()
    # 关闭被动套接字后无法建立新的连接，之前建立的连接可以正常通信
    # tcp_server_socket.close()
    # 因为服务端的程序需要一直运行，所以服务端的套接字可以不用关闭
```

