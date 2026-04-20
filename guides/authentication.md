# Authentication

## Overview

The draft public NeuroCAD API uses bearer-token authentication for machine-to-machine integrations.

The current public contract is designed for:

- enterprise platform connectors
- evaluation environments
- controlled partner integrations

## Token exchange

Clients exchange `client_id` and `client_secret` for a short-lived bearer token through:

- `POST /v1/auth/token`

Example request body:

```json
{
  "client_id": "partner_demo",
  "client_secret": "replace-in-production",
  "audience": "enterprise-api"
}
```

## Authorization header

Use the returned token in the `Authorization` header:

```http
Authorization: Bearer <token>
```

## Integration guidance

- keep credentials out of source control
- rotate credentials by environment
- use dedicated credentials per integration surface
- treat sandbox and production credentials as separate trust domains

## Current status

Public draft.

The exact provisioning workflow, role model, and onboarding flow may evolve as the public integration surface is finalized.
