def printTop(stack):
	try:
		print (len(stack), stack[-1])
	except Exception:
		print ("Ой-ой! Стек пустой!")



stack=[]
while True:
	for token in input().split(' '):
		try:
			if token.isdigit():
				stack.append(int(token))
				printTop(stack)
				x=(stack.pop()+stack.pop())
				stack.append(x)
			if token == 'stack':
				print (stack)
		except IndexError:
			print ('4ota ne to')