#!/usr/bin/env python3
"""Check the axiom dependencies reported by Lean for the principal declarations."""

from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "Checks" / "Axioms.lean"
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
REPORT = re.compile(
    r"'([^'\n]+)' (?:depends on axioms:\s*\[([^\]]*)\]|"
    r"does not depend on (?:any )?axioms)",
    re.MULTILINE,
)


def validate(output, expected):
    """Require one report per declaration and no axiom outside the allowlist."""
    observed = {}
    for match in REPORT.finditer(output):
        name = match.group(1)
        if name in observed:
            raise ValueError(f"Repeated axiom report: {name}")
        axioms = {item.strip() for item in (match.group(2) or "").split(",") if item.strip()}
        extra = axioms - ALLOWED
        if extra:
            raise ValueError(f"Unexpected axiom dependencies for {name}: {', '.join(sorted(extra))}")
        observed[name] = axioms
    missing = set(expected) - set(observed)
    unexpected = set(observed) - set(expected)
    if missing or unexpected:
        details = []
        if missing:
            details.append("Missing reports: " + ", ".join(sorted(missing)))
        if unexpected:
            details.append("Unexpected reports: " + ", ".join(sorted(unexpected)))
        raise ValueError("; ".join(details))
    return len(observed)


def main():
    expected = re.findall(r"^\s*#print axioms\s+(\S+)\s*$", AUDIT.read_text(), re.MULTILINE)
    if not expected or len(expected) != len(set(expected)):
        print("The audit inventory must contain distinct declarations.", file=sys.stderr)
        return 1
    try:
        result = subprocess.run(
            ["lake", "env", "lean", str(AUDIT.relative_to(ROOT))],
            cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
        )
    except OSError as error:
        print(f"Could not run Lake: {error}", file=sys.stderr)
        return 1
    print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.returncode:
        print(f"Lean exited with status {result.returncode}.", file=sys.stderr)
        return 1
    try:
        count = validate(result.stdout, expected)
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 1
    print(f"Verified {count} declarations; all reported axiom dependencies are within the allowlist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
