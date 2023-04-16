def double(func):
	def inner():
		func()
		print("Let's try that again!")
		func()
	return inner
