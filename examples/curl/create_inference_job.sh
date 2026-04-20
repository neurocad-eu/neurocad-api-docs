#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-https://sandbox.api.neurocad.eu}"
TOKEN="${TOKEN:-replace-me}"
PROJECT_ID="${PROJECT_ID:-prj_demo_001}"

curl -sS \
  -X POST "${BASE_URL}/v1/inference/jobs" \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -d @- <<JSON
{
  "project_id": "${PROJECT_ID}",
  "task": "field-inference",
  "input": {
    "material": "steel-a36",
    "resolution": "medium"
  },
  "labels": ["curl-example"]
}
JSON
