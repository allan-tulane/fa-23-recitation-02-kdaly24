from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(16, 5, 2) == 1031
	assert simple_work_calc(1, 2, 2) == 1
	assert simple_work_calc(23, 4, 2) == 531

def test_work():
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(27, 3, 2, lambda n: n) == 282
	assert work_calc(12, 2, 2,lambda n: n+n) == 80
	assert work_calc(1, 1, 2, lambda n: n*n) == 1
	

