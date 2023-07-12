from socket import *
from datetime import datetime
from os import makedirs
from os.path import exists, join


def connection_Scan(targetHost, targetPort, serviceName):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((targetHost, targetPort))
        result = '{:<8}  {: <8}    {}'.format(targetPort, 'open', serviceName)
        connskt.close()
    except:
        result = '{:<8}  {: <8}    {}'.format(targetPort, 'filtered', serviceName)
    return result


def portScan(targetIP, portFile):
    try:
        targetHost = gethostbyaddr(targetIP)[0]
    except:
        print('[-] cannot resolve IP address: {}'.format(targetIP))
        return

    scan_date = datetime.now().strftime('%Y-%m-%d')
    scan_time = datetime.now().strftime('%H-%M-%S')
    scan_dir = 'PortScan_result'
    makedirs(scan_dir, exist_ok=True)
    filename = get_unique_filename(scan_dir, 'scan', scan_date)
    output = ""

    output += '-' * 60 + '\n'
    output += '{:^60}\n'.format('Port Scan Results')
    output += '-' * 60 + '\n\n'
    output += 'Scan Date: {}\n'.format(scan_date)
    output += 'Scan Time: {} UTC\n\n'.format(scan_time)
    output += 'Host: {}\n'.format(targetHost)
    output += 'IP Address: {}\n\n'.format(targetIP)
    output += '-' * 60 + '\n\n'
    output += 'Status: Host is up\n'
    output += 'Latency: {}s\n\n'.format(getLatency(targetHost))
    output += 'Starting port scan for {}...\n\n'.format(targetHost)
    output += '{: <8}  {: <8}    {}\n'.format('PORT', 'STATE', 'SERVICE')

    setdefaulttimeout(1)
    try:
        with open(portFile, 'r') as portf:
            for line in portf:
                port, service = line.strip().split(',')
                result = connection_Scan(targetHost, int(port), service.strip())
                output += result + '\n'
    except FileNotFoundError:
        print('[-] Port list file not found: {}'.format(portFile))

    output += '\nPortScan complete for {}.\n'.format(targetHost)

    print(output)

    with open(filename, 'w') as f:
        f.write(output)

    print('PortScan is done: 1 IP address (1 host up) scanned in {} seconds.'.format(getLatency(targetHost)))
    print('Results saved to file: {}'.format(filename))


def getLatency(targetHost):
    try:
        start_time = datetime.now()
        _ = socket(AF_INET, SOCK_STREAM).connect_ex((targetHost, 80))
        end_time = datetime.now()
        latency = (end_time - start_time).total_seconds()
        return round(latency, 3)
    except:
        return 'unknown'


def get_unique_filename(directory, base_filename, scan_date):
    count = 1
    while True:
        filename = join(directory, '{}_{}_{}.txt'.format(base_filename, scan_date, count))
        if not exists(filename):
            return filename
        count += 1


if __name__ == '__main__':
    ip_add = input("Enter the IP address to scan: ")
    port_file = "ports.txt"

    try:
        targetIP = gethostbyname(ip_add)
    except:
        print('[-] cannot resolve IP address: {}'.format(ip_add))
    else:
        portScan(targetIP, port_file)
