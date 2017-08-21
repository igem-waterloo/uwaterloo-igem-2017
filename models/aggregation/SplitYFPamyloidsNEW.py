import math

#The binomial coefficient nCk...
def binom(n, k):
	if k > n or k < 0:
		return 0
	a = math.factorial(n)
	b = math.factorial(k)
	c = math.factorial(n - k)
	return a / (b * c)

#This is the \#(n,k) function I defined in my writeup...
def num(n, k):
	return binom(n - k - 1, k)

#This is the A(n,k) function I defined in my writeup...
def A(n, k):
	return pow(2, k) * num(n - 2, k - 1) + pow(2, k + 1) * num(n - 1, k)

#The expected number of fluorescing locations in a length n
#amyloid, according to formula I derived, is:
def expected_value(length):
	result = 0.0
	for i in range(0, int(length / 2)):
		result += i * A(length, i)

	result /= pow(2, length)
	print "Number of expected fluorescing locations on an amyloid of length {}: {}".format(length, result)
	return result

expected_value(10)
expected_value(50)
expected_value(75)
expected_value(100)
expected_value(1000)
expected_value(1010)
