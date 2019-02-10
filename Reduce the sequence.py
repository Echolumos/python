# There is a sequence 1, 2, 3, ..., N.
# At each iteration you remove every second element of the sequence, starting from the first element, 
# then from the last element, then again from the first and so on.

# Suppose N=9 and you have [1 2 3 4 5 6 7 8 9];
# At the first iteration you remove every second element, starting with the first element, so you get: [2 4 6 8];
# At the second iteration you remove every second element, starting with the last one, so you get: [2 6];
# Then you remove every 2nd element, again, from the beginning and get [6];
# So, for N=9 the answer is 6!

import numpy as np
from scipy import optimize
import math

def get_a_number(n):
    # get a number of iterations required to solve the problem 
    num_of_is = n.bit_length() - 1
    first = [1] # the first element in the sequence
    last = [n] # the last element in the sequence
    for i in xrange(num_of_is):	
        if i % 2 == 0 :  # if i is even, the first element is deleted from the sequence
            first[0] += 2**i # if the number of elements in the sequence is odd - the last element is removed, else it is preserved
            if n/(2**i) % 2 != 0: 
                last[0] -= 2**i
        else: # if i is odd, the last element is deleted from the sequence
            last[0] -= 2**i
            if n/(2**i) % 2 != 0: # if the number of elements in the sequence is odd - the first element is removed, else it is preserved
                first[0] += 2**i
return first[0]