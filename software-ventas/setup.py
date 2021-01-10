from setuptools import setup

setup(
	name='sv',
	version='0.1',
	py_modules=['sv'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		sv=sv:cli
	''',
)

# pip3 install editable . comando usado para instalar el programa