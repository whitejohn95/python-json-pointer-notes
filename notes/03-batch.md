# Ordered batch processing for Resolve a JSON Pointer

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
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

Result:
```json
20
```

## Case 2

Input:
```json
{
  "document": [
    1,
    2
  ],
  "pointer": ""
}
```

Result:
```json
[
  1,
  2
]
```

## Case 3

Input:
```json
{
  "document": {
    "": "empty-key"
  },
  "pointer": "/"
}
```

Result:
```json
"empty-key"
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

RFC 6901 escapes tilde as ~0 and slash as ~1. This implementation rejects malformed escapes, invalid array indices and the append marker.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
