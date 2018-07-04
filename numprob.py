#compute n+nn+nnn

n=input("Enter a value")
temp=str(n)
t1=temp+temp
t2=temp+temp+temp

sum=n+int(t1)+int(t2)

print("Sum=",sum)
