import socket                   # Import socket module

port = 8000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = ''     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(0)                     # Now wait for client connection.

print host
print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='requirements.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
    breakIId

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()