#!/usr/bin/env python3

import socket

from proxy_server import BUFFER_SIZE

HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    # create socket, connect, and recieve data
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    connect(('127.0.0.1', 8001))

if __name__ == "__main__":
    main()