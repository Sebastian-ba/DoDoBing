'''Imports'''
import sys
import re
import string
'''Imports end'''
'''Fields'''

'''Fields end'''

'''Parse'''


def parse_dna_file(filename):
    '''
    Parse file to an array of tuples (name, dna-string)
    @param: filename: path of file to parse
    '''
    dna_array = []
    dna_counter = -1
    with open(filename) as f:
        lines = f.readlines()
        cur_species = ""
        cur_dna = ""
        for line in lines:
            if line[0] == ">":
                #save prev species
                if dna_counter != -1:
                    dna_array.insert(dna_counter,(cur_species, cur_dna))

                #new species
                line_cleaned = line[1:]
                cur_species = line_cleaned.split()[0]
                cur_dna = ""
                dna_counter += 1
                continue
            line_newline_cleaned = line.rstrip()
            cur_dna += line_newline_cleaned

        #save last species occurence
        dna_array.insert(dna_counter,(cur_species, cur_dna))
    return dna_array

def parse_penalty_file(filename):
    '''
    Parse file to a dict of dicts {enzyme,{enzyme, score}}
    @param: filename: path of file to parse
    '''
    penalty_dict = {}

    with open(filename) as f:
        lines = f.readlines()
        line_count = 0
        map_array = []
        for line in lines:
            if line[0] == "#":
                continue

            line_space_cleaned = line.split()
            if line_count == 0:
                # read to tmparr
                map_array = line_space_cleaned
                line_count +=1
                continue

            # set new dict
            penalty_dict[line_space_cleaned[0]] = {}
            for x in range(1, len(line_space_cleaned)):
                penalty_dict[line_space_cleaned[0]][map_array[(int(x)-1)]] = int(line_space_cleaned[x])

            line_count += 1
    return penalty_dict

'''Parse end'''


'''Helper methods'''

def output(result):
    pass

'''Helper methods end'''

'''Algorithm'''
def space_efficient_alignment():
    pass

def backward_space_efficient_alignment():
    pass

def devide_and_conquer_alignment(dna_1, dna_2):
    # let m be the number of ymbols in dna_1
    # let n be the number of symbols in dna_2
    # if m <= 2 or n <= then 
        # compute optimal alignment using Allignemnt(X,Y)
    # call Space-Efficient-Alignment (X,Y[1:n/2])
    # Call Backward_Space_efficient_alignment(X,Y[n/2 +1:n])
    
    # Let q be the index minimizing f(q, n/2)+ g(q, n/2)
    # add (q,n/2) to global list P

    # devide_and_conquer_alignment(dna_1[1:q], dna_2[1:n/2])
    # devide_and_conquer_alignment(dna_1[q + 1:n], dna_2[n/2 +1:n])
    # return P....
    pass

'''def main_algo(all_dna, all_penalty):
    for i in range(len(all_dna)):
        for j in range (i, len(all_dna)):
            if i != j:
                res = devide_and_conquer_alignment(all_dna[i], all_dna[j], all_penalty)
                output(res)'''
'''Algorithm'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        all_dna = parse_dna_file(args[1])
        all_penalty = parse_penalty_file(args[2])
        #main_algo(all_dna, all_penalty)
        
'''END CODE'''

