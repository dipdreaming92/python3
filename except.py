while True:
	a=float(input('first number:'))
	b=float(input('second number:'))
	try:
		result=a/b
		print('result={}'.format(result))
	except ZeroDivisionError:	
		print('error:divison by zero')
	try_again=input('\ntry again (Y/N)?')

	if try_again.upper()!='Y':
		break
	print()	
print('good bye!')		