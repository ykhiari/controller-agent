import socket
import json
from os import environ
from client_socket import ClientSocket

config_file_path = environ["CONFIG_FILE"]

with open(config_file_path,"r") as jsonfile:
    config = json.load(jsonfile)

clt_socket = ClientSocket(config["server_ip"],config["port"])
clt_socket.send_msg()