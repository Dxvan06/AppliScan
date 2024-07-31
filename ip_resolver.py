import socket

def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.error:
        return None

