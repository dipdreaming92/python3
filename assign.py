authorized_users=[
	{
		'name':'john',
		'email':'john92',
		'password':'aaa'
	},
	{
		'name':'dip',
		'email':'dip92',
		'password':'bbb'

	}	
]
email=input('enter email')
password=input('enter password')
login_success=False
user_exist=False
for user in authorized_users:
	if email==user['email'] and password==user['password']:
		login_success=True
		user_exist=True
		print('user found:')
		print('name:{}'.format(user['name']))
		print('name:{}'.format(user['email']))
		break
	elif email==user['email']:
		user_exist=True	
if user_exist==False:
	print('user with email {} does not exist in our system.'.format(email))		
if login_success==False:
	print('acccess denied')	
