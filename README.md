## RDP Port Connection Monitor
This Python script monitors your system's Remote Desktop Protocol (RDP) port (default: 3389) for any incoming connection attempts. It logs the IP address, hostname, remote port, and connection status for each detected connection, providing real-time feedback.

## Features
* RDP Monitoring: Continuously monitors the RDP port for connection attempts.
* IP and Hostname Lookup: Resolves the hostname from the IP address of the connecting client.
* Real-Time Logs: Displays connection details such as timestamp, remote IP, hostname, and status in real-time.
* Cross-Platform: Works on Windows, Linux, and macOS with the psutil library.

## Requirements
* Python 3.x
* psutil library

Monitoring RDP port 3389 for connection attempts...

[2024-09-16 12:34:56] Connection attempt detected:
    Remote IP: 192.168.1.100
    Hostname: client.example.com
    Remote Port: 51512
    Status: ESTABLISHED
----------------------------------------
