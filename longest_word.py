str='This book is goodyugfyutyu for python.'
a=len(str)
str1=str.split(" ")
count=1
longlength=0
longword=""
print(a)
for i in range(0,a):
	if str[i]==" ":
		count=count+1
		
for j in str1:
	if len(j)>longlength:
		longword=j
		longlength = len(j)
		print("longlength :",longlength)
		
		
		
print("Longest word :",longword)		
		
print("No. of words:",count)

print(str1)		
		
		
		
		
		
		
		
		
		
		
		
		
		
input()