from math import floor

def GCD(a,b):
	if b==0:
		return (a,1,0)
	q = floor(a/b)
	(d,k,l) = GCD(b, a % b)
	return (d,l,k-l*q)

if __name__=="__main__":
	from random import randint
	a,b = randint(1,1000), randint(1,1000)
	print(a,b,GCD(a,b),sep='\t')