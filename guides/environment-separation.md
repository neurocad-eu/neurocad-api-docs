# Environment Separation

## Public stance

NeuroCAD treats sandbox and production as separate trust domains.

## Integration rules

- do not reuse credentials across environments
- keep sandbox callbacks and production callbacks separate
- keep environment-specific artifact stores separate
- log the environment alongside job identifiers in downstream systems

## Public endpoints

- production: `https://api.neurocad.eu`
- sandbox: `https://sandbox.api.neurocad.eu`

## Change discipline

Public contracts may evolve in sandbox before production promotion.

Consumers should validate:

- authentication flow
- payload shape
- polling logic
- webhook handling

in sandbox first.
