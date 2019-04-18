import socket

HOST = "127.0.0.1" #server IP address
PORT = 65432		# Port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #create socket

	s.connect((HOST, PORT)) #connect to host

	print('Client sending data')
	s.sendall(b'Hello, world') #send data

	print('Client receiving data')
	data = s.recv(1024)

print('Received', repr(data))
