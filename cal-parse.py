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
	'+':"плюс",
	'-':"минус",
	'*':"умножить",
	'/':"разделить"
}

def tupler(tup,ls):
	if ls==[]:
		print("конец")
		return tup
	print("tup=%s ls=%s" % (tup,ls))
	t=ls[0]
	if t.isdigit():
		# начали с числа
		x=int(t)
		t=ls[1]
		y=int(ls[2])
		print("v1 (%s %d %d)" % (op[t],x, y))
		return tupler((op[t],x,y),ls[3:])
	if t in op:
		# начали с операции, значит первый операнд - кортеж, а второй таки число
		x=tup
		y=int(ls[1])
		print("v2 (%s %s %d" % (op[t], x, y))
		return tupler((op[t],x,y),ls[2:])

tup=None
try:
	while True:
		print ("Пиши код: ")
		print (tupler(tup,parseToken(raw_input())))
except (KeyboardInterrupt,EOFError):
	print "всего хорошего!"
	exit(0)
