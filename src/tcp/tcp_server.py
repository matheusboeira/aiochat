import datetime
import socket
import threading
import time 

from termcolor import colored

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = {}
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Servidor iniciado em {}:{}".format(self.host, self.port))

        while True:
            client_socket, client_address = self.server_socket.accept()
            formatted_message = colored("{} conectou-se ao chat.".format(client_address), "grey")
            print(formatted_message)
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def broadcast(self, message, sender_socket):
      username = self.clients[sender_socket]
      for client_socket, client_username in self.clients.items():
          if client_socket != sender_socket:
              time = str(datetime.datetime.now().strftime('%H:%M:%S'))
              formatted_message = colored("{} <> {}: {}".format(time, username, message), "yellow")
              client_socket.send(formatted_message.encode('utf-8'))

    def handle_client(self, client_socket):
        username = client_socket.recv(1024).decode('utf-8')
        self.clients[client_socket] = username

        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    time = str(datetime.datetime.now().strftime('%H:%M:%S'))
                    formatted_message = colored("{} <> {}: {}".format(time, username, message), "yellow")
                    print(formatted_message)  
                    self.broadcast(message, client_socket)
                else:
                    self.remove_client(client_socket)
                    break
            except:
                self.remove_client(client_socket)
                break

    def remove_client(self, client_socket):
        if client_socket in self.clients:
            username = self.clients[client_socket]
            del self.clients[client_socket]
            client_socket.close()
            self.broadcast("{} desconectou-se.".format(username), None)

if __name__ == "__main__":
    server = ChatServer('localhost', 5555)
    server.start()
