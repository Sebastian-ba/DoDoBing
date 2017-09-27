from main import *

penalties_parsed = parse_penalty_file("../data/BLOSUM62.txt")

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
    assert penalties_parsed['A']['A'] == 4
    assert penalties_parsed['M']['N'] == -2
    assert penalties_parsed['A']['Q'] == -1
    assert penalties_parsed['T']['B'] == -1
    assert penalties_parsed['*']['*'] == 1
    assert penalties_parsed['A']['*'] == -4

def test_board_1_alg():
    result = alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    sresult = result[0]
    assert sresult == -10

def test_board_2_alg():
    result = alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    assert result[1] == "BQXF"

def test_board_3_alg():
    result = alignment(("First", "AFC"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "BQX"
    assert result[0] == -7

def test_board_4_alg():
    result = alignment(("First", "AF"), ("Second", "BQ"), penalties_parsed)
    assert result[1] == "BQ"
    assert result[0] == -5

def test_board_5_alg():
    result = alignment(("First", "A"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B"
    assert result[0] == -2

def test_board_6_alg():
    result = alignment(("First", "W"), ("Second", "D"), penalties_parsed)
    assert result[1] == "D"
    assert result[0] == -4

def test_board_7_alg():
    result = alignment(("First", "AFC"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B--"
    assert result[0] == -10

def test_board_8_alg():
    result = alignment(("First", "A"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "--X"
    assert result[0] == -8

def test_space_efficient1():
    result = space_efficient_alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    sresult = result[0]
    assert sresult == -10

def test_space_efficient2():
    result = space_efficient_alignment(("First", "AFCD"), ("Second", "BQXF"), penalties_parsed)
    assert result[1] == "BQXF"

def test_space_efficient3():
    result = space_efficient_alignment(("First", "AFC"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "BQX"
    assert result[0] == -7

def test_space_efficient4():
    result = space_efficient_alignment(("First", "AF"), ("Second", "BQ"), penalties_parsed)
    assert result[1] == "BQ"
    assert result[0] == -5

def test_space_efficient5():
    result = space_efficient_alignment(("First", "A"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B"
    assert result[0] == -2

def test_space_efficient6():
    result = space_efficient_alignment(("First", "W"), ("Second", "D"), penalties_parsed)
    assert result[1] == "D"
    assert result[0] == -4

def test_space_efficient7():
    result = space_efficient_alignment(("First", "AFC"), ("Second", "B"), penalties_parsed)
    assert result[1] == "B--"
    assert result[0] == -10

def test_space_efficient8():
    result = space_efficient_alignment(("First", "A"), ("Second", "BQX"), penalties_parsed)
    assert result[1] == "--X"
    assert result[0] == -8


def test_space_efficient_real1():
    result = space_efficient_alignment(
        ("Human", "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"),
        ("Goul", "VHWSAEEKQLITGLWGKVNVADCGAEALARLLIVYPWTQRFFASFGNLSSPTAINGNPMVRAHGKKVLTSFGEAVKNLDNIKNTFAQLSELHCDKLHVDPENFRLLGDILIIVLAAHFAKDFTPDSQAAWQKLVRVVAHALARKYH"),
        penalties_parsed
    )
    assert result[0] == 532

def test_space_efficient_real2():
    result = space_efficient_alignment(
        ("Trout", "VEWTDAEKSTISAVWGKVNIDEIGPLALARVLIVYPWTQRYFGSFGNVSTPAAIMGNPKVAAHGKVVCGALDKAVKNMGNILATYKSLSETHANKLFVDPDNFRVLADVLTIVIAAKFGASFTPEIQATWQKFMKVVVAAMGSRYF"),
        ("Rockcod", "VEWTDKERSIISDIFSHMDYDDIGPKALSRCLIVYPWTQRHFSGFGNLYNAEAIIGNANVAAHGIKVLHGLDRGVKNMDNIAATYADLSTLHSEKLHVDPDNFKLLSDCITIVLAAKMGHAFTAETQGAFQKFLAVVVSALGKQYH"),
        penalties_parsed
    )
    assert result[0] == 442
