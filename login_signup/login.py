from sys import argv

script, username_check, password_check= argv

def check():
	x = open(username_check).readlines()
	y = [wrong_name.replace('\n', '') for wrong_name in x]
	match = [True for name in y if username == name]
	
	x1 = open(password_check).readlines()
	y1 = [wrong_pw.replace('\n', '') for wrong_pw in x1]
	match1 = [True for pw in y1 if password == pw]
	
	if match and match1:
		print("Login Successful")
	else:
		print("Login Failed: Username or Password is incorrect")

username = input("Username: ")
password = input("Password: ")
check()