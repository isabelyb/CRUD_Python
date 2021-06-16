
your_name = input("What is your name? ")


def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)

		return result.upper()

	return wrapper


@upper
def say_your_name(name):
	return f"Hola, {name}"


if __name__ == '__main__':
	print (say_your_name(your_name))