from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Union


@dataclass
class EDErrorResponse:
    status_code: int
    detail: str | None
    units_charged: int


@dataclass
class EDDataResponse:
    status_code: int
    data: Any = field(repr=False)
    units_charged: int


EDResponse = Union[EDDataResponse, EDErrorResponse]
