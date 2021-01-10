
def test_valor_arg(n_arg, *args):
	print('primer valor normal: ', n_arg)

	for arg in args:
		print('este es un valor de *args: ', arg)

	print(n_arg)
	print(args)
	print(type(args))

def test_valor_kwargs(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.items():
			print('%s == %s' %(key, value))

		print(type(kwargs))

def test_valor_kwargs_args(*args, **kwargs):
	print(type(kwargs))
	print(kwargs)
	print('--------------')
	print(type(args))
	print(args)

if __name__ == '__main__':
	# test_valor_arg('victor','reynaldo','julian','ricardo')
	# test_valor_arg(['victor','reynaldo','julian','ricardo'])
	# test_valor_kwargs(cartoon='batman')
	test_valor_kwargs_args('flash', 'batman', cartoon='batman', company='dc_comics')