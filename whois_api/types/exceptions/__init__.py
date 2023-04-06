from dataclasses import dataclass, field


@dataclass
class APIException(Exception):
    message: str | None = field(default=None)
