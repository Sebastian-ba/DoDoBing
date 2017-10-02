from main import *

(nodes, edges) = parse_rail_file("../data/rail.txt")

def test_parser1():
	assert 119 == len(edges)

def test_parser2():
	assert 55 == len(nodes)
	
def test_parser3():
	assert "ORIGINS" == nodes[0].name
	assert "13N" == nodes[3].name
	assert "DESTINATIONS" == nodes[54].name

def test_parser4():
	assert -1 == edges[0].capacity
	assert 44 == edges[6].capacity
	assert -1 == edges[118].capacity
