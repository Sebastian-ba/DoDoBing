from main import *

edge1 = Edge(0,1,5,2)
node1 = Node("s")
node1.addEdgeTo(edge1, 0)
node2 = Node("t")
node2.addEdgeFrom(edge1, 0)

nodes = [node1,node2]
edges = [edge1]

def test_bottleneckTest1():
	assert "s" == nodes[0].name
	assert 5 == edges[nodes[1].related_edges[0]].capacity
	assert 3 == edges[nodes[1].related_edges[0]].capacity-edges[nodes[1].related_edges[0]].flow
	assert 3 == bottleneck(nodes,edges,[0,1])


def test_augmentTest1():
	res_edges = augment(nodes, edges, [0,1])
	assert 5 == res_edges[0].capacity

def test_augmentTest2():
	res_edges = augment(nodes, edges, [0,1])
	assert 5 == res_edges[0].flow