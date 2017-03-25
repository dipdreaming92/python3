data=[
{
'name': 'dipesh shrestha',
'email': 'dipdreaming92@gmail.com'
},
{
'name':'dinesh shrestha',
'email': 'dinesh95@gmail.com' 
}
]
print('name:%s' %data[1]['name'])
print('name:%s' %data[1]['email'])


for(i,item) in enumerate(data):
	print('\nuser %d' %(i+1))
	print('name: %s' %item['name'])
	print('name: %s' %item['email'])

