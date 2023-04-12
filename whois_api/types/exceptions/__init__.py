from dataclasses import dataclass, field


@dataclass
class APIException(Exception):
    message: str | None = field(default=None)


@dataclass
class OptionalParameterError(Exception):
    message: str | None = field(default=None)


@dataclass
class NotFoundError(Exception):
    message: str | None = field(default=None)
