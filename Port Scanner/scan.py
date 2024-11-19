import socket

def port_scan(target, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

target = '192.168.1.1'
ports = [21, 22, 80, 443]
port_scan(target, ports)
