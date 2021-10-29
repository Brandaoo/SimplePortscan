import socket
import pyfiglet




ascii_banner = pyfiglet.figlet_format("Portscan")
print(ascii_banner)


ip = input("ip adress: ")

for port in range(1, 65535):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.2)

	if s.connect_ex((ip,port)) ==0:


		print(ip, "====>" , port, "is open")
