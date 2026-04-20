# Webhooks

## Intended use

The public NeuroCAD integration surface is designed to support webhook-oriented delivery for long-running jobs and artifact availability notifications.

Typical events:

- `job.completed`
- `job.failed`
- `artifact.available`

## Recommended receiver behavior

- verify signatures before processing
- separate sandbox and production endpoints
- store event identifiers to prevent duplicate processing
- acknowledge quickly and process asynchronously when possible

## Current status

Webhook payload structure is still draft-level and will be published as the public event contract is finalized.
