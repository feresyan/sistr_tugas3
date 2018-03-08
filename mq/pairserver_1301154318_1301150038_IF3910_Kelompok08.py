import zmq # Import library zmq
import random # Import library random
import sys # Import library system
import time # Import library time

context = zmq.Context() #object zmq memanggil method konteks lalu menyimpannya ke variabel context
socket = context.socket(zmq.PAIR) #Server memanggil method socket dan mendefinisikan socket yang digunakan adalah pair
socket.bind("tcp://*:5556") # varabel sock memanggil method bind untuk menentukan port yang digunakan oleh server

while True:
    socket.send("Server message to client".encode()) #server mengirimkan pesan ke client
    msg = socket.recv() #server menerima pesan dari client
    print (msg) # server mencteak pesan dari client
    time.sleep(1) #server memanggil method sleep dengan value 1
 