n=int(input("Enter Starting:"))
m=int(input("\nEnter Ending:"))

for i in range(n,m+1):
  
   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i)