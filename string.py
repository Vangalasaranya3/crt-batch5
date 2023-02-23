txt='india is my country'
print(txt)
print(txt[1:5])
print(txt[:6])
print(txt[:])
print(txt[-4])
print(txt[::3])
ch='a'
print(ord(ch))
print(chr(65))
txt1='india is great'
txt2='id'
if txt2 in txt1:
	print("found")
else:
	print("not found")
txt='india is great'
for i in txt:
	print(i,end=" ")
txt='india is great'
i=0
while i<len(txt):
	letter=txt[i]
	print(letter,end=" ")
	i+=1
	