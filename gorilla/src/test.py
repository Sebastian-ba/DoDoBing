from main import *

def test_1():
    assert 1 == 1

def test_2():
    assert "1" == "1"

def test_3():
    assert 2 == 2

def test_parse_toys():
    dna_parsed = len(parse_dna_file("../data/Toy_FASTAs-in.txt"))
    assert dna_parsed == 3

def test_parse_real():
    dna_parsed = len(parse_dna_file("../data/HbB_FASTAs-in.txt"))
    assert dna_parsed == 13

def test_parse_penalties():
    penalties_parsed = len(parse_penalty_file("../data/BLOSUM62.txt"))
    assert penalties_parsed == 24