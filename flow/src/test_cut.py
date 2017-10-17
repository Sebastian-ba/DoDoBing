from main import *

e_1 = Edge(0,2,10,0)
e_2 = Edge(0,1,20,0)
e_3 = Edge(1,2,30,0)
e_4 = Edge(1,3,10,0)
e_5 = Edge(2,3,20,0)
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
edges_1 = [e_1,e_2,e_3,e_4,e_5]


def test_complex4():
    edges_solved = max_flow_alg(nodes_1, edges_1)
    
    edges_cut = min_cut(nodes_1, edges_solved)
    assert len(edges_cut) == 2

    print()
    flow_sum = 0
    flow_cap = 0
    for edge in edges_cut:
        flow_sum += edge.flow
        flow_cap += edge.capacity
        print(edge)

    assert flow_sum == 30
    assert flow_cap == 30
    

e_1 = Edge(0,2,10,0)
e_2 = Edge(0,1,20,0)
e_3 = Edge(1,2,30,0)
e_4 = Edge(1,3,10,0)
e_5 = Edge(2,3,20,0)

edges_2 = [Edge(0,1,-1,0),Edge(0,2,-1,0),e_3,e_4,e_5]
def test_complex4_with_infinite_edges():
    edges_solved = max_flow_alg(nodes_1, edges_2)
    
    edges_cut = min_cut(nodes_1, edges_solved)
    assert len(edges_cut) == 2

    print()
    flow_sum = 0
    flow_cap = 0
    for edge in edges_cut:
        flow_sum += edge.flow
        flow_cap += edge.capacity
        print(edge)

    assert flow_sum == 30
    assert flow_cap == 30



a = Node("a", 0)
b = Node("b", 1)
c = Node("c", 2)
d = Node("d", 3)
e = Node("e", 4)
f = Node("f", 5)

e1 = Edge(0,1,5,0)
a.addEdgeTo(1,0)
b.addEdgeTo(0,0)
e2 = Edge(0,2,5,0)
a.addEdgeTo(2,1)
c.addEdgeTo(0,1)
e3 = Edge(1,3,3,0)
b.addEdgeTo(3,2)
d.addEdgeTo(1,2)
e4 = Edge(1,4,6,0)
b.addEdgeTo(4,3)
e.addEdgeTo(1,3)
e5 = Edge(2,3,1,0)
c.addEdgeTo(3,4)
d.addEdgeTo(2,4)
e6 = Edge(2,4,3,0)
c.addEdgeTo(4,5)
e.addEdgeTo(2,5)
e7 = Edge(3,5,6,0)
d.addEdgeTo(5,6)
f.addEdgeTo(3,6)
e8 = Edge(4,5,6,0)
e.addEdgeTo(5,7)
f.addEdgeTo(4,7)

nodes_3 = [a,b,c,d,e,f]
edges_3 = [e1,e2,e3,e4,e5,e6,e7,e8]

def test_the_one_on_youtube():
    edges_solved = max_flow_alg(nodes_3, edges_3)

    edges_cut = min_cut(nodes_3, edges_solved)
    assert len(edges_cut) == 3
    print()
    flow_sum = 0
    flow_cap = 0
    for edge in edges_cut:
        flow_sum += edge.flow
        flow_cap += edge.capacity
        print(edge)

    assert flow_sum == 9
    assert flow_cap == 9
