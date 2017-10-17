'''Imports'''
import sys
#import re
#import string

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

class Node:
    def __init__(self, name, node_id):
        self.name = name
        self.id = node_id
        self.related_edges = {}

    def addEdgeTo(self, node_id, edge_id):
        self.related_edges[node_id] = edge_id


''' BFS '''
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
            # check if we're going in the correct direction
            if edges[eid].to_node_id == cur_node.id:
                continue
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


'''
    returns the current maximum throughput on the given path.
'''

def bottleneck(nodes, edges, path):
    # this is clearly positive infinity
    max_throughput = -1
    for i in range(len(path)-1):
        edge_id = nodes[path[i]].related_edges[path[i+1]]
        capacity = edges[edge_id].capacity
        if capacity >= 0:
            throughput = capacity - edges[edge_id].flow
            if throughput < max_throughput or max_throughput == -1:
                max_throughput = throughput

    return max_throughput

def min_cut(nodes, edges):
    ''' the old
    min_cut_edges = []
    for node in nodes:
        for nid, eid in node.related_edges.items():
            #if not(edges[eid].to_node_id in a):
            if edges[eid].flow == edges[eid].capacity:
                min_cut_edges.append(edges[eid])

    return min_cut_edges
    #'''
    ''' the new
    queue = []
    queue.append(nodes[0])
    while queue:
        cur_node = queue.pop(0)
        for nid, eid in cur_node.related_edges.items():
            # check if we are at max capacity
            if edges[eid].capacity == edges[eid].flow:
  
                continue
            if nid in a:
                continue
            if edges[eid].to_node_id == cur_node.id:
                #if not(edges[eid].from_node_id in a):
                #    queue.append(nodes[nid])
                #    a.add(nid)
                continue
            queue.append(nodes[nid])
            a.add(nid)
    #'''
    ''' # this is the one for reverse .
    a = set([len(nodes)-1])
    queue = []
    queue.append(nodes[len(nodes)-1])
    while queue:
        cur_node = queue.pop(0)
        for nid, eid in cur_node.related_edges.items():
            # check if we are at max capacity
            if edges[eid].capacity == edges[eid].flow:
                continue
            if nid in a:
                continue
            if edges[eid].from_node_id == cur_node.id:
                continue
            queue.append(nodes[nid])
            a.add(nid)
    '''
    print(a)

    min_cut_edges = []
    for nid in a:
        cur_node = nodes[nid]
        for nid, eid in cur_node.related_edges.items():
            ## change to from for the reverse
            #if not(edges[eid].from_node_id in a):
            if not(edges[eid].to_node_id in a):
            #if edges[eid].flow > 0 and edges[eid].flow == edges[eid].capacity:
                min_cut_edges.append(edges[eid])

    return min_cut_edges


def output(edges):
    if edges:
        for edge in edges:
            print("" + str(edge.from_node_id) + " " + str(edge.to_node_id) + " " + str(edge.flow) + " " + str(edge.capacity))
    else :
        print("There is no ideal cut")

'''Helper methods end'''

'''Algorithm'''
def augment(nodes, edges, path):
    max_throughput = bottleneck(nodes, edges, path)
    for i in range(len(path) - 1):
        edge_id = nodes[path[i]].related_edges[path[i+1]]
        if edges[edge_id].from_node_id == path[i]:
            #if edge is a forward edge then increase flow
            edges[edge_id].flow += max_throughput
        else:
            #if edge is a backward edge, decrease the flow
            edges[edge_id].flow -= max_throughput
    return edges

def max_flow_alg(nodes, edges):
    path = get_valid_path(nodes, edges)
    while path:
        edges = augment(nodes, edges, path)
        path = get_valid_path(nodes, edges)
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
