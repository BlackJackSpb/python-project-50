from gendiff.generator import generate_diff

file1 = 'tests/fixtures/file1.yml'
file2 = 'tests/fixtures/file2.yml'


def test_file1_vs_file2():
    assert generate_diff(file1, file2) == open('tests/fixtures/result_f1_f2_json.txt').read().strip()


def test_file1_vs_file1():
    assert generate_diff(file1, file1) == open('tests/fixtures/file1.txt').read().strip()


def test_file2_vs_file2():
    assert generate_diff(file2, file2) == open('tests/fixtures/file2.txt').read().strip()

def test_plain():
    assert generate_diff(file1, file2, 'plain') == open('tests/fixtures/result_plain.txt').read().strip()


def test_json():
    assert generate_diff(file1, file2, 'json') == open('tests/fixtures/result_json.txt').read().strip()
