#!python
# coding: utf-8

while True:
	try:
		print ('введите значение первого числа')
		x=float(input())
		print ('введите значение второго числа')
		y=float(input())
		print ('выберите действие')
		n=str(input())
	except KeyboardInterrupt:
		print("Oops!")
		exit(0)
	if n=='*':
		print (x*y)
	if n=='+':
		print(x+y)
	if n=='/':
		try:
			print(x/y)
		except ZeroDivisionError:
			print("Ayayaya")
	if n=='-':
		print (x-y)
