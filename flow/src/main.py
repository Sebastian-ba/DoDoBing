'''Imports'''
import sys
#import re
#import string

'''Parse'''

'''Parse end'''

'''Helper methods'''

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
        edge_id = nodes[path[i]]["edge_ids"][path[i+1]]
        throughput = edges[edge_id]["capacity"] - edges[edge_id]["flow"]
        if throughput < max_throughput or max_throughput == -1:
            max_throughput = throughput
    return max_throughput

'''Helper methods end'''

'''Algorithm'''
def augment(nodes, edges, start, target, path):
    max_throughput = bottleneck(P,f)
    for i in range(len(path) - 1):
        edge_id = nodes[path[i]]["edge_ids"][path[i+1]]
        if edges[edge_id]["from"] == path[i]: 
            #if edge is a forward edge then increase flow 
            edges[edge_id]["flow"] += max_throughput
        else:
            #if edge is a backward edge, decrease the flow
            edges[edge_id]["flow"] -= max_throughput
    return edges
    
def max_flow_alg(nodes, edges, start, target):
    path = get_valid_path(nodes, edges, start, target)
    if not(path):
        return None
    while not(path):
        edges = augment(nodes, edges, start, target, path)
        path = get_valid_path(nodes, edges, start, target)
    return edges
'''Algorithm end'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    #if len(args) > 2:
    #    all_dna = parse_dna_file(args[1])
    #    all_penalty = parse_penalty_file(args[2])
    #    main_algo(all_dna, all_penalty)

'''END CODE'''