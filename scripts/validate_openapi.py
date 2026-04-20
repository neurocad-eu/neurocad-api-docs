from __future__ import annotations

from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
OPENAPI_PATH = ROOT / "openapi" / "openapi.yaml"


def main() -> None:
    with OPENAPI_PATH.open("r", encoding="utf-8") as handle:
        document = yaml.safe_load(handle)

    assert document["openapi"].startswith("3.1"), "OpenAPI version must be 3.1.x"
    assert "paths" in document and document["paths"], "Specification must define paths"

    path_count = len(document["paths"])
    assert path_count >= 5, "Specification should expose at least five public paths"

    draft = {
        "type": "object",
        "required": ["openapi", "info", "paths", "components"],
    }
    Draft202012Validator(draft).validate(document)
    print(f"Validated OpenAPI draft with {path_count} paths")


if __name__ == "__main__":
    main()
