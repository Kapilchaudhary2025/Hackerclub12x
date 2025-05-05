import socket
import os
import platform
from scapy.all import *

# Display banner
def display_banner():
    print("#############################################")
    print("#   Welcome to Hacker Club by Kapil         #")
    print("#############################################\n")

# Port scanner function
def scan_ports(host, start_port=1, end_port=1024):
    print(f"Scanning ports on {host} from {start_port} to {end_port}...")
    open_ports = []

    try:
        target_ip = socket.gethostbyname(host)
        print(f"Resolved {host} to {target_ip}")
    except socket.gaierror:
        print("Error: Unable to resolve host.")
        return []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open")
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    if open_ports:
        print(f"\nOpen ports on {host}: {open_ports}")
    else:
        print(f"\nNo open ports found on {host}.")
    return open_ports

# OS detection function
def detect_os(host):
    print(f"Detecting OS for {host}...")
    try:
        ans, unans = sr(IP(dst=host)/ICMP(), timeout=2, verbose=0)
        for snd, rcv in ans:
            os_info = platform.system() + " - " + platform.release()  # Mock OS detection
            print(f"OS detected for {host}: {os_info}")
            return os_info
    except Exception as e:
        print(f"Error detecting OS: {e}")
    return None

# Traceroute function
def perform_traceroute(host):
    print(f"Performing traceroute to {host}...")
    try:
        result, unans = sr(IP(dst=host, ttl=(1, 30))/ICMP(), timeout=2, verbose=0)
        for snd, rcv in result:
            print(f"{rcv.ttl} -> {rcv.src}")
    except Exception as e:
        print(f"Error performing traceroute: {e}")

# Help menu function
def display_help():
    print("Available Features:")
    features = [
        "1. Port Scanning",
        "2. OS Detection",
        "3. Traceroute"
    ]
    for feature in features:
        print(feature)

# Main function
def main():
    display_banner()
    display_help()
    
    choice = input("\nEnter the number of the feature you want to use: ")
    if choice == "1":
        target_host = input("Enter the target host (e.g., IP or domain): ")
        start_port = int(input("Enter the starting port (default: 1): ") or 1)
        end_port = int(input("Enter the ending port (default: 1024): ") or 1024)
        scan_ports(target_host, start_port, end_port)
    elif choice == "2":
        target_host = input("Enter the target host (e.g., IP or domain): ")
        detect_os(target_host)
    elif choice == "3":
        target_host = input("Enter the target host (e.g., IP or domain): ")
        perform_traceroute(target_host)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()