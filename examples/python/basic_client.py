"""Minimal draft client for the NeuroCAD public API."""

from __future__ import annotations

import json
from urllib import request


BASE_URL = "https://sandbox.api.neurocad.eu"


def post_json(path: str, payload: dict, token: str | None = None) -> dict:
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = request.Request(f"{BASE_URL}{path}", data=data, headers=headers, method="POST")
    with request.urlopen(req) as response:  # noqa: S310 - public draft example
        return json.loads(response.read().decode("utf-8"))


def issue_token(client_id: str, client_secret: str) -> str:
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": "enterprise-api",
    }
    response = post_json("/v1/auth/token", payload)
    return response["access_token"]


def submit_job(token: str, project_id: str) -> dict:
    payload = {
        "project_id": project_id,
        "task": "solver-export",
        "input": {
            "material": "aluminum-6061",
            "export_format": "solver-bundle",
        },
        "labels": ["public-example"],
    }
    return post_json("/v1/inference/jobs", payload, token=token)


if __name__ == "__main__":
    print("Draft public example. Replace placeholder credentials before use.")
    token = issue_token("partner_demo", "replace-in-production")
    job = submit_job(token, "prj_demo_001")
    print(json.dumps(job, indent=2))
