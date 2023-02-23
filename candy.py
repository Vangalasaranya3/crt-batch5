k=int(input("how many you want"))
n=10
if k==0 or k>5:
    print("invalid input")
    print("number of candids left:",n)
elif k<=5:
   print("no of candids sold:",k)
   print("no of candids left:",n-k)