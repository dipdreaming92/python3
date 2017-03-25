names=['john doe','jane doe','johny turk','molly mormon']
i=0
total_names=len(names)
print('users:')
while i<total_names:
	end='  and\n' if i==total_names - 2 else '\n'
	print(' - %s' %names[i], end=end)
	i+=1