import zmq # Import library zmq
import time  # Import library time

context = zmq.Context() #object zmq memanggil method konteks

sock = context.socket(zmq.PUB)  #Publisher memanggil method socket dan mendefinisikan socket yang digunakan adalah publisher
sock.bind("tcp://127.0.0.1:5680") # varabel sock memanggil method bind untuk menentukan port yang digunakan oleh server

id = 0 # men set variabel id bernilai 0

while True:
    time.sleep(1) #publisher memmanggil method sleep dengan value 1
    handle = open("tes.txt","r")
    print(sock.send_string(handle.read())) #server mengirimkan pesan ke subscriber


