from main import *

(nodes_1, s1, t1, c1, n1, e1) = parse_red_file("../data/common-1-20.txt")
def test_common_1_20_some():
    assert n(nodes_1,s1,t1,c1,e1) == '-'

(nodes_2, s2, t2, c2, n2, e2) = parse_red_file("../data/common-1-100.txt")
def test_common_1_100_some():
    assert n(nodes_2,s2,t2,c2,e2) == '-'

(nodes_3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
def test_G_ex_some():
    res = n(nodes_3,s3,t3,c3,e3)
    assert res == 3

(nodes_4, s4, t4, c4, n4, e4) = parse_red_file("../data/increase-n8-2.txt")
def test_increase_n8_2_some():
    res = n(nodes_4,s4,t4,c4,e4)
    assert res == 1

(nodes_5, s5, t5, c5, n5, e5) = parse_red_file("../data/increase-n8-1.txt")
def test_increase_n8_1_some():
    res = n(nodes_5,s5,t5,c5,e5)
    assert res == 1