import socket
target_ip =input("host_ip: ")
target_port =int(input("host_port: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((target_ip, target_port))

    data_send = "Hello, server!"
    sock.send(data_send.encode())

    sock.close()

except Exception as e:
    print("Connection error: ", str(e))
