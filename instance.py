a=float(input('first number:'))
b=float(input('second number:'))
try:
	result=a/b
	print(result)
except ZeroDivisionError:	
	print('error:divison by zero')