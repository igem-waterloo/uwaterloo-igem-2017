import random

import matplotlib.pyplot as plt


class Promoter(object):
    def __init__(self, strength, inducer_concentration=None):
        self.strength = strength
	self.inducer_concentration = inducer_concentration

    def concentration(self):
	if self.inducer_concentration:
	    return self.strength * self.inducer_concentration
	return self.strength


class Prion(object):
    def __init__(self, name, promoter):
	self.name = name
	self.promoter = promoter


class Amyloid(object):
    def __init__(self, seq):
	self.seq = seq

    @classmethod
    def rand_amyloid(cls, prions, n):
	# TODO: make weighted random number generator based on promoter strength less bad
	weighted_prions = []
	for prion in prions:
	    weighted_prions += [prion] * prion.promoter.concentration()
	return cls([random.choice(weighted_prions) for _ in xrange(n)])

    # find the number of functional pairs in a sequence. a functional pair is either 'ab' or 'ba.' once an 'a' or 'b' is paired up,
    # it cannot be paired up again (ie. the sequence 'abaaba' should only be registered as having two functional pairs).
    def count_good(self):
	seq = self.seq
	lenSequence = len(seq)
	counter = 0
	numGood = 0
	while counter < (lenSequence - 1):
	    this_prot = seq[counter].name
	    next_prot = seq[counter + 1].name
	    if this_prot == 'a' and next_prot == 'b': # pair found.
		numGood += 1
		# skip two ahead in the sequence, since the next entry now cannot be part of another functional pair.
		counter += 2
	    elif this_prot == 'b' and next_prot == 'a': # pair found.
		numGood += 1
		# skip two ahead in the sequence, since the next entry now cannot be part of another functional pair.
		counter += 2
	    else:
		counter += 1
	# return the number of entries in functional pairs divided by the total number of entries. a number between 0 and 1. as the sequence
	# length approaches infinity, this ratio for lets=['a','b'] approaches 2/3 and for lets=['a','b','c'] approaches 1/3. also,
	# lets=['a','b','c','d'] gives 1/5 and lets=['a','b','c','d','e'] gives 2/15.
	# if you divide numGood*2 by the number of a's and b's rather than the total number of entries, then these ratios become:
	# 2/3, 1/2, 2/5, and 1/3.
        return float(numGood * 2) / lenSequence


trials = []
fracGood = []
# the number sequences of a given length we'll randomly produce and examine.
repeats = 10000

promoter1 = Promoter(strength=1, inducer_concentration=1)
promoter2 = Promoter(strength=5)
a = Prion(name='a', promoter=promoter1)
b = Prion(name='b', promoter=promoter1)
c = Prion(name='c', promoter=promoter2)

for ic in range(1, 30, 1):
    for _ in range(repeats):
	promoter1.inducer_concentration = ic
	amyloid = Amyloid.rand_amyloid([a, b, c], 20)
	trials.append(amyloid.count_good())
    fracGood.append(sum(trials) / repeats)
    print fracGood[-1]
    trials = []

fig1 = plt.figure()

data = fracGood
l = plt.plot(range(len(data)), data, 'r-')

plt.xlim(0, len(fracGood))
plt.ylim(0, max(fracGood) * 1.2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('SCIENCE')

plt.show()
