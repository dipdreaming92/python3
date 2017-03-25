point1=int(input('enter co ordinate of x:'))
point2=int(input('enter co ordinate of y:'))
if point1>0 and point2>0:  
	print('lies on 1st')
elif point1<0 and point2<0:  
	print('lies on 3th')
elif point1<0  and point2>0:
	print('lies on 2nd')
elif point1>0 and point2<0:
	print('lies on 4th')
elif point1==0 and point2==0:
	print('lies on origin')
else:
	print('nothing')					
