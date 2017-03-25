def fib(n):
	a,b=0,1

	while a<n:
		print(a)
		(a,b)=(b,a+b)
def main():
	n=int(input('n='))
	
	print (fib(n))
main()
