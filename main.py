import argparse
from port_scanner import scan_ports
from ip_resolver import resolve_ip
from service_detector import detect_services
from subdomain_enum import enumerate_subdomains
from dir_discovery import discover_directories

def main():
    parser = argparse.ArgumentParser(description="Web Application Scanning Tool")
    parser.add_argument("target", help="Target domain or IP address")
    parser.add_argument("--wordlist", help="Path to directory wordlist file", default="wordlist.txt")
    args = parser.parse_args()

    # Resolve IP
    ip = resolve_ip(args.target)
    if ip:
        print(f"Resolved IP: {ip}")

        # Scan Ports
        print("Scanning ports...")
        open_ports = scan_ports(ip)
        print(f"Open Ports: {open_ports}")

        # Detect Services
        print("Detecting services...")
        services = detect_services(ip)
        print(f"Services: {services}")

    else:
        print("Could not resolve IP.")

    # Enumerate Subdomains
    print("Enumerating subdomains...")
    subdomains = enumerate_subdomains(args.target)
    print(f"Subdomains: {subdomains}")

    # Discover Directories
    print("Discovering directories...")
    directories = discover_directories(f"http://{args.target}", args.wordlist)
    print(f"Found Directories: {directories}")

if __name__ == "__main__":
    main()
