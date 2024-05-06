import socket
import threading
import time


# 目标开放端口探测
def socket_port(ip, port):
    for port in range(port, port + 50):
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((ip, port))
            print(f"port: {port} 可用")
            s.close()
        except:
            pass
        time.sleep(3)


if __name__ == '__main__':
    user_input = input("输入ip")
    for i in range(1, 5000, 50):
        threading.Thread(target=socket_port, args=('user_input', i)).start()
