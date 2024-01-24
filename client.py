import socket

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connection on {HOST}:{PORT}")
    encore = ""
    while encore.upper() != "N" :
        message = input("Message à envoyer : ").encode()
        s.send(message)
        encore = input("Continuer ? (N:stop) ")

