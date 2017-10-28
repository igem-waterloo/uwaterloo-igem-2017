#!/usr/bin/python
import itertools
import math
#import matplotlib.pyplot as plt
#The binomial coefficient nCk...
def binom(n, k):
	if k > n or k < 0:
		return 0
	a = math.factorial(n)
	b = math.factorial(k)
	c = math.factorial(n - k)
	return a / (b * c)


def a(n):
	if n == 0:
		return 0
	elif n > 0:
		x = math.sqrt(2)
		
		result = ((3+2*x) /(x + 2) * 1.0) * pow((1.0 / (-1.0 - x)),n) + ((2*x - 3)/(x-2) * 1.0) * pow((1.0 / (x - 1)),n)
		return result

def b(n):
	x = math.sqrt(2)

	result = (1.0/(2 * x + 2)) * pow((1.0/(-1 - x)),n) + (1.0/(2 - 2*x)) * pow((1.0/(x - 1)),n)
	return -1 * result

		

#This is the A(n,k) function I defined in my writeup...
def A(n, k):
	result = 0.0
	for q in xrange(0, n + 1 - 2 * k):
 			
		lists = itertools.product(range(2,n-q-2 * (k - 1)), repeat=k)
		Lists = [x for x in lists if sum(x) == n - q]
	
		innerSum = 0.0
		for x in Lists:		
			innerProduct = 1.0
			for phi_i in x:
				innerProduct *= a(phi_i)
			innerSum += innerProduct	
		result +=	b(q) * innerSum
					
				
	return result	
#The expected number of fluorescing locations in a length n
#amyloid, according to formula I derived, is:
def expected_value(length):
	result = 0.0
	for i in xrange(0, int(length / 2) + 1):
		result += i * A(length, i)

	result /= pow(3, length)
	return result




if __name__ == '__main__':
	for i in xrange(2, 1000):
		r = 2 * expected_value(i) / i 
		print "{}: {}".format(i, r)


#fig1 = plt.figure()

#l = plt.plot(range(len(data)), data, 'r-')

#plt.xlim(0, len(data))
#plt.ylim(0, max(data) * 1.2)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('SCIENCE')

#plt.show()
