from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class EDErrorResponse:
    status_code: int
    detail: str | None
    units_charged: int


@dataclass
class EDDataResponse:
    status_code: int
    data: dict | None = field(repr=False)
    units_charged: int
