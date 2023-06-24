import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = None
        self.username = None

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        self.username = input("Enter your username: ")
        self.client_socket.send(self.username.encode('utf-8'))

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        while True:
            message = input()
            self.send_message(message)

    def receive_messages(self):
      while True:
          try:
              message = self.client_socket.recv(1024).decode('utf-8')
              print(message)
          except:
              print("Error receiving messages from the server.")
              self.client_socket.close()
              break


    def send_message(self, message):
        try:
            self.client_socket.send(message.encode('utf-8'))
        except:
            print("Error sending message to the server.")
            self.client_socket.close()

if __name__ == "__main__":
    client = ChatClient('localhost', 5555)
    client.start()
