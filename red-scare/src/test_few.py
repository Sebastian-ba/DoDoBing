from main import *

def test_1():
    (nodes_1, s1, t1, c1, n1 , e1) = parse_red_file("../data/common-1-20.txt")
    result = f(nodes_1,s1,t1, c1, e1)
    assert result == '-'

def test_2():
    (nodes_2, s2, t2, c2, n2 , e2) = parse_red_file("../data/common-1-100.txt")
    result = f(nodes_2,s2,t2, c2, e2)
    assert result == '-'


def test_3():
    (nodes_3, s3, t3, c3, n3 , e3) = parse_red_file("../data/increase-n8-1.txt")
    result = f(nodes_3,s3,t3, c3, e3)
    assert result == 1

