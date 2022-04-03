import socket

class ServerSocket:
    
    def __init__(self, host_ip, port) -> None:
        self.host_ip = host_ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host_ip, self.port))
        self.s.listen()
        self.conn, self.addr = self.s.accept()
            
    def receive_msg(self) -> None:
        with self.conn:
            print(f"connected by {self.addr}")
            while True:
                data = self.conn.recv(1024)
                print(f"The received message server side is {data}")
                self.conn.sendall(data)
                if data == b"stop now":
                    self.s.close()
                    break