import ast


__version__ = '1.0.0'


mutable_types = [
    ast.Dict,
    ast.List,
    ast.Set,
    ast.Call,
]


class MutableClassAttrsChecker(object):
    """
    Mutable class attributes checker.

    Flake8 extension that alerts when a mutable type is used for class
    attributes.

    """
    name = 'flake-mutable-class-attrs'
    version = __version__

    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        err_msg = 'FIXME_CODE - mutable class attribute of type {}'

        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                for attr in node.body:
                    if isinstance(attr, ast.Assign):
                        for mutable_type in mutable_types:
                            if isinstance(attr.value, mutable_type):
                                yield (
                                    attr.value.lineno,
                                    attr.value.col_offset,
                                    err_msg.format(type(attr.value).__name__),
                                    type(self)
                                )
