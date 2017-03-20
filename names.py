n= ['john doe', 'jane doe', 'johny turk']
n[0] = 'foo bar'
print('names now:', n)

n.append('molly mormom')
n.append('joe bloggs')
print('names finally:', n)
print('last name in the list: %s' % n[-1])

joined_n ='\n'.join(n)
print('\nList of names:')
print(joined_n)