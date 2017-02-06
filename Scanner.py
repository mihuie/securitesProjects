import socket
import os
import sys

def getBanner( ip, port):
    try:
        s=socket.socket()
        s.connect((ip,port))
        s.send("hello is it me youre looking for")
        banner = s.recv(512)
        print "\nConnected to: " + str(ip)+" "+" on port #"+" " + str(port)+ " "+ " is successful"
        print str(banner)

    except:
        
        return " the connection was not made on the port"
  

def main():

    portList = [21, 22, 25, 80, 110, 443]

    address=raw_input("Enter the ip or hostname that you would like to scan: ")
    ip_add= socket.gethostbyname(address)
    # print ip_add

    for port in portList:
    	getBanner(ip_add , port)
        


if __name__ == "__main__":
    main()







