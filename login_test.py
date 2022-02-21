#Completing the code
#4 parts- Q1, Q2, Q3, Q4

class User:
	def __init__(self, username, password=None, phone=None):
		self.username = username
		self.password = password
		self.phone = phone
    
	def verify_password(self):
		pwd = input("Enter your password: ")
		if self.password == pwd:
			return True
		else:
			return False
    
	def make_password(self):
		while True:
			pwd = input("Enter password: ")
			again = input("Re-enter Password: ")
			if pwd == again:
				self.password = pwd
				print('Password updated!')
				break
			else:
				print("Passwords don't match!!")
				print("Try again!\n-New password-")

	def add_number(self):
		#Q3 done
		num = input('Enter your phone number: ')
		for x in num:
			if not x.isnumeric():
				print('Only numbers are allowed!!')
				print('-Please re-enter-')
				self.add_number()
			else:
				self.phone = num
				print('Number updated!')
    
	def change_password(self):
		#Q2 done
		print('-Current Password-')
		if self.verify_password():
			print('-New password-')
			self.make_password()
		else:
			print('Password not matching!!')
			choice = ('Do you want to try again? (y for yes): ')
			if choice.lower() == 'y':
				self.change_password()
    
	def change_username(self):
		#Q4 done
		if self.verify_password():
			new = input('Enter your new username: ')
			choice = input('Are you sure you want to keep this as your username? (y for yes): ')
			if choice.lower() == 'y':
				self.username = new
			else:
				choice = input('Do you want to re-enter a new username? (y for yes): ')
				if choice.lower() == 'y':
					self.change_username()
		else:
			print('Incorrect password!')

			
names = {"Shounak": User("Shounak"), "Prantika": User("Prantika")}

def add_user(username):
	#Q1 done
	reg=User(username)
	reg.make_password()
	names[username]=reg	

	
while True:
    name = input("\nInput Username (q to quit): ")
    if name.lower() == "q":
        break
    elif name in names.keys():
        user = names[name]
        if user.password is not None:
            if user.verify_password():
                print("Logged In!")
                if user.phone is None:
                    print("We don't have your phone number.")
                    print("Do you want to add it to your credentials?")
                    i = input("(y/n): ")
                    if i.lower() == "y":
                        user.add_number()
                while True:
                    print("Options:\n\t1. Logout\n\t2. Change Password\n\t3. Change Username")
                    opt = input("(1/2/3): ")
                    if opt == "1": # logout
                        break
                    elif opt == "2": # change pwd
                        user.change_password()
                    elif opt == "3": # change username
                        user.change_username()
                    else:
                        print("No Such Option!\nTry Again!")
            else:
                print("Invalid password!\nTry again")
        else:
            print("Make a password for your brand new account!")
            user.make_password()
    else:
        print("you are not a user")
        i = input("Make a new Account? (y/n):")
        if i.lower() == "y":
            add_user(name)
#print(names)
