from main import *



def test_G_ex_many():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert t3 in nodes3[s3].edges_out


def test_5():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "5" in nodes3[s3].edges_out


def test_1():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "1" not in nodes3[s3].edges_out

def test_6():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "6" not in nodes3["5"].edges_out

def test_6_not_in_7():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "6" not in nodes3["7"].edges_out

def test_5_contains_7():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "7" in nodes3["5"].edges_out

def test_y_contains_7_in():
	(nodes3, s3, t3, c3, n3, e3) = parse_red_file("../data/G-ex.txt")
	reduce_graph(nodes3, s3, t3)
	assert "7" in nodes3["5"].edges_in


def test_wall_s():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert "3" in nodes4[s4].edges_out

def test_wall_s_in():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert "3" in nodes4[s4].edges_in

def test_wall_t_in():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert "3" in nodes4[t4].edges_in

def test_wall_t():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert "3" in nodes4[t4].edges_out

def test_wall_t_3_count():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert len(nodes4["3"].edges_in) == 2

def test_wall_t_4():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert "4" not in nodes4[t4].edges_out

def test_wall_t_4_in():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert "4" not in nodes4[t4].edges_in

def test_wall_s_4_in():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-p-1.txt")
	reduce_graph(nodes4, s4, t4)
	assert "4" not in nodes4[s4].edges_in


def test_wall_s_t_in():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-z-3.txt")
	reduce_graph(nodes4, s4, t4)
	assert t4 in nodes4[s4].edges_in

def test_wall_s_t_out():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-z-3.txt")
	reduce_graph(nodes4, s4, t4)
	assert t4 in nodes4[s4].edges_out

def test_wall_t_s_out():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-z-3.txt")
	reduce_graph(nodes4, s4, t4)
	assert s4 in nodes4[t4].edges_out

def test_wall_t_s_in():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-z-3.txt")
	reduce_graph(nodes4, s4, t4)
	assert s4 in nodes4[t4].edges_in

def test_wall_t_s_out_not_in():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-z-3.txt")
	reduce_graph(nodes4, s4, t4)
	assert "17" not in nodes4[t4].edges_out

def test_wall_t_3_count_2():
	(nodes4, s4, t4, c4, n4, e4) = parse_red_file("../data/wall-z-3.txt")
	reduce_graph(nodes4, s4, t4)
	assert len(nodes4[t4].edges_in) == 1