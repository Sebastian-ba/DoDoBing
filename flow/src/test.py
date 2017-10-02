from main import *

''' Simple Test Graph '''
edge1 = Edge(0,1,5,2)
node1 = Node("s")
node1.addEdgeTo(edge1, 0)
node2 = Node("t")
node2.addEdgeFrom(edge1, 0)
nodes = [node1,node2]
edges = [edge1]

''' Complex Test Graph '''
e1 = Edge(0,3,10,3)
e2 = Edge(0,2,20,5)
e3 = Edge(2,3,30,10)
e4 = Edge(2,1,10,6)
e5 = Edge(3,1,20,5)

s = Node("s")
s.addEdgeTo(e1,0)
s.addEdgeTo(e2,1)

t = Node("t")
t.addEdgeFrom(e4,3)
t.addEdgeFrom(e5,4)

n2 = Node("n2")
n2.addEdgeFrom(e2,1)
n2.addEdgeTo(e3,2)
n2.addEdgeTo(e4,3)

n3 = Node("n3")
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

	s = Node("s")
	s.addEdgeTo(e1,0)
	s.addEdgeTo(e2,1)

	t = Node("t")
	t.addEdgeFrom(e4,3)
	t.addEdgeFrom(e5,4)

	n2 = Node("n2")
	n2.addEdgeFrom(e2,1)
	n2.addEdgeTo(e3,2)
	n2.addEdgeTo(e4,3)

	n3 = Node("n3")
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