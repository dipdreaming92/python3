n,sum=0,0
while n<5:
	value =input('enter number %s:'%(n+1))

	try:
		value=float(value)
		sum=sum+value
		n+=1
	except ValueError:
		print('invalid input.plese enter numeric value.\n')
print('\nsum=%.2f' %sum)		