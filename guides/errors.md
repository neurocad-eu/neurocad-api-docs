# Error Semantics

## Envelope

The draft public API returns errors in a stable envelope:

```json
{
  "error": {
    "code": "not_found",
    "message": "Requested resource does not exist."
  }
}
```

## Public error classes

- `unauthorized`
- `forbidden`
- `not_found`
- `validation_error`
- `rate_limited`
- `internal_error`

## Guidance for integrators

- treat `code` as the stable machine field
- treat `message` as human-readable diagnostic text
- do not build control flow on full message strings
- log request identifiers where available
