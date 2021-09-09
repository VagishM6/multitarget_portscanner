import socket
from IPy import IP


# function to perform scan on the target
def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(1, 500):
        scan_port(converted_ip, port)


# checking if the ip address is numeric, else converting the domain to ip address
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


# function to grab info of open ports
def get_banner(s):
    return s.recv(1024)


# function to scan the port
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        # try, except block to grab the service info from the open ports
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass


if __name__ == "__main__":
    # specifying the ipaddress
    targets = input('[+] Enter Target/s To Scan(split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)