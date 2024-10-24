from socket import *  # 从socket模块导入所有内容，以便使用网络编程相关的功能

serverName = '172.28.101.207'  # 指定服务器的IP地址，表示客户端将连接到此服务器
serverPort = 12000  # 指定服务器的端口号，用于发送数据的目标端口

clientSocket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字，AF_INET表示IPv4，SOCK_DGRAM表示UDP协议

message = input('Input lowercase sentence:')  # 从用户那里获取输入的字符串，用于发送给服务器

clientSocket.sendto(message.encode(), (serverName, serverPort))  # 将用户输入的字符串编码成字节，并通过套接字发送给服务器，发送到指定的服务器地址和端口

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # 从服务器接收修改后的消息，2048表示缓冲区大小，返回数据和服务器的地址

print(modifiedMessage.decode())  # 将接收到的字节数据解码为字符串，并打印输出

clientSocket.close()  # 关闭客户端套接字，释放资源
