import zmq # Import library zmq

context = zmq.Context() #object zmq memanggil method konteks


sock = context.socket(zmq.PULL) #worker memanggil method socket dan mendefinisikan socket yang digunakan adalah PULL
sock.connect("tcp://192.168.0.23:1627") #worker melakukan koneksi ke port yang digunakan oleh manager

while True:
    message = sock.recv() #Worker menerima pesan dari manager
    print ("Received: {msg}".format(msg=message)) #Worker mencetak pesan yang diterima oleh manager