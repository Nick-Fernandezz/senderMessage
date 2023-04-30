import socket

# IP
# socket.AF_INET - IP4
# socket.AF_INET6 - IP6

# Connect protocol
# socket.SOCK_DGRAM - UDP
# socket.SOCK_STREAM - TCP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto(b'message for you', ('127.0.0.1', 8888))