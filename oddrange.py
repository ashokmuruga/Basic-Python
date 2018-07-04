#Odd numbers in range

lower=input("Enter lower limit")
upper=input("Enter Upper limit")
print("Odd Numbers\n")
for i in range(lower,upper+1):
    if(i%2!=0):
       print(i)
    
