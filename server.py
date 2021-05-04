"""
TCP - Протокол передачи данных который гарантирует получение пакетов на стороне клиента
UDP - Протокол передачи данных который не гарантирует получение пакетов на стороне клиента
"""
import socket
import threading

connections = []
HOST = 'localhost'
PORT = 9000
server = socket.socket()


def notify_users(sock, data):
    for client in connections:
        if client != sock:
            client.send(data)


def broadcast(sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                notify_users(sock, data)
        except Exception as e:
            print(e)
            break


def new_client():
    while True:
        sock, addr = server.accept()
        connections.append(sock)
        client = threading.Thread(target=broadcast, args=[sock])
        client.start()


def main():
    server.bind((HOST, PORT))
    server.listen(1)
    print('Сервер запущен!')
    thread = threading.Thread(target=new_client)
    thread.start()


if __name__ == '__main__':
    main()

"""
ONLINE = []

Маша +1

ONLINE = [Маша]
Петя +1
ONLINE = [Петя, Маша]
Маша > Привет

for пользователь in ONLINE:
    if пользователь != Маша:
        пользователь.отправить(Привет)
"""

