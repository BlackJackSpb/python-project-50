from gendiff.generator import generate_diff

file1 = 'tests/fixtures/file1.yml'
file2 = 'tests/fixtures/file2.yml'


def test_file1_vs_file2():
    assert generate_diff(file1, file2) == open('tests/fixtures/result_f1_f2_json.txt').read().strip()
