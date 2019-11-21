import socket
import time
import pickle


img_len = 921764
i = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 1243))
s.listen(5)
clientsocket, address = s.accept()
data = b''
print("Connection from {} has been established.".format(address))
while True:
    while i < img_len:
        # now our endpoint knows about the OTHER endpoint.
        d = clientsocket.recv(1024)
        i += len(d)
        data +=d
    print("len",len(data))
    msg = pickle.loads(data)
    print(msg)
    data = pickle.dumps(msg)
    clientsocket.send(data)
    time.sleep(10)
    break