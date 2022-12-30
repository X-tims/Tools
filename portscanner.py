import os
import socket
import Ipy
import sys
class Portscanner:
def __init__(self, sockettype, recvamt):
self.sockettype = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto = 0)
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
        getInputinteractive()