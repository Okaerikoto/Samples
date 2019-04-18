import socket

#Socket server that sends back the data received by the client to the client on the same computer
#Source du tuto https://realpython.com/python-sockets/#background 18/04/2019

HOST = '127.0.0.1' #loopback interface address / localhost
PORT = 65432 #Port to listen on (port <1023 are priviledged)

#AF_INET is the Internet address family for IPv4
#SOCK_STREAM is the socket type for TCP

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
#"with" will handle the closing of the socket instead of using try: except: finally:
#finally: is executed after a try, whether an exception occured or not so socket.close() is usually called in a finally:
		s.bind((HOST, PORT)) # Here, s.bind expects a pair (2-tuple) of host and port because we specified 
		s.listen() # opens the socket to connection
		conn, addr = s.accept() # This call is blocking until a client gets connected 
		#conn is a new socket to exchange the data
		with conn:
			print('Host was connected by', addr)
			while True:
				data = conn.recv(1024)
				print('Host received ', data)
				if not data:
					break
				conn.sendall(data)
