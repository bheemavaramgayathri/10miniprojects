Total= int(input("enter:"))
Present=int(input("enter:"))
Attendance=Present/Total*100
if Attendance>75:
	print("eligible")
else:
	print("not eligible")