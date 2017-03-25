def fib(n=50):
	a,b=0,1

	while a<n:
		print(a)
		(a,b)=(b,a+b)
fib(500)	


n=int(input('enter limit:'))
fib(n)		