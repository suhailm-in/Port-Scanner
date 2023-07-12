from socket import *

def connection_Scan(targetHost, targetPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((targetHost, targetPort))
        connskt.close()
        return True
    except:
        return False

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] Cannot resolve %s' % targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print('\nScan result for: %s' % targetName[0])
    except:
        print('\nScan result for: %s' % targetIP)
    print("\nPORT\tSTATE")
    for port in targetPorts:
        if connection_Scan(targetHost, port):
            print("%-10sopen" % port)

if __name__ == '__main__':
    ip_add = input("Enter IP address: ")
    port_list = [80, 443, 22, 21, 25, 53, 110, 143, 3389, 445]
    portScan(ip_add, port_list)
