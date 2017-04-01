import test
def main():
	n=int(input("enter a number:"))
	series=test.fibo(n)
	print('series upto {}:\n {}'.format(n,series))
	print('factorial of {}:{}'.format(n,test.factorial(n)))
	print(__name__)
main()