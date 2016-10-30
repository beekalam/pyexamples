import argparse, socket
import sys
import os
from datetime import datetime
import struct
import time
MAX_BYTES = 4096
IP = ''
PORT = 1800
import time
# def server(port):
#     print port
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     # sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#     sock.bind((IP, port))
#     print('Listening at {}'.format(sock.getsockname()))
#     while True:
#         data, address = sock.recvfrom(MAX_BYTES)
#         try:
#             (code, id, length, authenticator) = struct.unpack("!BBH16s", data[0:20])
#             print data[20:]
#         except struct.error:
#             print  "Packet header is corrupt"
#
#         print "code: " + str(code)
#         print "id: " + str(id)
#         print "autheticator: " + str(authenticator)
#         print "address: " + str(address)
#         print time.ctime()
#
#     # print('The client at {} says {!r}'.format(address, text))
#     text = 'Your data was {} bytes long'.format(len(data))
#     print "=" * 80
#     #data = text.encode('ascii')
#     #sock.sendto(data, address)
#
#
# def client(port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     text = 'The time is {}'.format(datetime.now())
#     data = text.encode('ascii')
#     sock.sendto(data, (IP, port))
#     print('The OS assigned me the address {}'.format(sock.getsockname()))
#     data, address = sock.recvfrom(MAX_BYTES)  # Danger!
#     text = data.decode('ascii')
#     print('The server {} replied {!r}'.format(address, text))
#

if __name__ == '__main__':
    num = 1000
    l = []
    IP = '127.0.0.1'
    PORT = 18000
    for i in xrange(num):
        l.append(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
    for i in xrange(num):
        PORT += 1
        os.system("ss -s")
        time.sleep(0.1)
        time.sleep(0.1)
        l[i].bind((IP, PORT))