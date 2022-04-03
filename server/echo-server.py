import socket
import json
from os import environ
from server_socket import ServerSocket

config_file_path = environ["CONFIG_FILE"]

with open(config_file_path,"r") as jsonfile:
    config = json.load(jsonfile)

srv_socket = ServerSocket(config["server_listner"],config["port"])
srv_socket.receive_msg()