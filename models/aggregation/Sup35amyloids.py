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
	return -1 *result

		



#This is the A(n,k) function I defined in my writeup...
def A(n, k):
	result = 0.0
	for q in xrange(0, n):
 			
		lists = itertools.combinations(range(0,k), k + 1)
		Lists = [x for x in lists if sum(x) == n - q]
		
		for x in Lists:		
			pseudoResult = 1.0
			for i in x:
				pseudoResult *= a(i)
			result += b(q) * pseudoResult			
				
	return result	
#The expected number of fluorescing locations in a length n
#amyloid, according to formula I derived, is:
def expected_value(length):
	result = 0.0
	for i in xrange(0, int(length / 2)):
		result += i * A(length, i)

	result /= pow(3, length)
	return result




if __name__ == '__main__':
	data = []
		
	print "Ratio of expected fluorescing proteins  on an amyloid of length {}: {}"
	for i in range(2, 1000):
		r = 2 * expected_value(i) / i 
		print "{}".format(a(i))
		print "{}".format(b(i))
		print "{}: {}".format(i, r)
		data.append(r)


#fig1 = plt.figure()

3  
#l = plt.plot(range(len(data)), data, 'r-')

#plt.xlim(0, len(data))
#plt.ylim(0, max(data) * 1.2)
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('SCIENCE')

#plt.show()
