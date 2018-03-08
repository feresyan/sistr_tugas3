import zmq # Import library zmq
import time # Import library time

context = zmq.Context() #object zmq memanggil method konteks

sock = context.socket(zmq.PUSH) #Publisher memanggil method socket dan mendefinisikan socket yang digunakan adalah PUSH
sock.bind("tcp://127.0.0.1:5690")  # variabel sock memanggil method bind untuk menentukan port yang digunakan oleh server

id = 0 # men set variabel id bernilai 0

while True:
    time.sleep(1) #manager memmanggil method sleep dengan value 1
    id, now = id+1, time.ctime() #manager menyimpan waktu yang telah digenerate dari library pada sebuah variabel
    message = "{id} - {time}".format(id=id, time=now)  #manager menyiapakan pesan yang akan dikirimkan ke worker
    sock.send(message.encode()) #manager mengirimkan pesan ke worker
    print ("Sent: {msg}".format(msg=message)) #manager mencetak pesan yang dikirim