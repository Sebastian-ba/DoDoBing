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
    def __init__(self, from_node_id, to_node_id, capacity, flow):
        self.from_node_id = from_node_id
        self.to_node_id = to_node_id
        self.capacity = capacity
        self.flow = flow

class Node:
    def __init__(self, name, node_id):
        self.name = name
        self.id = node_id
        self.related_edges = {}

    def addEdgeTo(self, edge, edge_id):
        self.related_edges[edge.to_node_id] = edge_id

    def addEdgeFrom(self, edge, edge_id):
        self.related_edges[edge.from_node_id] = edge_id


def output():
    pass

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
    if not(path):
        return None
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
        for edge in max_flow_alg(nodes, edges):
            # "The maximum value of an s-t flow is equal to the minimum capacity over all s-t cuts"
            # To find the minimum cut flow must be > 0 and flow = capacity
            if edge.flow > 0 and edge.flow == edge.capacity:
                print(edge.from_node_id, edge.to_node_id, edge.flow)

'''END CODE'''
