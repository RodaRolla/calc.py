#!/usr/bin/python
## -*- coding: utf-8 -*-

def parseToken(ls):
	# num
	# symbol
	b=e=0 # Begin/End
	r=[]  # return
	while b<len(ls):
		e=b+1
		#print("%d:%d=%s" % (b,e,ls[b:e]))
		if ls[b:e].isdigit():
			# парсим число
			while ls[b:e].isdigit():
				if e>=len(ls):
					break;
				e+=1
			else:
				e-=1
		#print ("token [%d:%d] %s" % (b,e,ls[b:e]))
		r.append(ls[b:e])
		b=e
	#print ("res %s" % r)
	return r

op = {
	'+': lambda a,b:a+b,
	'-': lambda a,b:a-b,
	'*': lambda a,b:a*b,
	'/': lambda a,b:a/b
}

#op = {
#	'+': 'plus',
#	'-': 'minus',
#	'*': 'mul',
#	'/': 'div'
#}

imp = {
	'+': 0,
	'-': 0,
	'*': 1,
	'/': 1
}

# возвращает
# (op,a1,a2,tail,sign)
def tupler(tup,ls):
	if ls==[]:
		#print("конец")
		return tup
	#print("tup=%s ls=%s" % (tup,ls))
	t=ls[0]
	if t.isdigit():
		# начали с числа
		if len(ls)>3 and imp[ls[1]]<imp[ls[3]]:
			# далее более важная операция
			x=int(t)
			t=ls[1]
			#print("v1:1 (%s %d tupler(%s,%s))" % (t,x, tup,ls[2:]))
			y=tupler(tup,ls[2:])
			(o,a,b,l,s)=y
			#print("v1:2 (%s %d %s)" % (t,x, y))
			return tupler((op[t],x,y,ls[2:],t),l)
		else:
			if len(ls)>3 and imp[ls[1]]>imp[ls[3]]:
				# далее менее важная
				x=int(t)
				t=ls[1]
				y=int(ls[2])
				if isinstance(tup, tuple):
					(o,a,b,l,s)=tup
					#print("v2x (%s %d %d)" % (t,x, y))
					return (op[t], x ,y, ls[3:],t)
				else:
					return tupler((op[t], x ,y, ls[3:],t),ls[3:])
			else:
				# далее такая же
				x=int(t)
				t=ls[1]
				y=int(ls[2])
				#print("v2 (%s %d %d)" % (t,x, y))
				return tupler((op[t],x,y,ls[3:],t),ls[3:])
	if t in op:
		# начали с операции, значит первый операнд - кортеж, а второй таки число
		if len(ls)>3 and imp[ls[0]]<imp[ls[2]]:
			# нет, там кортеж
			x=tup
			#print("v3:1 (%s %s tupler(%s,%s))" % (t,x, tup,ls[1:]))
			y=tupler(tup,ls[1:])
			#print("v3:2 (%s %s %s)" % (t,x, y))
			return (op[t],x,y,ls[1:],t)
		else:
			x=tup
			y=int(ls[1])
			#print("v4 (%s %s %d)" % (t, x, y))
			return tupler((op[t],x,y,ls[2:],t),ls[2:])

def result(f):
	(op,a1,a2,lx,t)=f
	#print f
	#print a1
	#print a2
	if isinstance(a1, tuple):
		#print a1
		a1=result(a1)
	if isinstance(a2, tuple):
		#print a2
		a2=result(a2)
	#print "a1 %d" % a1
	#print "a2 %d" % a2
	r=op(a1,a2)
	#print "r %d" % r
	return r

def printFormula(f):
	(op,a1,a2,lx,t)=f
	s="("+t+" "
	if isinstance(a1, tuple):
		a1=printFormula(a1)
	s=s+str(a1)+" "
	if isinstance(a2, tuple):
		a2=printFormula(a2)
	s=s+str(a2)+")"
	return s

tup=None
try:
	while True:
		print ("Пиши код: ")
		formula=tupler(tup,parseToken(raw_input()))
		print printFormula(formula)
		print ("Результат=%d" % result(formula))
except (KeyboardInterrupt,EOFError):
	print "всего хорошего!"
	exit(0)
