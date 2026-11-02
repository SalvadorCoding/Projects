import socket
import argparse

parser = argparse.ArgumentParser("Port Scanner", description="Write in the range (or just the singular) port(s) you would like to scan!")
start_port = parser.add_argument("start-port")

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host,port))
    s.close()

    if result == 0:
        return True
    else:
        return False

host = parser.add_argument("-s", "--start", type=int, default=1)
start_port = int(input("What is the starting port? "))
end_port = int(input("What is the end port? "))

for port in range(start_port, end_port + 1):
    if scan_port(host, port):# == True
        print("Port", port,"is open!")
