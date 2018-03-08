import zmq # Import library zmq

context = zmq.Context() #object zmq memanggil method konteks


print("Connecting to hello world server...") #client mencetak string yang sudah ditentukan
socket = context.socket(zmq.REQ) #variabel konteks memanggil method socket untuk membuat socket lalu disimpan ke dalam variabel
socket.connect("tcp://192.168.0.23:1627") #varabel socket memanggil method bind untuk menentukan port yang digunakan


for request in range(10):
    print("Sending request %s ..." % request) #client mencetak string yang sudah ditentukan sebanyak 10 kali
    socket.send(b"Hello") # bisa juga : socket.send("Hello".encode) #Client mengirimkan pesan sebanyak 10 kali ke server


    message = socket.recv() #Client menerima pesan dari server
    print("Received reply %s [ %s ]" % (request, message)) #client mencetak pesan dari server
