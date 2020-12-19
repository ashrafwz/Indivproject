import random
import socket
import struct

from ipaddress import IPv4Network

s=socket.socket()
host = "192.168.0.4"
port = 8888

s.bind((host,port))

s.listen(4)
print("Waiting for connection")

while True:
	connection,address = s.accept()
	data = connection.recv(2048).decode()
	print (data)
	if data == "yes":
		ip=socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
		print (str(ip))
		new_ip = str(ip)
		ip1, ip2, ip3, ip4 = new_ip.split('.')
		data2 = int(connection.recv(2048).decode())
		
		if (data2 == 24):
			ip_addr= ip1+"."+ip2+"."+ip3+".0/"+str(data2)
		
		elif (data2 ==16):
			ip_addr= ip1+"."+ip2+".0.0/"+str(data2)

		elif (data2 ==8):
			ip_addr= ip1+".0.0.0/"+str(data2) 

		elif (data2 ==32):
			ip_addr= new_ip+"/"+str(data2)
		else : 
			print("invalid Prefix")
 
		net = IPv4Network(ip_addr)
		prx = net.prefixlen
		submask = net.netmask
		defgateway = net.network_address
		print (str(net))

		ip_add="Your IP Address =" + str(ip)
		info1= "Prefix = "+str(prx)
		info2= "Subnet mask=" + str(submask)
		info3= "Default gateway="+ str(defgateway)
		infoAll= ip_add+"\n"+info1+"\n"+info2+"\n"+info3+"\n"
		connection.send (str.encode(infoAll))

		print (infoAll)

connection.close()

s.close()

