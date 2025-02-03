import pytest
from gendiff.generator import generate_diff


def get_full_path(file):
    return 'tests/fixtures/' + file


def get_result(file):
    with open(file) as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, formate, answer", [
    ('file1.yml', 'file2.yml', "stylish", 'file_1_2.txt'),
    ('file2.yml', 'file1.yml', "stylish", 'file_2_1.txt'),
    ('file1.yml', 'file1.yml', "stylish", 'file1.txt'),
    ('file2.yml', 'file2.yml', "stylish", 'file2.txt'),
    ('file1.yml', 'file2.yml', "plain", 'plain_1_2.txt'),
    ('file2.yml', 'file1.yml', "plain", 'plain_2_1.txt'),
    ('file1.yml', 'file2.yml', "json", 'json_1_2.txt'),
    ('file2.yml', 'file1.yml', "json", 'json_2_1.txt')  
])
def test_all(file1, file2, formate, answer):
    full_path1 = get_full_path(file1)
    full_path2 = get_full_path(file2)
    correct_answer = get_result(get_full_path(answer))
    assert generate_diff(full_path1, full_path2, formate) == correct_answer
