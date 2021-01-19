import ast

def dump(node, annotate_fields=True, include_attributes=False, indent=' '):
    """
    Return a formatted dump of the tree in *node*. This is mainly useful for
    debugging purpose. The returned string will show the names and the values for 
    fields. This makes the code impossible to evaluate, so if evaluation is wanted 
    *annotate_fields* must be set fo False. Attributes such as line numbers 
    and columns offsets are not dumpled by default. If this is wanted, 
    *include_attributes* can be set to True.
    """
    def _format(node, level=0):
        if isinstance(node, ast.AST):
            fields = [(a, _format(b, level)) for a, b in ast.iter_fields(node)]
            rv = '%s(%s' % (node.__class__.__name__, ', '.join(
                ('%s=%s' % field for field in fields)
                if annotate_fields else
                (b for a, b in fields)
            ))
            if include_attributes and node._attributes:
                rv += fields and ', ' or ' '
                rv += ', '.join('%s=%s' % (a, _format(getattr(node, a)))
                                for a in node._attributes)
            return rv + ')'
        elif isinstance(node, list):
            lines = ['[']
            lines.extend(
                (
                    indent * (level + 2) + _format(x, level + 2) + ',' 
                    for x in node
                )
            )
            if len(lines) > 1:
                lines.append(indent * (level + 1) + ']')
            else:
                lines[-1] += ']'
            return '\n'.join(lines)
        return repr(node)

    if not isinstance(node, ast.AST):
        raise TypeError('expected AST, got %r' % node.__class__.__name__)

    return _format(node)


def parseprint(source, filename='<unkown>', mode='exec', **kwargs):
    """
    Parse the source and pretty-print the AST.
    """
    node = ast.parse(source, filename, mode=mode)
    print(dump(node, **kwargs))