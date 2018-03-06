import zmq # Import library zmq

context = zmq.Context() #object zmq memanggil method konteks


sock = context.socket(zmq.SUB) #Publisher memanggil method socket dan mendefinisikan socket yang digunakan adalah subscriber


sock.setsockopt(zmq.SUBSCRIBE, b"1") #variabel sock memanggil method setsock
sock.connect("tcp://127.0.0.1:5680") #Subscriber melakukan koneksi ke port yang digunakan oleh publisher

while True:
    handle = open("tes_client.txt","wb")
    # sock.recv(handle.write())
    file = sock.recv()
    print(file)
    # handle.write(sock.recv())
    # message= sock.recv() #Subscriber menerima pesan dari publisher
    # print (message) #Client mencetak pesan dari publisher