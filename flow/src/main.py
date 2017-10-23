'''Imports'''
import sys

'''Parse'''

def parse_rail_file(filename):
    nodes = []
    edges = []

    node_counter = 0
    edge_counter = 0

    flow = 0

    parsing_nodes = False
    parsing_edges = False

    total_nodes = 0
    total_edges = 0

    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if parsing_edges:
                string_integers = line.split(' ')
                node_id_1 = int(string_integers[0])
                node_id_2 = int(string_integers[1])
                capacity = int(string_integers[2])
                edges.append( Edge(node_id_1, node_id_2, capacity, flow))
                nodes[node_id_1].addEdgeTo(node_id_2, edge_counter)
                nodes[node_id_2].addEdgeTo(node_id_1, edge_counter)
                edge_counter += 1
                if edge_counter == total_edges:
                    parsing_edges = False
                continue
            if parsing_nodes:
                nodes.append(Node(line[:-1], node_counter))
                node_counter += 1
                if node_counter == total_nodes:
                    parsing_nodes = False
                continue
            if total_nodes == 0:
                total_nodes = int(line)
                parsing_nodes = True
                continue
            if total_edges == 0:
                total_edges = int(line)
                parsing_edges = True

    return(nodes,edges)

'''Parse end'''

'''Helper methods'''
class Edge:
    def __init__(self, node_id_1, node_id_2, capacity, flow):
        self.node_id_1 = node_id_1
        self.node_id_2 = node_id_2
        self.capacity = capacity
        self.flow = flow
        self.forward = True

    def is_forward(self, node_id_1, node_id_2):
        return self.node_id_1 == node_id_1 and self.node_id_2 == node_id_2
    
    def __str__(self):
        return str(self.node_id_1) + " " + str(self.node_id_2) + " " + str(self.capacity) + " " + str(self.flow)

class Node:
    def __init__(self, name, node_id):
        self.name = name
        self.id = node_id
        self.related_edges = {}

    def addEdgeTo(self, node_id, edge_id):
        self.related_edges[node_id] = edge_id
    
    def __str__(self):
        return str(self.name) + " " + str(self.id) + " " + str(self.related_edges)

''' Optimized BFS. Doesn't do much for out very small dataset,
    but should help with large/ very large data sets.
    
    Also ensures that we always
    look at nodes in the expected (correct) fashion - highest remaining capacity 
    node first.

    Can maybe be further tuned to always return the the most optimal "path" not
    based on "steps".
'''
def optimized_valid_path(nodes, edges):
    # final steps dict to return, mapping is (nodeid -> nodeid)
    path_steps = {}

    # visited nodes tracker
    visited_nodes = [False]*(len(nodes))

    # sorted queue based on (cap - flow), inserted structure is (value, nodeid) tuples
    sorted_queue = []

    # enqueue start node, has 0 capacity/flow, since we do not have a preceding node
    sorted_queue.append((0, nodes[0]))

    # empty start path
    path_steps[0] = None
    visited_nodes[0] = True

    while sorted_queue:
        #dequeue first vertex (highest value)
        cur_node = sorted_queue.pop(0)[1]

        # iterate all vertex edges
        for nid, eid in cur_node.related_edges.items():
            # sanity check if we are at max capacity
            if (edges[eid].capacity - edges[eid].flow) == 0:
                continue
            # last node, the end
            if nid == (len(nodes) - 1):
                path_steps[nid] = cur_node.id
                return get_full_path(path_steps, nid)
            # check if we visited node before

            # do we want to check if there is a better path in terms of node -> node capacity or should we just take them in the highest order no matter what?
            if visited_nodes[nid] == False:
                # enqueue val, node
                sorted_queue.append((edges[eid].capacity - edges[eid].flow, nodes[nid]))
                # sort list based on val in highest first order.
                sorted_queue = sorted(sorted_queue, key=lambda tup: tup[0], reverse=True)
                path_steps[nid] = cur_node.id
                visited_nodes[nid] = True
    return None

''' BFS 
    Unused due to opt. BFS being implemented.
'''
def get_valid_path(nodes, edges):
    path_steps = {}

    # visited nodes tracker
    visited_nodes = [False]*(len(nodes))
    # queue of nodes to check from
    queue = []

    # queue start Node
    queue.append(nodes[0])
    path_steps[0] = None
    visited_nodes[0] = True

    while queue:
        # dequeue first vertex in queue

        cur_node = queue.pop(0)
        for nid, eid in cur_node.related_edges.items():
            # check if we are at max capacity
            if (edges[eid].capacity - edges[eid].flow) == 0:
                continue
            # last node, the end
            if nid == (len(nodes) - 1):
                path_steps[nid] = cur_node.id
                return get_full_path(path_steps, nid)
            # check if we visited node before
            if visited_nodes[nid] == False:
                queue.append(nodes[nid])
                path_steps[nid] = cur_node.id
                visited_nodes[nid] = True
    return None

''' Traceback the valid path from a certain nid '''
def get_full_path(path_dict, nid):
    cur_path = []
    while path_dict[nid] != None:
        cur_path.append(nid)
        nid = path_dict[nid]
    cur_path.append(0)
    cur_path.reverse()
    return cur_path

'''returns the current maximum throughput on the given path.'''
def bottleneck(nodes, edges, path):
    # this is clearly positive infinity
    max_throughput = -1
    for i in range(len(path) - 1):
        edge_id = nodes[path[i]].related_edges[path[i + 1]]
        capacity = edges[edge_id].capacity
        flow = edges[edge_id].flow
        if capacity >= 0:
            if edges[edge_id].is_forward(path[i],path[i + 1]):
                throughput = capacity - flow
            else: 
                throughput = flow + capacity - flow
                edges[edge_id].forward = False

            if throughput < max_throughput or max_throughput == -1:
                max_throughput = throughput
    return max_throughput

def min_cut(nodes, edges):
    a = set([0])
    queue = []
    queue.append(nodes[0])
    while queue:
        cur_node = queue.pop(0)
        for nid, eid in cur_node.related_edges.items():
            if edges[eid].capacity == edges[eid].flow or nid in a:
                continue
            a.add(nid)
            queue.append(nodes[nid])
  
    b = set()
    for nid in a:
        cur_node = nodes[nid]
        for nid, eid in cur_node.related_edges.items():
            if not(edges[eid].node_id_1 in a):
                b.add(nid)

    a = a | b

    min_cut_edges = []
    for nid in a:
        cur_node = nodes[nid]
        for nid, eid in cur_node.related_edges.items():
            if not(edges[eid].node_id_2 in a) or not(edges[eid].node_id_1 in a):
                min_cut_edges.append(edges[eid])
    return min_cut_edges


def output(edges):
    if edges:
        for edge in edges:
            print(str(edge))
    else :
        print("There is no ideal cut")

'''Helper methods end'''

'''Algorithm'''
def augment(nodes, edges, path):
    max_throughput = bottleneck(nodes, edges, path)

    for i in range(len(path) - 1):
        edge_id = nodes[path[i]].related_edges[path[i+1]]
        if edges[edge_id].forward:
            edges[edge_id].flow += max_throughput
        else:
            edges[edge_id].flow -= max_throughput
            edges[edge_id].forward = True
            
    return edges


def max_flow_alg(nodes, edges):
    path = optimized_valid_path(nodes, edges)
    while path:
        edges = augment(nodes, edges, path)
        path = optimized_valid_path(nodes, edges)
    return edges
'''Algorithm end'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        nodes, edges = parse_rail_file(args[1])
        edges = max_flow_alg(nodes, edges)
        min_cut_edges = min_cut(nodes, edges)
        output(min_cut_edges)
'''END CODE'''
