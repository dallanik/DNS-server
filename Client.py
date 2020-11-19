import socket

PORT = 53
IP = 'localhost'
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    data = input(">")
    s.sendto(data.encode(), (IP, PORT))
    server_data, addr = s.recvfrom(1024)
    print(server_data.decode())
