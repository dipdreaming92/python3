n=0
sum=0
while n<5:
	value = input('enter number %d: ' %(n+1))
	sum=sum+float(value)
	n+=1
print('sum=%.2f' %sum)
