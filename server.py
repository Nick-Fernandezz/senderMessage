import socket

# IP
# socket.AF_INET - IP4                                                               
# socket.AF_INET6 - IP6

# Connect protocol
# socket.SOCK_DGRAM - UDP
# socket.SOCK_STREAM - TCP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 8888)) # reserv adress 127.0.0.1 and port 8888 for listening
result = s.recv(1024) # listening port 8888 and input them 
print('Message:', result.decode('utf-8')) # print Message
s.close() # close connection



