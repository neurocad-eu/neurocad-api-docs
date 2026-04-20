# Rate Limits

## Public posture

The draft public API is intended for controlled enterprise integrations rather than anonymous bulk traffic.

## Expected behavior

Clients should expect:

- per-client rate controls
- burst protection on token issuance
- backoff requirements after `429` responses
- stricter limits in sandbox than in production planning

## Client guidance

- cache bearer tokens until expiry
- use bounded polling intervals
- prefer webhooks for completion signaling
- implement exponential backoff with jitter after `429`

## Current status

The exact numeric limits are not committed in the public draft yet.

This guide documents the expected client posture so partner implementations are resilient before production onboarding.
