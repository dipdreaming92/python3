squares= [x**2 for x in range(10)]
print('squares:',squares)
num=[1,2,3,4,5,6,7,8,9,10]
even_num= [x for x in num if x%2 ==0]
odd_num= [x for x in num if x%2 !=0]
print('numbers:',num)
print('even numbers:',even_num)
print('odd numbers:',odd_num)