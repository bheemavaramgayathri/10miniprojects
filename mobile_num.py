#mobile number validator 
n=input("enter valid mobile number:")
if n.isdigit()and len(n)<=10:
	print("valid")
else:
	print("invaild")