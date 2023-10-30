import socket

host =input('Give host: ')
ports = range(1, 1025)

def scan_port(host, port):
    try:
        socket.setdefaulttimeout(1)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.connect((host, port))
       
        print("Port is open: ",port)
        
        sock.close()
        
    except ConnectionRefusedError:
        print("Port is closed: ",port)
    except Exception as e:
        print("Port error: " , port,":", str(e))


for port in ports:
    scan_port(host, port)