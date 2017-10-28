#!/usr/bin/python

import math
import matplotlib.pyplot as plt
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
    return binom(n - k, k)

#This is the A(n,k) function I defined in my writeup...
def A(n, k):
    return pow(2, k) * num(n - 2,k - 1) + pow(2, k + 1) * num(n - 1, k)

#The expected number of fluorescing locations in a length n
#amyloid, according to formula I derived, is:
def expected_value(length):
    result = 0.0
    for i in range(0, int(length / 2)):
        result += i * A(length, i)

    result /= pow(2, length)
    return result

if __name__ == '__main__':
    data = []
    print "Ratio of expected fluorescing proteins  on an amyloid of length {}: {}"
    for i in range(2, 1000):
        r = 2 * expected_value(i) / i 
        print "{}: {}".format(i, r)
        data.append(r)


fig1 = plt.figure()
  
l = plt.plot(range(len(data)), data, 'r-')

plt.xlim(0, len(data))
plt.ylim(0, max(data) * 1.2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('SCIENCE')

plt.show()
