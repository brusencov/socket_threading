import socket
import threading

HOST = 'localhost'
PORT = 9000
sock = socket.socket()


def sender(name):
    while True:
        msg = input('Введите сообщение > ')
        sock.send(f'{name}: {msg}'.encode())


def receiver():
    while True:
        data = sock.recv(1024)
        print(data.decode())


def main():
    name = input('Введите имя: ')
    sock.connect((HOST, PORT))
    print('Соединение прошло успешно!')

    send = threading.Thread(target=sender, args=[name])
    send.start()

    receive = threading.Thread(target=receiver)
    receive.start()


if __name__ == '__main__':
    main()
