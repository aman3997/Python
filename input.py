a=[]
print("Enter Numbers(0-10):")
for i in range(0,10):
	a.append(int(input(" ")))
	
print("\n\n",a,"\n\n")


b=a.copy()
b.sort()
print("Largest :",b[9],"\n\nSmallest :",b[0])