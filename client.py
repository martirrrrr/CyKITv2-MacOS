
import socket

HOST = '127.0.0.1'  # Indirizzo del server (locale)
PORT = 3131
        # Deve essere la stessa porta usata dal server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print(f"Tentativo di connessione a {HOST} sulla porta {PORT}...")
    client.connect((HOST, PORT))
    print("Connessione stabilita!")

#    data = client.recv(1024)  # Riceve il messaggio dal server
#    print("Messaggio dal server:", data.decode())  # Mostra il messaggio ricevuto

except ConnectionRefusedError as e:
    print(f"Errore di connessione: {e}")
except Exception as e:
    print(f"Errore generico: {e}")
finally:
    client.close()
    print("Connessione chiusa.")
