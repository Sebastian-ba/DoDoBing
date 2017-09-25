from main import *

penalties_parsed = parse_penalty_file("../data/BLOSUM62.txt")

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
    assert len(penalties_parsed) == 24
    assert penalties_parsed['W']['W'] == 11

def testBoard1Alg():
    result = Alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    sresult = result[0]
    assert sresult == -10

def testBoard2Alg():
    result = Alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    assert result[1] == "BQXF"


def testBoard3Alg():
    result = Alignment(("First", "AFC"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "BQX"
    assert result[0] == -7

def testBoard4Alg():
    result = Alignment(("First", "AF"), ("Second", "BQ"), penalties_parsed)
    assert result[1] == "BQ"
    assert result[0] == -5

def testBoard5Alg():
    result = Alignment(("First", "A"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B"
    assert result[0] == -2


def testBoard6Alg():
    result = Alignment(("First", "W"), ("Second", "D"), penalties_parsed)
    assert result[1] == "D"
    assert result[0] == -4


def testBoard7Alg():
    result = Alignment(("First", "AFC"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B--"
    assert result[0] == -10

def testBoard8Alg():
    result = Alignment(("First", "A"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "--X"
    assert result[0] == -8

''''''

def testspace_efficient1():
    result = space_efficient_alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    sresult = result[0]
    assert sresult == -10

def testspace_efficient2():
    result = space_efficient_alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    assert result[1] == "BQXF"


def testspace_efficient3():
    result = space_efficient_alignment(("First", "AFC"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "BQX"
    assert result[0] == -7

def testspace_efficient4():
    result = space_efficient_alignment(("First", "AF"), ("Second", "BQ"), penalties_parsed)
    assert result[1] == "BQ"
    assert result[0] == -5

def testspace_efficient5():
    result = space_efficient_alignment(("First", "A"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B"
    assert result[0] == -2


def testspace_efficient6():
    result = space_efficient_alignment(("First", "W"), ("Second", "D"), penalties_parsed)
    assert result[1] == "D"
    assert result[0] == -4


def testspace_efficient7():
    result = space_efficient_alignment(("First", "AFC"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B--"
    assert result[0] == -10

def testspace_efficient8():
    result = space_efficient_alignment(("First", "A"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "--X"
    assert result[0] == -8