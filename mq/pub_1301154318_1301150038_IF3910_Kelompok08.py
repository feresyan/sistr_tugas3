import zmq # Import library zmq
import time  # Import library time

context = zmq.Context() #object zmq memanggil method konteks

sock = context.socket(zmq.PUB)  #Publisher memanggil method socket dan mendefinisikan socket yang digunakan adalah publisher
sock.bind("tcp://192.168.0.23:1627") # varabel sock memanggil method bind untuk menentukan port yang digunakan oleh server

id = 0 # men set variabel id bernilai 0

while True:
    time.sleep(1) #publisher memmanggil method sleep dengan value 1
    id, now = id+1, time.ctime() #publisher menyimpan waktu yang telah digenerate dari library pada sebuah variabel

    message = "1-Update! >> #{id} >> {time}".format(id=id, time=now) #server menyiapakan pesan yang akan dikirimkan ke subscriber
    sock.send(message.encode('ascii')) #server mengirimkan pesan ke subscriber

    message = "2-Update! >> #{id} >> {time}".format(id=id, time=now) #server menyiapakan pesan yang akan dikirimkan ke subscriber
    sock.send(message.encode('ascii')) #server mengirimkan pesan ke subscriber

    id += 1 #value id ditambah 1