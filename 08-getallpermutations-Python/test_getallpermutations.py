import os,sys
sys.path.append(os.getcwd())
from getallpermutations import getallpermutations
import pytest
from itertools import permutations

@pytest.mark.parametrize('x',[
	("abc"), ("abcd"), ("ab"), ("abcde"), 
	("pqr"), ("pqrs"), ("pq"), ("pqrst"), 
	("xyz"), ("xyza"), ("xy"), ("xyzab"),
])

def test_getallpermutations(x):
	l = list(permutations(x, r=len(x)))
	l.sort(key = lambda x: x[0])
	print(l)
	assert getallpermutations(x) == l
