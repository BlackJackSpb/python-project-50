import pytest
from gendiff.generator import generate_diff

file1 = 'tests/fixtures/file1.yml'
file2 = 'tests/fixtures/file2.yml'
file1_txt = 'tests/fixtures/file1.txt'
file2_txt = 'tests/fixtures/file2.txt'
file1_2 = 'tests/fixtures/result_f1_f2.txt'
file2_1 = 'tests/fixtures/result_f2_f1.txt'
plain1_2 = 'tests/fixtures/result_plain_f1_f2.txt'
plain2_1 = 'tests/fixtures/result_plain_f2_f1.txt'
json1_2 = 'tests/fixtures/result_json_f1_f2.txt'
json2_1 = 'tests/fixtures/result_json_f2_f1.txt'


list_paramete = [
    (file1, file2, "stylish", file1_2),
    (file2, file1, "stylish", file2_1),
    (file1, file1, "stylish", file1_txt),
    (file2, file2, "stylish", file2_txt),
    (file1, file2, "plain", plain1_2),
    (file2, file1, "plain", plain2_1),
    (file1, file2, "json", json1_2),
    (file2, file1, "json", json2_1)
]


def formatting(file):
    return open(file).read().strip()


@pytest.mark.parametrize("par1, par2, formate, result", list_paramete)
def test_all(par1, par2, formate, result):
    assert generate_diff(par1, par2, formate) == formatting(result)
