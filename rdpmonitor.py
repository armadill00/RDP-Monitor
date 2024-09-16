import psutil
import socket
import time
from datetime import datetime

# Define the RDP port (default is 3389)
RDP_PORT = 3389

def check_rdp_connections():
    connections = psutil.net_connections()
    rdp_connections = []

    for conn in connections:
        if conn.laddr.port == RDP_PORT:
            rdp_connections.append(conn)
    
    return rdp_connections

def get_ip_info(ip):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return hostname
    except socket.herror:
        return "Unknown Host"

def monitor_rdp():
    print(f"Monitoring RDP port {RDP_PORT} for connection attempts...\n")
    
    while True:
        connections = check_rdp_connections()
        
        if connections:
            for conn in connections:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                remote_ip = conn.raddr.ip
                remote_port = conn.raddr.port
                hostname = get_ip_info(remote_ip)
                status = conn.status

                print(f"[{timestamp}] Connection attempt detected:")
                print(f"    Remote IP: {remote_ip}")
                print(f"    Hostname: {hostname}")
                print(f"    Remote Port: {remote_port}")
                print(f"    Status: {status}")
                print("-" * 40)
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    try:
        monitor_rdp()
    except KeyboardInterrupt:
        print("Monitoring stopped.")
