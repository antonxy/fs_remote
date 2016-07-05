#!/usr/bin/env python2
import socket
outSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
outSock.connect(("127.0.0.1", 3332))
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 4242))
serversocket.listen(5)
while 1:
    print "waiting for connection"
    (clientsocket, address) = serversocket.accept()
    print "got connection"
    while 1:
        try:
            read = clientsocket.recv(1024)
        except Exception as e:
            print "Could not read from socket"
            print e
            break
        if read == '':
            print "lost connection"
            break
        print "read: " + read
        splitted = read.split("\n")
        print splitted
        for line in splitted:
            try:
                num = int(line)
            except ValueError:
                print "Could not parse line: " + line
            else:
                print "Got number " + str(num)
                if num < 1 or num > 20:
                    print "invalid cue number"
                outStrBase = "FSOC" + str(504 + num)
                outStr = outStrBase + "255\n" + outStrBase + "000\n"
                outSock.send(outStr)
            
