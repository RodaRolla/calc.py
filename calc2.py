#!python
# coding: utf-8
def printTop(stack):
	try:
		print (len(stack), stack[-1])
	except: Exception
def multiplying(stack):
	stack.append(stack.pop()*stack.pop())

def addition(stack):
	stack.append(stack.pop()+stack.pop())

def subtraction(stack):
	stack.append(-stack.pop()+stack.pop())

def division(stack):
	try:
		stack.append((stack.pop()/stack.pop())**-1)
	except ZeroDivisionError:
		print('T_T')

ops={
	'+': addition,
	'-': subtraction,
	'*': multiplying,
	'/': division
}


stack=[]
while True:
	for token in input().split(' '):
		try:
			if token.isdigit():
				stack.append(int(token))
				printTop(stack)
			if token == 'stack':
				print (stack)
			continue
			
			if token in ops:
				ops[token](stack)
				printTop(stack)
		except IndexError:
			print ('4ota ne to')
