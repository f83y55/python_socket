import socket

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    client, addr = s.accept()
    with client:
        print(f"Connected by {addr[0]}")
        while True:
            data = client.recv(1024)
            if data :
                print(data.decode())


