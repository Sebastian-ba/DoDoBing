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
    pass

'''Helper methods end'''

'''Algorithm'''
def augment(nodes, edges, start, target, path):
    max_througput = bottleneck(P,f)
    for node_id in path:
        # if e=(u,v) is a forward edge then 
            # increase f(e) in G by b
        # else ((u,v) is a backward edge, and let e=(v,u))
            # decrease f(e) in G by b
    return nodes
    
def max_flow_alg(nodes, edges, start, target):
    path = get_valid_path(nodes, edges, start, target)
    if not(path):
        return None
    while not(path):
        edges = augment(nodes, new_edges, start, target, path)
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