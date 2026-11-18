from solution import solve

value = {'document': {'a/b': {'~key': [10, 20]}}, 'pointer': '/a~1b/~0key/1'}
print(solve(value))
