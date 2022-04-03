import socket

class ClientSocket:
    
    def __init__(self, host_ip, port) -> None:
        self.host_ip = host_ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(( self.host_ip, self.port))
            
    def send_msg(self) -> None:
        self.s.sendall(b"Hello, world")
        data = self.s.recv(1024)
        print(f"Received {data!r}")
        self.s.close()