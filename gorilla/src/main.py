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

def output(dna_1, dna_2, result):
    print(dna_1[0] + "--" + dna_2[0] + ": " +  str(result[0]))
    print(dna_1[1])
    print(result[1])

'''Helper methods end'''

'''Algorithm'''
def alignment(dna_1, dna_2, all_penalty):
    a = []
    for i in range(0, len(dna_1[1])+1):
        a.append([])
        for j in range(0, len(dna_2[1])+1):
            a[i].append((0,""))


    for i in range(1, len(dna_1[1])+1):
        a[i][0] = (-4 * i, "-" + a[i-1][0][1])
    for j in range(1, len(dna_2[1])+1):
        a[0][j] = (-4 * j, "-" + a[0][j-1][1])
    for j in range(1,len(dna_2[1])+1):
        for i in range(1,len(dna_1[1])+1):
            left = -4 + a[i][j-1][0]
            down = -4 + a[i-1][j][0]
            cross = all_penalty[dna_1[1][i-1]][dna_2[1][j-1]] + a[i-1][j-1][0]
            if(left > down and left > cross):
                a[i][j] = (left, a[i][j-1][1] + "-")
            elif down > left and down > cross:
                a[i][j] = (down , a[i-1][j][1] + "-")
            else :
                a[i][j] = (cross , a[i-1][j-1][1] + dna_2[1][j-1])
    return a[len(dna_1[1])][len(dna_2[1])]


def space_efficient_alignment(dna_1, dna_2, all_penalty):
    a = []
    for i in range(0, 2):
        a.append([])
        for j in range(0, len(dna_1[1])+1):
            a[i].append((0,""))
    for i in range(1, len(dna_1[1])+1):
        a[0][i] = (-4 * i, "-" + a[0][i-1][1])
    for j in range(1,len(dna_2[1])+1):
        a[j%2][0] = (-4 * j, "-" + a[j%2-1][0][1])
        for i in range(1,len(dna_1[1])+1):
            left = -4 + a[j%2-1][i][0]
            down = -4 + a[j%2][i-1][0]
            cross = all_penalty[dna_1[1][i-1]][dna_2[1][j-1]] + a[j%2-1][i-1][0]
            if(left > down and left > cross):
                a[j%2][i] = (left, a[j%2-1][i][1] + "-")
            elif down > left and down > cross:
                a[j%2][i] = (down , a[j%2][i-1][1] + "-")
            else :
                a[j%2][i] = (cross , a[j%2-1][i-1][1] + dna_2[1][j-1])
            letter = j
    return a[len(dna_2[1]) % 2][len(dna_1[1])]

def backward_space_efficient_alignment():
    pass

def devide_and_conquer_alignment(dna_1, dna_2, all_penalty):
    # let m be the number of symbols in dna_1
    # let n be the number of symbols in dna_2
    # if m <= 2 or n <= 2 then
        # compute optimal alignment using Allignment(X,Y)
    # call Space-Efficient-Alignment (X,Y[1:n/2])
    # Call Backward_Space_efficient_alignment(X,Y[n/2 +1:n])

    # Let q be the index minimizing f(q, n/2)+ g(q, n/2)
    # add (q,n/2) to global list P

    # devide_and_conquer_alignment(dna_1[1:q], dna_2[1:n/2])
    # devide_and_conquer_alignment(dna_1[q + 1:n], dna_2[n/2 +1:n])
    # return P....
    pass

def main_algo(all_dna, all_penalty):
    for i in range(len(all_dna)):
        for j in range (i, len(all_dna)):
            if i != j:
                res = space_efficient_alignment(all_dna[j], all_dna[i], all_penalty)
                output(all_dna[i], all_dna[j], res)

'''Algorithm'''

'''RUN CODE'''
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        all_dna = parse_dna_file(args[1])
        all_penalty = parse_penalty_file(args[2])
        main_algo(all_dna, all_penalty)

'''END CODE'''
