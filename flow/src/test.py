from main import *

''' Simple Test Graph '''
edge1 = Edge(0,1,5,2)
node1 = Node("s", 0)
node2 = Node("t", 1)

node1.addEdgeTo(1, 0)
node2.addEdgeTo(0, 0)

nodes = [node1,node2]
edges = [edge1]


def test_bottleneckTest1():
	assert "s" == nodes[0].name
	assert 5 == edges[nodes[1].related_edges[0]].capacity
	assert 3 == edges[nodes[1].related_edges[0]].capacity-edges[nodes[1].related_edges[0]].flow
	assert 3 == bottleneck(nodes,edges,[0,1])


''' Complex Test Graph '''
#'''
e1 = Edge(0,3,10,3)
e2 = Edge(0,2,20,5)
e3 = Edge(2,3,30,10)
e4 = Edge(2,1,10,6)
e5 = Edge(3,1,20,5)

s = Node("s", 0)
t = Node("t", 1)
n2 = Node("n2", 2)
n3 = Node("n3", 3)

s.addEdgeTo(3,0)
s.addEdgeTo(2,1)

t.addEdgeTo(2,3)
t.addEdgeTo(3,4)

n2.addEdgeTo(0,1)
n2.addEdgeTo(3,2)
n2.addEdgeTo(1,3)

n3.addEdgeTo(0,0)
n3.addEdgeTo(2,2)
n3.addEdgeTo(1,4)

N = [s,t,n2,n3]
E = [e1,e2,e3,e4,e5]

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

def test_bottleneckTest_infinity():
	e_infinity = Edge(3,1,-1,5)
	E_infinity_set = [e1,e2,e3,e_infinity,e5]
	res = bottleneck(N,E_infinity_set,[0,2,1])
	assert 15 == res

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

e1_ = Edge(0,2,10,0)
e2_ = Edge(0,1,20,0)
e3_ = Edge(1,2,30,0)
e4_ = Edge(1,3,10,0)
e5_ = Edge(2,3,20,0)

s = Node("s", 0)
n2 = Node("n2", 1)
n3 = Node("n3", 2)
t = Node("t", 3)

s.addEdgeTo(2,0)
s.addEdgeTo(1,1)

t.addEdgeTo(1,3)
t.addEdgeTo(2,4)

n2.addEdgeTo(0,1)
n2.addEdgeTo(2,2)
n2.addEdgeTo(3,3)

n3.addEdgeTo(0,0)
n3.addEdgeTo(1,2)
n3.addEdgeTo(3,4)

nodes_1 = [s,n2,n3,t]
edges_1 = [e1_,e2_,e3_,e4_,e5_]

def test_max_flow():
	new_edges = max_flow_alg(nodes_1, edges_1)

	assert new_edges[0].flow == 10
	assert new_edges[1].flow == 20
	assert new_edges[2].flow == 10
	assert new_edges[3].flow == 10
	assert new_edges[4].flow == 20

'''
def test_max_flow_infinite():

	e1_infinity = Edge(0,2,-1,0)

	edges_2 = [e0,e1_infinity,e2,e3,e4]

	new_edges = max_flow_alg(nodes_1, edges_2)

	assert new_edges[0].flow == 10
	assert new_edges[1].flow == 40
	assert new_edges[2].flow == 30
	assert new_edges[3].flow == 10
	assert new_edges[4].flow == 20


def test_max_flow_infinite2():
	e0_infinity = Edge(0,1,-1,0)

	edges_3 = [e0,e1,e2,e3,e4]

	new_edges = max_flow_alg(nodes, edges_3)

	assert new_edges[0].flow == 20
	assert new_edges[1].flow == 20
	assert new_edges[2].flow == 20
	assert new_edges[3].flow == 0
	assert new_edges[4].flow == 20

def test_on_the_file1():
	nodes, edges = parse_rail_file("../data/rail.txt")
	edges = max_flow_alg(nodes, edges)
	flow_sum_org = 0
	flow_sum_des = 0

	for n_id, edge_id in nodes[0].related_edges.items():
		flow_sum_org += edges[edge_id].flow
	
	for n_id, edge_id in nodes[54].related_edges.items():
		flow_sum_des += edges[edge_id].flow

	print("flow_sum for file: " + str(flow_sum_des))
	
	assert flow_sum_org == flow_sum_des


def test_on_the_file2():
	nodes, edges = parse_rail_file("../data/rail.txt")
	edges = max_flow_alg(nodes, edges)
	min_cut_edges = min_cut(nodes, edges)
	print(len(min_cut_edges))
	output(min_cut_edges)
	# this is according to the out file from the data folder.
	assert len(min_cut_edges) == 9


#'''