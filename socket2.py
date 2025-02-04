import socket

class Server:
    def __init__(self, port=55555):
        self.port = port

    def Connect(self):
        print("* Connecting . . .")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', self.port))
        sock.listen(1)  # Aspetta solo una connessione per test
        print(f"Server in ascolto sulla porta {self.port}")

        conn, addr = sock.accept()
        print(f"Connessione ricevuta da {addr}")

        conn.sendall(b"Hello, client!")
        conn.close()

# Avvia il server
server = Server()
server.Connect()
