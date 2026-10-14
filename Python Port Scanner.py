import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host,port))
    s.close()

    if result == 0:
        return True
    else:
        return False

host = input("What is the host? ")
port = int(input("What is the port? "))
test1 = scan_port(host, port)
print(test1)
