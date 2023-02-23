num=int(input("enter number"))
i=sum=0
while(i<=num):
    if i%2==0:
        print(i,end="\t")
        sum=sum+i
    i=i+1
print("\n",sum)