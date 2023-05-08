from dataclasses import dataclass, field
from typing import List


@dataclass
class APIError(Exception):
    status_code: int = field()
    message: str = field()

    def __post_init__(self):
        super().__init__(self.message)


@dataclass
class UnexpectedError(APIError):
    pass


@dataclass
class TooManyRequestsError(APIError):
    retry_after: int = field()


@dataclass
class MissingValueError(APIError):
    parameters: List[str] = field()


@dataclass
class InvalidValueError(APIError):
    parameters: List[str] = field()


@dataclass
class TooManyParametersError(APIError):
    pass


@dataclass
class CountryNotFoundError(APIError):
    pass


@dataclass
class CurrencyNotFoundError(APIError):
    pass


@dataclass
class FeatureNotFoundError(APIError):
    pass


@dataclass
class LanguageNotFoundError(APIError):
    pass


@dataclass
class LocationNotFoundError(APIError):
    pass
