import socket
import sys




addr = ""
port = 8080
timeout = ""
    
class Portscanner: 
    def getInputinteractive():
        addrs = input("[+] Address: ")
        if addrs.isalpha == True:
        	addr = socket.gethostbyname(addrs)
        else:
        	addr = addrs
       # port = int(input("[+] Port: "))
        timeout = input("[+] Timeout(s): ")

    def connect():
            print(">> Initiating....")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            
            Portscanner.getInputinteractive()
            print(">>> Instantiating connection...")
            print(port)
            sock.connect((addr, port))
            print("✓ Connected")
            socket.setdefaulttimeout(int(timeout))
            
Portscanner.connect()