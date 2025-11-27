import socket as skt

# create a tcp socket
client_socket = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
# connect to the file sender server
client_socket.connect(('localhost', 12345))

# step a request a file
filename = input("Enter filename to download: ") # user input for the filename
client_socket.sendall(filename.encode('utf-8')) # sends file to the server

# receive file data
with open(filename, 'wb') as f: # open a new file locally in binary write mode "wb"
    while True:
        data = client_socket.recv(1024) # recieves chunks of data from server
        if not data:
            break
        f.write(data) # the chunks get written into a file

# print confirmation and close close connection      
print('File received successfully.')
client_socket.close()
