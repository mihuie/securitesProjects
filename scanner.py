from socket import *
import os, signal, re


def handler(signum, frame):
    raise KeyboardInterrupt

signal.signal(signal.SIGALRM, handler)

common_ports = {
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "67": "DHCP",
    "80": "HTTP",
    "110": "POP3",
    "143": "IMAP",
    "194": "IRC",
    "443": "HTTPS",
    "465": "Cisco Protocol",
    "993": "IMAPS",
    "995": "POP3S",
    "3306": "MySQL",
    "7001": "weblogic",
    "8080": "tomcat/WDCP",
    "8089": "jboss",
    "8128": "squid",
    "25565": "Minecraft",
    "27017": "mongodb",
    "28017": "mongodb",
    "10000": "virtualmin/webmin"
}

def Banner(targetHost, targetPort):
    try:
        signal.alarm(15)
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((targetHost, int(targetPort)))
        conn.settimeout(10)

        try:
            banner = conn.recv(1024)
            print ""
        except:
            conn.send("HEAD / HTTP/1.0\r\n\r\n")
            banner = conn.recv(1024)

        return banner
    except:
        raise Exception('err')
    finally:
        conn.close()
        signal.alarm(0)

def scan(targetHost, targetPort):
    try:
        banner = str(Banner(targetHost, targetPort))
        if str(targetPort) in common_ports:
            print("Port {}({}) is OPEN!".format(str(targetPort), common_ports[str(targetPort)]))
        else: 
            print("{} is OPEN!".format(targetPort))
        print banner, 

        vList = open('list_vuln.txt', 'r')
        temp = re.findall(r"[a-zA-Z]+", banner)
        temp = [ x.lower() for x in temp ]

        for line in vList.readlines():
            vuln_app = line.strip('\n')
            vuln_app = vuln_app.strip(' ')

            if(vuln_app.lower() in temp):
                print "{} is vulnerable\n".format(vuln_app)
        vList.close()
            
    except:
        if str(targetPort) in common_ports:
            print("Port {}({}) is CLOSED!".format(str(targetPort), common_ports[str(targetPort)]))
        else:
            print("Port {} is CLOSED!".format(targetPort))
    
    return

def scanPort(targetHost, targetPorts):

    print "\n"
    print "*" * 40
    print "scan result for: " + targetHost
    print "*" * 40

    for port in targetPorts:
        scan(targetHost, port)

    return

def main():
    Host = raw_input(
        "\nEnter a remote host to scan or a range of host\n[Example => 192.168.56.101 or 192.168.56.101-223]: ")
    targetPort = raw_input(
        "\nEnter a port or list of ports to scan or \n'all' to scan default list of ports[Example => 22, 23, 80]: ")

    targetPort = str(targetPort).strip(' ')
    Host = str(Host).strip(' ')

    if targetPort is None:
        print "port can't be empty!"
        return
    elif targetPort.lower() == 'all':
        ports = common_ports.keys()
    elif "," in targetPort:
        ports = targetPort.split(",")
    else:
        ports = [targetPort]

    if "-" not in str(Host):
        scanPort(Host, ports)
    elif "-" in str(Host) and str(Host).count("-") == 1:
        initalHost = str(Host).split('-')[0]
        start = int(initalHost.split('.')[-1:][0])
        stop = int(str(Host).split('-')[1])
        head = initalHost.split('.')[:-1]

        for x in range(start, stop+1):
            temp = head + [str(x)]
            target = ('.').join(temp)
            temp = []

            scanPort(target, ports)

    print "\n\n"

if __name__ == '__main__':
    main()
