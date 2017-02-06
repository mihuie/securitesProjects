import socket
import os
import sys

def getBanner( ip, port):
    try:
        socket.setdefaulttimeout(5)
        s=socket.socket()
        s.connect((ip,port))
        s.send("hello is itt me youre looking for")
        banner = s.recv(512)
        print " Connected to: " + str(ip)+" "+" on port #"+" " + str(port)+ " "+ " is successful"
        print '\n'
        print str(banner)

    except:
        
        return " the connection was not made on the port"


def Check_Vulnerabilities(banner):
    # Write code that opens text-file and check line by line for banner here
  

def main():

    portList = [21, 22, 25, 80, 110, 443,3306]
    name=socket.gethostbyname(socket.gethostname())
    #print name

    print "-"*150
    print " Wecome to our Banner Grabbing Application"
    print "-"*150
    

    address=raw_input("Enter the ip or hostname of a remote host that you would like to scan example mona.uwi.edu: ")
    ip_add= socket.gethostbyname(address)
    new_add=ip_add.split(".")
    next_add= new_add[0]+"."+new_add[1]+"."+new_add[2]+"."

    print '\n'
    print " This is the IP address that willl be scanned as well as everything in the range up to 255......" +" "+ ip_add
    for x in range(0,256):
        for ports in portList:
            address=next_add+str(x)
            print "Scanning "+ address + " "+ "on port number "+ " "+ str(ports)
            getBanner(address, ports)
        
    

if __name__ == "__main__":
    main()







