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
                from_node_id = int(string_integers[0])
                to_node_id = int(string_integers[1])
                capacity = int(string_integers[2])
                edges.append( Edge(from_node_id, to_node_id, capacity, flow))
                nodes[from_node_id].addEdgeTo(edges[edge_counter], edge_counter)
                nodes[to_node_id].addEdgeFrom(edges[edge_counter], edge_counter)

                if edge_counter == total_edges:
                    parsing_edges = False
                continue
            if parsing_nodes:
                nodes.append(Node(line[:-1]))
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
    def __init__(self, from_node_id, to_node_id, capacity, flow):
        self.from_node_id = from_node_id
        self.to_node_id = to_node_id
        self.capacity = capacity
        self.flow = flow


class Node:
    def __init__(self, name):
        self.name = name
        self.related_edges = {}

    def addEdgeTo(self, edge, edge_id):
        self.related_edges[edge.to_node_id] = edge_id

    def addEdgeFrom(self, edge, edge_id):
        self.related_edges[edge.from_node_id] = edge_id


def output():
    pass

def get_valid_path(nodes, edges, start, target):
    pass

''' 
    returns the current maximum throughput on the given path.
'''

def bottleneck(nodes, edges, path):
    # this is clearly positive infinity
    max_throughput = -1
    for i in range(len(path)-1):
        edge_id = nodes[path[i]].related_edges[path[i+1]]
        throughput = edges[edge_id].capacity - edges[edge_id].flow
        if throughput < max_throughput or max_throughput == -1:
            max_throughput = throughput
    return max_throughput

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
    
def max_flow_alg(nodes, edges, start, target):
    path = get_valid_path(nodes, edges, start, target)
    if not(path):
        return None
    while not(path):
        edges = augment(nodes, edges, path)
        path = get_valid_path(nodes, edges, start, target)
    return edges
'''Algorithm end'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        (nodes,edges) = parse_rail_file(args[1])
        print(nodes[0].name)
    #    all_dna = parse_dna_file(args[1])
    #    all_penalty = parse_penalty_file(args[2])
    #    main_algo(all_dna, all_penalty)

'''END CODE'''