from main import *

''' Simple Test Graph '''
edge1 = Edge(0,1,5,2)
node1 = Node("s", 0)
node1.addEdgeTo(edge1, 0)
node2 = Node("t", 1)
node2.addEdgeFrom(edge1, 0)
nodes = [node1,node2]
edges = [edge1]

''' Complex Test Graph '''
e1 = Edge(0,3,10,3)
e2 = Edge(0,2,20,5)
e3 = Edge(2,3,30,10)
e4 = Edge(2,1,10,6)
e5 = Edge(3,1,20,5)

s = Node("s", 0)
s.addEdgeTo(e1,0)
s.addEdgeTo(e2,1)

t = Node("t", 1)
t.addEdgeFrom(e4,3)
t.addEdgeFrom(e5,4)

n2 = Node("n2", 2)
n2.addEdgeFrom(e2,1)
n2.addEdgeTo(e3,2)
n2.addEdgeTo(e4,3)

n3 = Node("n3", 3)
n3.addEdgeFrom(e1,0)
n3.addEdgeFrom(e3,2)
n3.addEdgeTo(e5,4)

N = [s,t,n2,n3]
E = [e1,e2,e3,e4,e5]


''' Test Methods '''

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
	res = res_edges[0].flow
	assert 5 == res


def test_bottleneckTest2():
	res = bottleneck(N,E,[0,2,3,1])
	assert 15 == res

def test_bottleneckTest3():
	res = bottleneck(N,E,[0,3,1])
	assert 7 == res

def test_bottleneckTest4():
	e1 = Edge(0,3,10,3)
	e2 = Edge(0,2,20,5)
	e3 = Edge(2,3,30,10)
	e4 = Edge(2,1,10,6)
	e5 = Edge(3,1,-1,5)

	s = Node("s", 0)
	s.addEdgeTo(e1,0)
	s.addEdgeTo(e2,1)

	t = Node("t", 1)
	t.addEdgeFrom(e4,3)
	t.addEdgeFrom(e5,4)

	n2 = Node("n2", 2)
	n2.addEdgeFrom(e2,1)
	n2.addEdgeTo(e3,2)
	n2.addEdgeTo(e4,3)

	n3 = Node("n3", 3)
	n3.addEdgeFrom(e1,0)
	n3.addEdgeFrom(e3,2)
	n3.addEdgeTo(e5,4)

	N = [s,t,n2,n3]
	E = [e1,e2,e3,e4,e5]


	res = bottleneck(N,E,[0,3,1])
	assert 7 == res

def test_bottleneckTest5():
	res = bottleneck(N,E,[0,2,1])
	assert 4 == res

def test_augmentTest3():
	res_edges = augment(N, E, [0,3,1])
	res = res_edges[0].flow
	assert 10 == res

def test_augmentTest4():
	res_edges = augment(N, E, [0,2,1])
	res = res_edges[1].flow
	assert 9 == res

def test_augmentTest5():
	res_edges = augment(N, E, [0,2,1])
	res = res_edges[3].flow
	assert 10 == res

def test_max_flow():
	e0 = Edge(0,1,10,0)
	e1 = Edge(0,2,20,0)
	e2 = Edge(2,3,30,0)
	e3 = Edge(2,1,10,0)
	e4 = Edge(1,3,20,0)

	s = Node("s", 0)
	s.addEdgeTo(e0, 0)
	s.addEdgeTo(e1, 1)

	n2 = Node("n2", 1)
	n2.addEdgeFrom(e1, 1)
	n2.addEdgeFrom(e3, 3)
	n2.addEdgeTo(e4, 4)

	n3 = Node("n3", 2)
	n3.addEdgeFrom(e0, 0)
	n3.addEdgeTo(e3, 3)
	n3.addEdgeTo(e2, 2)

	t = Node("t", 3)
	t.addEdgeFrom(e4, 4)
	t.addEdgeFrom(e2, 2)

	nodes = [s,n2,n3,t]
	edges = [e0,e1,e2,e3,e4]

	new_edges = max_flow_alg(nodes, edges)

	assert new_edges[0].flow == 10
	assert new_edges[1].flow == 20
	assert new_edges[2].flow == 20
	assert new_edges[3].flow == 0
	assert new_edges[4].flow == 10
