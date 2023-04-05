import pytest
from gendiff.generate_diff import generate_diff


FILE1 = 'tests/fixtures/file1.json'
FILE2 = 'tests/fixtures/file2.json'
EXPECTED = 'tests/fixtures/result_json.txt'


def test_generate_diff():
    with open(EXPECTED, encoding='utf8') as f:
        assert generate_diff(FILE1, FILE2) == f.read().strip()
