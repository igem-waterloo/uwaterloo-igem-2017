import math

#The binomial coefficient nCk...
def binom(n,k):
	if n == k:
		return 1;
	elif k == 1:
		return n;
	elif k > n:
		return 0;
	elif k == 0:
		return 1;
	elif k < 0:
		return 0;
	elif n > k:
		a = math.factorial(n)
		b = math.factorial(k)
		c = math.factorial(n - k)
		div = a // (b * c)
		return div;

#This is the \#(n,k) function I defined in my writeup...
def num(n,k):
	return binom(n-k-1,k);

#This is the A(n,k) function I defined in my writeup...
def A(n,k):
	return pow(2,k) * num(n-2,k-1) + pow(2,k+1) * num(n-1,k);

#The expected number of fluorescing locations in a length n
#amyloid, according to formula I derived, is:
def ExpectedValue(length):
	result = 0.00;
	for i in range(0,int(math.floor(length/2))):
		result += i * A(length,i) ;	

	result /= pow(2,length);
	print "Number of expected fluorescing locations on an amyloid of length ", length,": ", result; 
	return result;

ExpectedValue(10);
ExpectedValue(50);
ExpectedValue(75);
ExpectedValue(100);
ExpectedValue(1000);
ExpectedValue(1010);
