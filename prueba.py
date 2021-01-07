PASSWORD = '12345'


def upper(func):
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)

		return result.upper()
	return wrapper

@upper
def say_my_name(name):
	return f'Hola, {name}'

def password_required(func):
	def wrapper():
		password = str(input('input the password'))

		if password == PASSWORD:
			return func()
		else:
			print('The password is NOT correct')
	return wrapper

@password_required
def needs_password():
	print('The password is correct')

if __name__ == '__main__':
	valor = say_my_name('Victor')
	print(valor)
	needs_password()
