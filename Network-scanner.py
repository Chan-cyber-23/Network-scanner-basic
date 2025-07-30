import socket
import ipaddress

def scan_ip(ip):
    try:
        socket.setdefaulttimeout(0.5)
        s = socket.socket()
        s.connect((str(ip), 80))
        return True
    except:
        return False

# Enter the network range you want to scan
network = ipaddress.ip_network("192.168.1.0/30", strict=False)

print("Scanning network...")

for ip in network.hosts():
    if scan_ip(ip):
        print(f"[+] Host is up: {ip}")
    else:
        print(f"[-] Host is down: {ip}")
