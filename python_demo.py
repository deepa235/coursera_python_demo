"""
module for approximating sqrt
More..
"""

from numpy import *
x = 0.01

def sqrt(x):

	s = 1.
	tol = 1.e-14
	kmax = 100
	for k in range(kmax):
	    print "Before iteration %s, s = %20.15f" % (k,s)
	    s0 = s
	    s = 0.5* (s + x/s)
	    delta_s = s-s0
	    if abs(delta_s/x) < tol:
	       break
	print "After %s iteration, s = %20.15f" % (k+1,s)
