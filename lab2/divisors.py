def divisors(n):
	n = int(n)
	for num in range(1,n+1):
		if n % num == 0:
			print num

if __name__=='__main__':
	n = raw_input("enter a number ")
	divisors(n)

