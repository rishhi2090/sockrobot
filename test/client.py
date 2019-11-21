import socket
import pickle
import cv2

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("34.70.118.65", 1243))

msg = "test"

while True:
    s.sendall(pickle.dumps(msg+i))