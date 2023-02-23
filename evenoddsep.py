num=int(input("enter the number"))
i=evensum=oddsum=0
while(i<=num):
    if i%2==0:
       evensum=evensum+i 
       i=i+1
    else:
       oddsum=oddsum+i
       i=i+1
print("the sum is",evensum)
print("the sum is",oddsum)

