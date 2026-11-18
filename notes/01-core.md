# Resolve a JSON Pointer: implementation

## What the example does

RFC 6901 escapes tilde as ~0 and slash as ~1. This implementation rejects malformed escapes, invalid array indices and the append marker.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "document": {
    "a/b": {
      "~key": [
        10,
        20
      ]
    }
  },
  "pointer": "/a~1b/~0key/1"
}
```

Expected result:

```json
20
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
