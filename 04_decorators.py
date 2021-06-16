PASSWORD = "hello123"


def password_required(func):
	def wrapper():   # Por convención este es el nombre del a función interna
		password = input("What is the password? ")

		if password == PASSWORD:
			return func()
		else:
			print("The password is not correct")

	return wrapper

@password_required
def needs_password():
	print("The password is correct, welcome")


if __name__ == "__main__":
	needs_password()