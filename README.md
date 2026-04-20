# neurocad-api-docs

[![API Contract Validation](https://github.com/neurocad-eu/neurocad-api-docs/actions/workflows/validate.yml/badge.svg)](https://github.com/neurocad-eu/neurocad-api-docs/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/neurocad-eu/neurocad-api-docs)](https://github.com/neurocad-eu/neurocad-api-docs/releases)

Public API specifications, integration guides, and SDK references for NeuroCAD.

Docs portal:

- [docs.neurocad.eu](https://docs.neurocad.eu/)

## Purpose

This repository is the public documentation surface for the NeuroCAD integration layer.

It is intended for enterprise teams, technical partners, and internal platform integrators who need a clear contract for how external systems will interact with NeuroCAD.

## Scope

This repository is designed to host:

- versioned OpenAPI and schema artifacts
- authentication and authorization models
- request and response examples
- SDK usage patterns
- integration notes for enterprise workflows
- change logs for externally visible API behavior

## What this repository does not contain

This repository does not expose:

- production kernel internals
- model implementation details
- internal orchestration pipelines
- private deployment or operational systems

The goal is to provide a serious public integration surface without disclosing proprietary implementation details.

## Intended structure

As the public surface expands, this repository will be organized around:

- `openapi/` for versioned API contracts
- `schemas/` for shared request and response schemas
- `examples/` for language-specific usage examples
- `guides/` for integration and authentication documentation
- `postman/` for importer-ready API collections
- `scripts/` for lightweight validation utilities

## Core public documents

- `guides/getting-started.md`
- `guides/authentication.md`
- `guides/environment-separation.md`
- `guides/versioning.md`
- `guides/rate-limits.md`
- `guides/errors.md`
- `guides/webhooks.md`
- `docs/index.html`

## Operational signals

This repository now exposes:

- versioned OpenAPI contract material
- reusable JSON schemas
- Postman-ready import artifacts
- syntax-checked Python, JavaScript, and shell examples
- validation workflow for public contract integrity
- tagged releases for externally visible changes

## Status

Public reference surface in active hardening.

Current public artifacts include:

- draft OpenAPI contract
- reusable JSON schemas
- Python, JavaScript, and curl examples
- Postman collection
- contract validation workflow

## Links

- Organization: [github.com/neurocad-eu](https://github.com/neurocad-eu)
- Website: [neurocad.eu](https://neurocad.eu)
- Contact: [office@neurocad.eu](mailto:office@neurocad.eu)
