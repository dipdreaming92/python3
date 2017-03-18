print("enter marks of five subject")
e=input("enter marks of english")
n=input("enter marks of nepali")
s=input("enter marks of science")
m=input("enter marks of math")
so=input("enter marks of social")
total=float(e) + float(n) + float(s) + float(m) + float(so)
print("total marks {}".format(total))
per=(total/500) *100
print("percent ={:.2f}%" .format(per))



