import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

# Creating the port scanning function
def scan_port(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host,port))
        s.close()

        if result == 0:
            return True
        else:
            return False

parser = argparse.ArgumentParser("Port Scanner", description="Write in the range (or just the singular) port(s) you would like to scan!")
parser.add_argument("host")

# Threading pool - creating 100 workers to work through the ports at the same time
with ThreadPoolExecutor(max_workers=100) as executor:
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int,default=1024)
    args = parser.parse_args()
    ports = range(args.start,args.end + 1)
    hosts = [args.host] * len(ports)
    
    resultMap = executor.map(scan_port,[args.host] * len(ports),ports)
    
# Tells the user which ports are open
for ports,hosts in zip(ports, resultMap):
    if hosts == True:
        print(args.host, "has", ports, "open!")
