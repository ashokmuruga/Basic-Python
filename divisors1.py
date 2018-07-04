#factors(n)


number=input("Enter the number")
a=[]
for i in range(2,number+1):
    if(number%i==0):
       a.append(i);

print(a)

print("Small Divisor",min(a))

  
    	
