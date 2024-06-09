import socket    #this module searches the local IP address of machine
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# connect() for UDP doesn't send packets
s.connect(('10.0.0.0', 0))
bbb=s.getsockname()[0]
print(bbb)