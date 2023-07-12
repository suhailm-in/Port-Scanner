from socket import *

def connection_Scan(targetHost, targetPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((targetHost, targetPort))
        print('[+]%d/tcp open'% targetPort)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% targetPort)

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] cannot resolve %s '% targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print('\n[+] Scan result of : %s ' % targetName[0])
    except:
        print('\n[+] Scan result of : %s ' % targetIP)
    setdefaulttimeout(1)
    for i in targetPorts:
        print('Scanning Port: %d' % i)
        connection_Scan(targetHost, int(i))

if __name__ == '__main__':
    ip_add = input("enter ip address : ")
    # port_add = input("Enter Ports (multiple numbers separated by spaces): ")
    port_list = [80, 443, 22, 21, 25, 53, 110, 143, 3389, 445]

    # port_add_split = port_add.split()
    # port_list = [int(num) for num in port_add_split]

    portScan(ip_add, port_list)


    # ip_add = input("enter ip address : ")
    # port_add = int(input("enter port number : "))
    # print(ip_add, port_add)

    # connection_Scan('142.250.71.14', 80)
    # connection_Scan(ip_add, port_add)

