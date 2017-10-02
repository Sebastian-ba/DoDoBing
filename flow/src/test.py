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
