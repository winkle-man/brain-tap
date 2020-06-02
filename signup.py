from sys import argv

script, username_check, password_check, email_check = argv

running = True
	
while running:
	new_user = input("Enter Desired Username: ")
	x = open(username_check).readlines()
	y = [wrong_name.replace('\n', '') for wrong_name in x]
	match = [True for name in y if new_user == name]
	if match:
		print("Username already exists..\n")
	else:
		if new_user == "":
			pass
		else:
			running = False


running1 = True

while running1:
	new_pw = input("Enter Desired Password: ")
	if new_pw == "":
		pass
	else:
		running1 = False


running2 = True

while running2:
	new_email = input("Enter email address: ")
	x = open(email_check).readlines()
	y = [address.replace('\n', '') for address in x]
	match = [True for email in y if new_email == email]
	if match:
		print("Email already registered..\n")
	else:
		if new_email == "":
			pass
		else:
			running2 = False

append_uname = open(username_check, 'a')
append_uname.write("\n" + new_user)
append_uname.close()


append_pw = open(password_check, 'a')
append_pw.write("\n" + new_pw)
append_pw.close()

append_email = open(email_check, 'a')
append_email.write("\n" + new_email)
append_email.close

print("Credentials registered\nThank you!")