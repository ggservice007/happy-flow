from six.moves import cStringIO
import ujson
from ast_utils.unparser import Unparser
from ast_utils.printer import Printer, JSONPrinter

__version__ = '0.0.1'


def unparse(tree):
    v = cStringIO()
    Unparser(tree, file=v)
    return v.getvalue()


def dump(tree):
    v = cStringIO()
    Printer(file=v).visit(tree)
    return v.getvalue()

def dump_json(tree):
    v = cStringIO()
    JSONPrinter(file=v).visit(tree)
    return ujson.dumps(
            ujson.loads(v.getvalue()),
            ensure_ascii=False,
            escape_forward_slashes=False,
            indent=2
        )
