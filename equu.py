
equ = input("enter the equation of straight line in the form of y = mx +c : ")
rhs = equ.split('=')[1]
parts = rhs.split('+')
m = parts[0].replace('x', '').strip()
c = parts[1].strip()

print('slope of line: {}'.format(m))
print('y-intercept of line: {}'.format(c))