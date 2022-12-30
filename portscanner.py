import socket
import sys

addr = ""
port = ""
timeout = ""

class Portscanner:
    
    def getInputfrmcli():
        if sys.argv[0].isalpha() = True:
            addr = socket.gethostbyname(sys.argv[0])
        else:
            addr = sys.argv[0]
        port = sys.argv[1]
        timeout = sys.argv[2]
            
    
    def getInputinteractive():
        if sys.argv[0].isalpha() = True:
            addr = socket.gethostbyname(sys.argv[0])
        else:
            addr = sys.argv[0]
        port = input("[+] Port: ")
        timeout = input("[+] Timeout(s): ")
        
    
    def connect():
        if __name__ == "__main__":
            print(">> Initiating....")
            getInputinteractive()
            print(">>> Instantiating connection...")
            sock = socket.create_connection((addr,port))
            print("✓ Connected")
            socket.setdefaulttimeout(int(timeout)
        else:
            print(">> Initiating....")
            getInputfrmcli()
            print(">>> Instantiating connection...")
            sock = socket.create_connection((addr,port))
            print("✓ Connected")
            socket.setdefaulttimeout(int(timeout)
    def testconn():
        sock = connect()
        while sock = True:
            sock.send(b"TCK")
            sock.recv(1024).decode()
        else:
            pass
            
           

testconn()