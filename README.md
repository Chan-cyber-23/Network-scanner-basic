# Network Scanner - Beginner Python Project

This Python script scans a range of IP addresses and checks which hosts are active on port 80 using sockets.

## Features
- Uses `ipaddress` and `socket` modules
- Scans a subnet like 192.168.1.0/30
- Fast and beginner-friendly

## How It Works
1. You specify the IP range (e.g., `192.168.1.0/30`)
2. Script tries to connect to each IP on port 80
3. It reports which hosts respond (are up)

## Use Cases
- Small home network scanning
- Understanding IP ranges and host status
