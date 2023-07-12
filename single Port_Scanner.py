from socket import *

def connection_Scan(targetHost, targetPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((targetHost, targetPort))
        print('[+]%d/tcp open'% targetPort)
        connskt.close()
    except:
        print('[-]%d/tcp closed'% targetPort)


if __name__ == '__main__':
    connection_Scan('172.217.31.206',80)