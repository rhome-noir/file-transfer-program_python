import socket as skt

# create tcp server socket object that listens for a connection
server_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
server_socket.bind(('localhost', 12345)) # bind server and port
server_socket.listen(1) # listen for a connection request
print("File server started. Waiting for connection ...")

# let user know that the server is connected to a address
conn, addr = server_socket.accept() # conn = new socket object for communication | addr = the client's address
print(f"Connected by {addr}")

# recieve filename request
filename = conn.recv(1024).decode('utf-8') # read up to 1024 bytes and convert to a string
print(f"Client requested file: {filename}")

try:
    with open(filename, 'rb') as f: # open requested file in binary mode "rb"
        
        # read and send file in chunks of 1024 bytes
        chunk = f.read(1024)
        while chunk: # loop until file is fully read
            conn.sendall(chunk) 
            chunk = f.read(1024)
    print("File transfer complete")
except FileNotFoundError:
    conn.sendall(b'ERROR: File not found.')

# close connection 
conn.close()