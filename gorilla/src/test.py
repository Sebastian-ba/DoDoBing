from main import *

def test_1():
    assert 1 == 1

def test_2():
    assert "1" == "1"

def test_3():
    assert 2 == 2

def test_parse_toys():
    dna_parsed = parse_dna_file("../data/Toy_FASTAs-in.txt")
    assert len(dna_parsed) == 3
    assert dna_parsed[1][1] == "KAK"

def test_parse_real():
    dna_parsed = parse_dna_file("../data/HbB_FASTAs-in.txt")
    assert len(dna_parsed) == 13
    assert dna_parsed[2][0] == "Gorilla"

def test_parse_penalties():
    penalties_parsed = parse_penalty_file("../data/BLOSUM62.txt")
    assert len(penalties_parsed) == 24
    print(penalties_parsed['*'])
    assert penalties_parsed['W']['W'] == 11
    assert penalties_parsed['A']['A'] == 4
    assert penalties_parsed['M']['N'] == -2
    assert penalties_parsed['A']['Q'] == -1
    assert penalties_parsed['T']['B'] == -1
    assert penalties_parsed['*']['*'] == 1
    assert penalties_parsed['A']['*'] == -4
