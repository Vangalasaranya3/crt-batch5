k=int(input("enter the weight"))
k=7000
if k==0:
	print("the estimated time is:,invalid")
elif k<=2000:
	print("the estimated time is:,25minutes")
elif k<=4000:
	print("the estimated time is:,35minutes")
elif k<=7000:
	print("the estimated time is:,45minutes")
else:
     print("the estimated time is overloaded")