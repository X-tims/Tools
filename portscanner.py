import os
import socket
import Ipy
import sys

addr = ""
port = ""
timeout = ""

class Portscanner:
    def __init__(self, recvamt):
        self.recvamt = 1024 * 1024
    
    def getInputfrmcli(self):
        addr= sys.args[0]
        port = sys.args[1]
        timeout = sys.args[2]
    
    def getInputinteractive(self):
        addr = input("[+] Address: ")
        port = input("[+] Port: ")
        timeout = input("[+] Timeout(s): ")
    
    def connect(self):
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
    def testconn(self):
        sock = connect()
        while sock = True:
            sock.recv(int(self.recvamt))
        
        
        