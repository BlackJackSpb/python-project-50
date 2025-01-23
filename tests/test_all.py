from gendiff.generator import generate_diff

file1 = 'tests/fixtures/file1.yml'
file2 = 'tests/fixtures/file2.yml'
file1_txt = 'tests/fixtures/file1.txt'
file2_txt = 'tests/fixtures/file2.txt'
file1_2_txt = 'tests/fixtures/result_f1_f2_json.txt'
plain = 'tests/fixtures/result_plain.txt'
json = 'tests/fixtures/result_json.txt'


def test_file1_vs_file2():
    assert generate_diff(file1, file2) == open(file1_2_txt).read().strip()


def test_file1_vs_file1():
    assert generate_diff(file1, file1) == open(file1_txt).read().strip()


def test_file2_vs_file2():
    assert generate_diff(file2, file2) == open(file2_txt).read().strip()


def test_plain():
    assert generate_diff(file1, file2, 'plain') == open(plain).read().strip()


def test_json():
    assert generate_diff(file1, file2, 'json') == open(json).read().strip()
