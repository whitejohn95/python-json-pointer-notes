import re

def resolve(document, pointer):
    if pointer == '':
        return document
    if not pointer.startswith('/'):
        raise ValueError('pointer must start with slash')
    for part in pointer[1:].split('/'):
        if re.search(r'~(?![01])', part):
            raise ValueError('invalid pointer escape')
        key = part.replace('~1', '/').replace('~0', '~')
        if isinstance(document, list):
            if not re.fullmatch(r'0|[1-9][0-9]*', key):
                raise ValueError('invalid array index')
            document = document[int(key)]
        else:
            document = document[key]
    return document

def solve(value):
    return resolve(value["document"], value["pointer"])
