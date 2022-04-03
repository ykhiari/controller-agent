import socket

class ClientSocket:
    
    def __init__(self, host_ip, port) -> None:
        self.host_ip = host_ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(( self.host_ip, self.port))
            
    def send_msg(self, msg) -> None:
        message = bytes(msg,'utf8')
        self.s.send(message)
        data = self.s.recv(1024)
        print(f"Received {data!r}")