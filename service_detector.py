import nmap

def detect_services(target_ip):
    nm = nmap.PortScanner()
    nm.scan(target_ip, arguments='-sV')
    return nm.csv()
