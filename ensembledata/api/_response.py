from dataclasses import dataclass, field
from typing import Any


@dataclass
class EDResponse:
    status_code: int
    data: Any = field(repr=False)
    units_charged: int
