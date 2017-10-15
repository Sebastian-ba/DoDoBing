from main import *

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

nodes_3 = [s,n2,n3,t]
edges_3 = [e0,e1,e2,e3,e4]

def test_complex4():
    edges_3_solved = max_flow_alg(nodes_3, edges_3)
    
    print("\nShould print  0 1 10 && 0 2 20")
    edges_3_solved = min_cut(nodes_3, edges_3_solved)
    output(edges_3_solved)

edges_3[0] = Edge(0,1,-1,0)
edges_3[1] = Edge(0,2,-1,0)
def test_complex4_with_infinite_edges():
    edges_3_solved = max_flow_alg(nodes_3, edges_3)
    
    print("\nShould print 2 3 30 && 1 3 20")
    edges_3_solved = min_cut(nodes_3, edges_3_solved)
    output(edges_3_solved)