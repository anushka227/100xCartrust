"""Compare user-submitted values with mocked API payloads."""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any

from field_config import FIELDS, FieldSpec


def _norm_text(s: str) -> str:
    s = (s or "").strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s


def _norm_digits(s: str) -> str:
    return re.sub(r"\D", "", s or "")


def _parse_date(s: str) -> datetime | None:
    s = (s or "").strip()
    for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def field_match_score(user: str, verified: str, spec: FieldSpec) -> float:
    """Return 0.0–100.0 similarity score."""
    u_raw = user or ""
    v_raw = verified or ""

    if spec.input_type == "number":
        u = _norm_digits(u_raw)
        v = _norm_digits(v_raw)
        if not u and not v:
            return 100.0
        if u == v:
            return 100.0
        try:
            if int(u) == int(v):
                return 100.0
        except ValueError:
            pass
        return 0.0

    if spec.input_type == "date":
        du, dv = _parse_date(u_raw), _parse_date(v_raw)
        if du and dv and du.date() == dv.date():
            return 100.0
        if _norm_text(u_raw) == _norm_text(v_raw):
            return 100.0
        return 0.0

    # text / textarea
    if _norm_text(u_raw) == _norm_text(v_raw):
        return 100.0

    u_d = _norm_digits(u_raw)
    v_d = _norm_digits(v_raw)
    if u_d and v_d and u_d == v_d:
        return 85.0

    return 0.0


def build_rows(
    user_values: dict[str, str],
    rto: dict[str, Any],
    insurance: dict[str, Any],
    third_party: dict[str, Any],
) -> list[dict[str, Any]]:
    api_by_source = {
        "rto": rto.get("data", {}),
        "insurance": insurance.get("data", {}),
        "third_party": third_party.get("data", {}),
    }
    rows: list[dict[str, Any]] = []
    for spec in FIELDS:
        user_val = user_values.get(spec.key, "")
        verified_val = str(api_by_source[spec.source].get(spec.key, "") or "")
        score = field_match_score(user_val, verified_val, spec)
        rows.append(
            {
                "key": spec.key,
                "label": spec.label,
                "source": spec.source,
                "user": user_val,
                "verified": verified_val,
                "score": round(score, 1),
                "matched": score >= 99.9,
            }
        )
    return rows


def overall_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    matched = sum(1 for r in rows if r["matched"])
    total = len(rows)
    avg = sum(r["score"] for r in rows) / total if total else 0.0
    return {
        "matched": matched,
        "total": total,
        "avg_percent": round(avg, 1),
    }
