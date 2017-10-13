from main import *

# simple

edge1 = Edge(0,1,5,2)
node1 = Node("s", 0)
node1.addEdgeTo(edge1, 0)
node2 = Node("t", 1)
node2.addEdgeFrom(edge1, 0)
nodes = [node1,node2]
edges = [edge1]

def test_basic():
    print("\nNothing Should be printed")
    output(nodes,edges)

edges[0] = Edge(0,1,5,5)
def test_basic2():
    print("\nShould Print (0,1,5)")
    output(nodes,edges)

# complex

e0 = Edge(0,1,10,3)
e1 = Edge(0,2,20,5)
e2 = Edge(2,3,30,10)
e3 = Edge(2,1,10,6)
e4 = Edge(1,3,20,5)

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

nodes_2 = [s,n2,n3,t]
edges_2 = [e0,e1,e2,e3,e4]

def test_complex():
    print("\nNothing Should be printed")
    output(nodes_2,edges_2)

edges_2[0] = Edge(0,1,10,10)
def test_complex2():
    print("\nShould Print (0,1,10)")
    output(nodes_2,edges_2)

edges_2[3] = Edge(2,3,30,30)
def test_complex3():
    print("\nShould Print (0,1,10) && (2,3,30)")
    output(nodes_2,edges_2)


e0 = Edge(0,1,10,0)
e1 = Edge(0,2,20,0)
e2 = Edge(2,3,30,0)
e3 = Edge(2,1,10,0)
e4 = Edge(1,3,20,0)

nodes_3 = [s,n2,n3,t]
edges_3 = [e0,e1,e2,e3,e4]

def test_complex4():
    edges_3_solved = max_flow_alg(nodes_3, edges_3)
    
    print("\nShould print (0,1,10) && (0,2,20)")
    output(nodes_3,edges_3_solved)

edges_3[0] = Edge(0,1,-1,0)
edges_3[1] = Edge(0,2,-1,0)
def test_complex4_with_infinite_edges():
    edges_3_solved = max_flow_alg(nodes_3, edges_3)
    
    print("\nShould print (2,3,30) && (1,3,20)")
    output(nodes_3,edges_3_solved)