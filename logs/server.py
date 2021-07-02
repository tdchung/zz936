'''
Server code from loguru.readthedocs.io
Use to test network logging
'''

import socketserver
import pickle
import struct
import json

from loguru import logger

PORT = 5000 #Make sure to set the same port defined in logging template


class LoggingStreamHandler(socketserver.StreamRequestHandler):

    def handle(self):
        while True:
            chunk = self.connection.recv(4)
            if len(chunk) < 4:
                break
            slen = struct.unpack('>L', chunk)[0]
            chunk = self.connection.recv(slen)
            while len(chunk) < slen:
                chunk = chunk + self.connection.recv(slen - len(chunk))
            record = pickle.loads(chunk)
            #print(json.loads(record['msg']))
            level, message = record["levelname"], json.loads(record["msg"])['text']
            logger.patch(lambda record: record.update(record)).log(level, message)

server = socketserver.TCPServer(('localhost', PORT), LoggingStreamHandler)
server.serve_forever()