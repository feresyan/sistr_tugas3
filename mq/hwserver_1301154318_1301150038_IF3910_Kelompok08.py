import time # Import library time
import zmq # Import library zmq

context = zmq.Context() #object zmq memanggil method konteks
socket = context.socket(zmq.REP) #variabel konteks memanggil method socket untuk membuat socket lalu disimpan ke dalam variabel
socket.bind("tcp://*:5555") # varabel socket memanggil method bind untuk menentukan port yang digunakan

while True:

    message = socket.recv() #server menerima message dari client
    print("Received request: %s" % message) #server mencetak pesan

	# do some work
    time.sleep(1) #server memanggil method sleep dengan value 1


    socket.send(b"World") #server mengirim pesan client
