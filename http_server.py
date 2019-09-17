'''
http服务端
如果浏览器的请求内容 /
响应码为 200 OK,将index.html内容作为相应内容
如果浏览器的请求是其他的
响应吗为 404 Not Fount 内容为 'Sorry...'
'''

from socket import *
# 与客户端交互
def handle(connfd):
    # 获取http请求
    data = connfd.recv(4096).decode()
    request_line = data.split('\n')[0] #请求行
    info = request_line.split(' ')[1]#请求内容
    # 看一下请求内容是不是/
    if info == '/':
        with open('index.html') as f:
            # 组织http响应
            response = "HTTP/1.1 200 OK\r\n" # 响应行
            response += "Content-type:text/html\r\n" # 响应头
            response += '\r\n' # 空行
            response += f.read() # 数据内容
    else:
        pass

