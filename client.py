import cv2
import io
import socket
import struct
import time
import pickle
import numpy as np
import socket
import sys
cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('35.222.185.180',1243))
while True:
    ret,frame=cap.read()
    data = pickle.dumps(frame) ### new code
    clientsocket.sendall(struct.pack("L", len(data))+data) ### new code
# cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     if key == 27: # exit on ESC
#         break
# cv2.destroyWindow("preview")

# client_socket = socket.socket()

# client_socket.connect(('', 8000))  # ADD IP HERE

# # Make a file-like object out of the connection
# connection = client_socket.makefile('wb')
# try:
#     camera = cv2.VideoCapture(0)
#     # Start a preview and let the camera warm up for 2 seconds
#     camera.start_preview()
#     time.sleep(2)

#     # Note the start time and construct a stream to hold image data
#     # temporarily (we could write it directly to connection but in this
#     # case we want to find out the size of each capture first to keep
#     # our protocol simple)
#     start = time.time()
#     stream = io.BytesIO()
#     if vc.isOpened(): # try to get the first frame
#         rval, frame = vc.read()
#     else:
#         rval = False
#     while rval:
#         cv2.imshow("preview", frame)
#         rval, frame = vc.read()
#         key = cv2.waitKey(20)
#         if key == 27: # exit on ESC
#             break
#     cv2.destroyWindow("preview")
#     for foo in camera.capture_continuous(stream, 'jpeg'):
#         # Write the length of the capture to the stream and flush to
#         # ensure it actually gets sent
#         connection.write(struct.pack('<L', stream.tell()))
#         connection.flush()
#         # Rewind the stream and send the image data over the wire
#         stream.seek(0)
#         connection.write(stream.read())
#         # If we've been capturing for more than 30 seconds, quit
#         if time.time() - start > 60:
#             break
#         # Reset the stream for the next capture
#         stream.seek(0)
#         stream.truncate()
#     # Write a length of zero to the stream to signal we're done
#     connection.write(struct.pack('<L', 0))
# finally:
#     connection.close()
#     client_socket.close()


# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("35.193.10.157",5006))
# # msg = s.recv(1024)
# # print(msg.decode("utf-8"))
# d = {1:"Hey",2:"There"}
# msg = pickle.dumps(d)
# msg = bytes(msg)

# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False

# while rval:
#     # cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     # if key == 27: # exit on ESC
#     #     break
#     s.send(bytes(frame))
# # cv2.destroyWindow("preview")
# import socket

# HOST = '35.193.10.157'  # The server's hostname or IP address
# PORT = 5006        # The port used by the server
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
# else:
#     rval = False


# # cv2.destroyWindow("preview")
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     # while rval:
#         # cv2.imshow("preview", frame)
#     rval, frame = vc.read()
#     key = cv2.waitKey(20)
#     # if key == 27: # exit on ESC
#     #     break
#     print(len(bytes(pickle.dumps(frame))))
#     s.send(bytes(pickle.dumps(frame),"utf-8"))
#     # s.sendall(b'Hello, world')
#         # data = s.recv(1024)
#     data = []
#     # while True:
#     data = s.recv(921764)
#         # if not packet: break
#         # data.append(packet)
#     print(data)
#     print(len(data))
#     data_arr = pickle.loads((data))
#     print (data_arr)

#     cv2.imshow("preview",data_arr)
#     cv2.destroyWindow("preview")

# print('Received', repr(data))
# import socket
# import pickle
# import cv2
# import time
# import numpy as np
# HEADERSIZE = 10
# import cv2
# import io
# import struct
# import zlib

# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # s.connect(("35.239.222.64", 1243))
# # # s.connect(("127.0.0.1", 1243))
# vc = cv2.VideoCapture(0)

# if vc.isOpened(): # try to get the first frame
#     rval, frame = vc.read()
#     # cv2.imshow("preview",frame)
# else:
#     rval = False
# # while rval:
    
# def sendImg():
#     rval, frame = vc.read()
#     msg = pickle.dumps(frame)
#     print("send len",len(msg))
#     s.sendall(pickle.dumps(frame))

# def getAnswer():
#     msg_len = 40
#     i = 0
#     data = b''
#     while i < msg_len:
#         # now our endpoint knows about the OTHER endpoint.
#         d = s.recv(1024)
#         # print(len(d),i)
#         i += len(d)
#         data +=d
#     print("len",len(data))
#     msg = pickle.loads(data)
#     print(msg)

# if __name__ == "__main__":
    
#     # print(start)
#     # while True:
#     #     start = time.time()
#     #     while time.time()< start+2:
#     #         sendImg()
#     #     while time.time()< start+2:
#     #         getAnswer()

#     HOST = '35.222.185.180'  # The server's hostname or IP address
#     PORT = 1243       # The port used by the server
    

#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((HOST, PORT))
#     connection = client_socket.makefile('wb')

#     cam = cv2.VideoCapture(0)

#     cam.set(3, 320);
#     cam.set(4, 240);

#     img_counter = 0

#     encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

#     while True:
#         ret, frame = cam.read()
#         result, frame = cv2.imencode('.jpg', frame, encode_param)
#     #    data = zlib.compress(pickle.dumps(frame, 0))
#         data = pickle.dumps(frame, 0)
#         size = len(data)


#         print("{}: {}".format(img_counter, size))
#         client_socket.sendall(struct.pack(">L", size) + data)
#         img_counter += 1

#     cam.release()
    # a=1024
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((HOST, PORT))
    #     while True:
    #         rval, frame = vc.read()
    #         frame_arr = np.array(frame).dumps()
    #         # frame_bytes = frame_arr.tostring()
    #         print(len(frame_arr))
    #         # print(len(frame_bytes))
    #         s.sendall(frame_arr)
            # data = s.recv(1024)
            # msg = pickle.loads(data)

            # print('Received', repr(msg))

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((HOST, PORT))
    #     while True:
    #         # s.sendall(b'Hello, world')
    #         # data = s.recv(1024)
    #         # msg = pickle.loads(data)
    #         # print('Received', msg)
    #         while True:
    #             rand = pickle.dumps(frame)
    #             s.sendall(rand)
                # time.sleep(5)

    #             # amount_expected=0
    #             # img_len = 921764
    #             # msg = b''
    #             # while amount_expected < img_len:
    #             #     data = s.recv(1024)
    #             #     amount_expected += len(data)
    #             #     msg += data

                
    #             # print(len(msg))
    #             # msg = pickle.loads(msg)
    #             # # print(data+i)
    #             # if not data:
    #             #     break
                