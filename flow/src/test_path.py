from main import *

# simple

edge1 = Edge(0,1,5,2)
node1 = Node("s", 0)
node1.addEdgeTo(1, 0)
node2 = Node("t", 1)
node2.addEdgeTo(0, 0)
nodes = [node1,node2]
edges = [edge1]

# complex

e0 = Edge(0,1,10,3)
e1 = Edge(0,2,20,5)
e2 = Edge(2,3,30,10)
e3 = Edge(2,1,10,6)
e4 = Edge(1,3,20,5)

s = Node("s", 0)
s.addEdgeTo(1, 0)
s.addEdgeTo(2, 1)

n2 = Node("n2", 1)
n2.addEdgeTo(0, 1)
n2.addEdgeTo(2, 3)
n2.addEdgeTo(3, 4)

n3 = Node("n3", 2)
n3.addEdgeTo(0, 0)
n3.addEdgeTo(1, 3)
n3.addEdgeTo(3, 2)

t = Node("t", 3)
t.addEdgeTo(1, 4)
t.addEdgeTo(2, 2)

nodes_2 = [s,n2,n3,t]
edges_2 = [e0,e1,e2,e3,e4]

# 0 flow on first

e0 = Edge(0,1,10,10)
e1 = Edge(0,2,20,5)
e2 = Edge(2,3,30,10)
e3 = Edge(2,1,10,6)
e4 = Edge(1,3,20,5)

s = Node("s", 0)
s.addEdgeTo(1, 0)
s.addEdgeTo(2, 1)

n2 = Node("n2", 1)
n2.addEdgeTo(0, 1)
n2.addEdgeTo(2, 3)
n2.addEdgeTo(3, 4)

n3 = Node("n3", 2)
n3.addEdgeTo(0, 0)
n3.addEdgeTo(1, 3)
n3.addEdgeTo(3, 2)

t = Node("t", 3)
t.addEdgeTo(1, 4)
t.addEdgeTo(2, 2)

nodes_3 = [s,n2,n3,t]
edges_3 = [e0,e1,e2,e3,e4]

# long path

e0 = Edge(0,1,10,10)
e1 = Edge(0,2,20,5)
e2 = Edge(2,3,30,30)
e3 = Edge(2,1,10,6)
e4 = Edge(1,3,20,5)

s = Node("s", 0)
s.addEdgeTo(1, 0)
s.addEdgeTo(2, 1)

n2 = Node("n2", 1)
n2.addEdgeTo(0, 1)
n2.addEdgeTo(2, 3)
n2.addEdgeTo(3, 4)

n3 = Node("n3", 2)
n3.addEdgeTo(0, 0)
n3.addEdgeTo(1, 3)
n3.addEdgeTo(3, 2)

t = Node("t", 3)
t.addEdgeTo(1, 4)
t.addEdgeTo(2, 2)

nodes_4 = [s,n2,n3,t]
edges_4 = [e0,e1,e2,e3,e4]

# no more paths

e0 = Edge(0,1,10,3)
e1 = Edge(0,2,20,5)
e2 = Edge(2,3,30,30)
e3 = Edge(2,1,10,6)
e4 = Edge(1,3,20,20)

s = Node("s", 0)
s.addEdgeTo(1, 0)
s.addEdgeTo(2, 1)

n2 = Node("n2", 1)
n2.addEdgeTo(0, 1)
n2.addEdgeTo(2, 3)
n2.addEdgeTo(3, 4)

n3 = Node("n3", 2)
n3.addEdgeTo(0, 0)
n3.addEdgeTo(1, 3)
n3.addEdgeTo(3, 2)

t = Node("t", 3)
t.addEdgeTo(1, 4)
t.addEdgeTo(2, 2)

nodes_5 = [s,n2,n3,t]
edges_5 = [e0,e1,e2,e3,e4]

def test_basic():
    path = get_valid_path(nodes, edges)
    assert path == [0, 1]

def test_complex():
    path = get_valid_path(nodes_2, edges_2)
    assert path == [0, 1, 3] # valid

def test_complex2(): # block flow from 0->1
    path = get_valid_path(nodes_3, edges_3)
    assert path == [0, 2, 3] # valid

def test_complex3(): # block flow from 2->3 & 0->1
    path = get_valid_path(nodes_4, edges_4)
    assert path == [0, 2, 1, 3] # valid

def test_complex4(): # block from from 2->3 & 1->3
    path = get_valid_path(nodes_5, edges_5)
    assert path == None # valid

edge1 = Edge(0,1,-1,0)
edge2 = Edge(1,2,10,0)
node1 = Node("s", 0)
node1.addEdgeTo(1, 0)
node2 = Node("n1", 1)
node2.addEdgeTo(0, 0)
node2.addEdgeTo(2, 1)
node3 = Node("t", 2)
node3.addEdgeTo(1, 1)
nodes_6 =  [node1, node2, node3]
edges_6 =  [edge1, edge2]

def test_simple_infinite_path():
    path = get_valid_path(nodes_6, edges_6)
    assert path == [0,1,2]



