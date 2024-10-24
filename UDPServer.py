from socket import *  # 从socket模块导入所有内容，以便使用网络编程相关的功能

serverPort = 12000  # 指定服务器的端口号，服务器将监听该端口接收数据

serverSocket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字，AF_INET表示IPv4，SOCK_DGRAM表示UDP协议

serverSocket.bind(('', serverPort))  # 将服务器套接字绑定到指定的端口号，''表示可以绑定到任意可用的本地IP地址

print("The server is ready to receive")  # 打印消息，告知服务器已准备好接收客户端消息

while True:  # 进入无限循环，持续等待客户端消息
    message, clientAddress = serverSocket.recvfrom(2048)  # 接收来自客户端的消息，2048为接收缓冲区大小，返回客户端的消息和地址

    modifiedMessage = message.decode().upper()  # 将接收到的消息解码为字符串，并将其转换为大写

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)  # 将修改后的消息编码为字节，并发送回客户端的地址
