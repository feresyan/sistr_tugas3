import zmq # Import library zmq

context = zmq.Context() #object zmq memanggil method konteks


sock = context.socket(zmq.SUB) #Publisher memanggil method socket dan mendefinisikan socket yang digunakan adalah subscriber


sock.setsockopt(zmq.SUBSCRIBE, b"2") #variabel sock memanggil method setsock
sock.connect("tcp://192.168.0.23:1627") #Subscriber melakukan koneksi ke port yang digunakan oleh publisher

while True:
    message= sock.recv() #Subscriber menerima pesan dari publisher
    print (message) #Client mencetak pesan dari publisher