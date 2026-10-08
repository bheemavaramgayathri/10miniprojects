#simple calculator 
a=int(input("enter:"))
b=int(input("Enter:"))
Operator=input("enter the operator:")
if Operator=="+":
	print(a+b)
elif Operator=="-":
	print(a-b)
elif Operator=="*":
	print(a*b)
elif Operator=="/":
	print(a/b)
elif Operator=="//":
	print(a//b)
elif Operator=="**":
	print(a**b)
elif Operator=="%":
	print(a%b)
else:
	print("invalid operator")