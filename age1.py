age=int(input('enter you age:'))
if age<=0:
	print('invalid input for age')
elif age<=1:
	print('you are an infant')
elif age<=12:
	print('you are just a kid')
elif age<=19:
	print('you are teenager')
elif age<=45:
	print('')
elif age<=59:
	print('you are middle aged')
elif age<=120:
	print('you are old now')
else:
	print('you r too old but still alive')
