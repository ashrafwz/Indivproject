import socket

s = socket.socket()
host = "192.168.0.4"
port = 8888

s.connect((host, port))

input_req = input("\nRequest IP from Server? (yes/no) : ")

s.send(str.encode(input_req))

numhost= input("Please enter number of Prefix (8/16/24/32)= ") 

if (numhost== "8" or numhost=="16" or numhost=="24"or numhost=="32"):
	 
	s.send(str.encode(numhost))
else :
	print("Invalid Prefix")

reply = s.recv(1024).decode()

print(reply)




s.close()

