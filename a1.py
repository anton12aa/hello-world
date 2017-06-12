v = input()
m=int(input())
n=int(input())
a=int(input())
sa=a*a
s=m*n

if s%sa>=1:
	b=s//sa+1
	print(b)
else:	
	b=s//sa
	print(b)
