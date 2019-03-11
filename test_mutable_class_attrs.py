import ast
import pytest

from mutable_class_attrs import MutableClassAttrsChecker


@pytest.mark.parametrize("input_,expected", [
    ('{}', 'FIXME_CODE - mutable class attribute of type Dict'),
    ('{"a": 0}', 'FIXME_CODE - mutable class attribute of type Dict'),
    ('[]', 'FIXME_CODE - mutable class attribute of type List'),
    ('[0]', 'FIXME_CODE - mutable class attribute of type List'),
    ('{1,}', 'FIXME_CODE - mutable class attribute of type Set'),
    ('dict()', 'FIXME_CODE - mutable class attribute of type Call'),
    ('list()', 'FIXME_CODE - mutable class attribute of type Call'),
    ('set()', 'FIXME_CODE - mutable class attribute of type Call'),

    ('None', None),
    ('0', None),
    ('"string"', None),
    ('()', None),
    # ('frozenset()', None),  # FIXME
])
def test_attr_types(input_, expected):
    code = """
class Foo():
    attr = {}
""".format(input_)


    checker = MutableClassAttrsChecker(ast.parse(code), 'ignored')
    result = tuple(checker.run())

    if expected is None:
        assert not result
    else:
        assert expected == result[0][2]
