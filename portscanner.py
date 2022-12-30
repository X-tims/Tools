import os
import socket
import Ipy
import sys
class Portscanner:
def __init__(self, sockettype, recvamt):
    self.sockettype = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    self.recvamt = 1024 * 1024

def getInputfrmcli(addr, port, timeout):
sys.args[0] = addr
sys.args[1] = port
sys.args[2] = timeout

def getInputinteractive(addr, port, timeout):
    addr = input("[+] Address: ")
    port = input("[+] Port: ")
    timeout = input("[+] Timeout(s): ")

def 