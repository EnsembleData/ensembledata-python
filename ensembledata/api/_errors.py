from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EDError(Exception):
    status_code: int
    detail: str | None
    units_charged: int
