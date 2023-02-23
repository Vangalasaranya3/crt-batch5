num=int(input("enter the number"))
temp=0
while num!=0:
     temp=num%10
     print(temp,end="")
     num=num//10