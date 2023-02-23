a=7
b=6
i=j=temp=1
list_=[]
n=int(input("Enter n:"))
while(temp<=n):
    if temp%2!=0:
        list_.append(a*(i-1))
        i+=1
    else:
        list_.append(b*(j-1))
    temp+=1
print("the {} term is:{}".format(n,list_[n-1]))