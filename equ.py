#input the equation in y=mx+c
equation=input('equation: ')
#'y','mx+c'
rhs = equation.split('=')[1]
#'mx','c'
parts = rhs.split('+')

m = parts[0].replace('x','').strip()
c = parts[1].strip()

print('slope of line: {}'.format(m))
print('y intercept of line: {}'.format(c))
