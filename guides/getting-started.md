# Getting Started

## Minimum public integration loop

1. exchange client credentials for a bearer token
2. create or resolve a project container
3. submit an inference or export job
4. poll job state or receive a webhook
5. resolve artifact metadata and download references

## Recommended reading order

1. `guides/authentication.md`
2. `guides/environment-separation.md`
3. `guides/versioning.md`
4. `guides/rate-limits.md`
5. `guides/errors.md`
6. `guides/webhooks.md`

## Public artifacts to start with

- `openapi/openapi.yaml`
- `postman/neurocad-api.postman_collection.json`
- `examples/python/basic_client.py`
- `examples/javascript/basic_client.mjs`
- `examples/curl/create_inference_job.sh`

## Intended usage

The public API surface is designed for:

- enterprise integration planning
- sandbox onboarding
- SDK and connector development
- technical diligence and contract review
