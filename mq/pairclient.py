import zmq # Import library zmq
import random # Import library random
import sys # Import library system
import time # Import library time

context = zmq.Context() #object zmq memanggil method konteks lalu menyimpannya ke variabel context
socket = context.socket(zmq.PAIR) #Client memanggil method socket dan mendefinisikan socket yang digunakan adalah pair
socket.connect("tcp://localhost:5556") #client melakukan koneksi ke port yang digunakan oleh server

while True:
    msg = socket.recv() #Client menerima pesan dari server
    print (msg)  # client mencteak pesan dari server
    socket.send("client message 1 to server".encode()) #client mengirimkan pesan ke server
    socket.send("client message 2 to server".encode()) #client mengirimkan pesan ke server
    time.sleep(1) #server memanggil method sleep dengan value 1