import socket
import argparse

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
start_port = int(input("What is the starting port? "))
end_port = int(input("What is the end port? "))

for port in range(start_port, end_port + 1):
    if scan_port(host, port):# == True
        print("Port", port,"is open!")
