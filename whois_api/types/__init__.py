from __future__ import annotations

import datetime
import inspect
import sys
from typing import List, Optional, TypeVar

from pydantic import BaseModel  # pylint: disable=no-name-in-module

A = TypeVar(
    "A",
    bool,
    dict,
    "Language",
    "Feature",
    "FeatureName",
    "Currency",
    "Country",
    "Location",
    "LocationName",
    "LocationAirportCode",
    "LocationLink",
    "IP",
    "UserAgent",
    "Browser",
    "OS",
)


class APIResponse(BaseModel):
    success: bool
    output: List[A]
    execution_time: str


class Language(BaseModel):
    language_alpha_2: Optional[str] = None
    language_alpha_3: str
    name: str
    native_name: Optional[str] = None


class FeatureName(BaseModel):
    language_alpha_3: str
    name: str
    description: str


class Feature(BaseModel):
    fclass: str
    fcode: str
    name: List[FeatureName]

    def get_name_by_lang(self, language_alpha_3: str) -> FeatureName | None:
        name = next(
            filter(
                lambda e: e.language_alpha_3 == language_alpha_3,
                self.name,
            ),
            None,
        )

        if name:
            return name
        if language_alpha_3 != "eng":
            return self.get_name_by_lang(language_alpha_3="eng")
        return None  # pragma: no cover


class Currency(BaseModel):
    currency_alpha_3: str
    currency_alpha_numeric: int
    name: str
    native_name: Optional[str] = None
    symbol: Optional[str] = None


class Country(BaseModel):
    country_alpha_2: str
    country_alpha_numeric: str
    fips: str
    emoji: str
    area: Optional[float] = None
    population: Optional[int] = None
    continent_alpha_2: str
    top_level_domain: Optional[str] = None
    currency_alpha_3: Optional[str] = None
    phone_alpha: Optional[int] = None
    location_id: int


class LocationName(BaseModel):
    language_alpha_3: Optional[str] = None
    name: str
    is_preferred: bool
    is_short: bool
    is_colloquial: bool
    is_historic: bool
    historic_from: Optional[int] = None
    historic_to: Optional[int] = None


class LocationAirportCode(BaseModel):
    airport_code_type: str
    airport_code: str


class LocationLink(BaseModel):
    language_alpha_3: Optional[str] = None
    url: str


class Location(BaseModel):
    location_id: int
    name: List[LocationName]
    latitude: float
    longitude: float
    fcode: Optional[str] = None
    country_alpha_2: Optional[str] = None
    admin_1_location_id: Optional[int] = None
    admin_2_location_id: Optional[int] = None
    population: Optional[int] = None
    elevation: Optional[int] = None
    gtopo30: int
    timezone: Optional[str] = None
    postal_code: List[str]
    abbreviation: List[str]
    airport_code: List[LocationAirportCode]
    link: List[LocationLink]
    updated_at: datetime.date

    def get_name_by_lang(self, language_alpha_3: str) -> LocationName | None:
        name = sorted(
            filter(
                lambda e: e.language_alpha_3 == language_alpha_3 and e.
                is_colloquial is False and e.is_historic is False,
                self.name,
            ),
            key=lambda e: [e.is_preferred, not e.is_short],
            reverse=True,
        )
        if name:
            return name[0]
        if language_alpha_3 != "eng":
            return self.get_name_by_lang(language_alpha_3="eng")
        return None  # pragma: no cover


class IP(BaseModel):
    ip: str
    isp: Optional[str] = None
    organization: Optional[str] = None
    asn: Optional[str] = None
    asn_name: Optional[str] = None
    is_mobile: Optional[bool] = None
    is_proxy: Optional[bool] = None
    is_hosting: Optional[bool] = None
    location: List[Location] = []

    def fmt_location(self, language_alpha_3: str) -> str:
        location_hierarchy = [
            x.get_name_by_lang(language_alpha_3).name for x in self.location
            if x is not None
        ]  # type: ignore
        return ", ".join(
            sorted(set(location_hierarchy), key=location_hierarchy.index))


class Browser(BaseModel):
    family: Optional[str] = None
    version: Optional[str] = None


class OS(BaseModel):
    family: Optional[str] = None
    version: Optional[str] = None


class UserAgent(BaseModel):
    family: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    os: OS
    browser: Browser


APIResponse.model_rebuild()


def dynamic_formatter(obj: dict | bool):
    if isinstance(obj, bool):
        return obj
    for key, value in obj.items():
        if isinstance(value, dict):
            obj[key] = dynamic_formatter(obj=value)
        if isinstance(value, list):
            obj[key] = list(
                map(
                    lambda e: dynamic_formatter(e)
                    if isinstance(e, dict) else e, value))

    if obj.get("class_name"):
        for class_name, model in inspect.getmembers(sys.modules[__name__],
                                                    inspect.isclass):
            if class_name != obj["class_name"]:
                continue
            if not issubclass(model, BaseModel):
                continue

            obj = model(**obj)
            break
        else:
            for class_name, model in inspect.getmembers(
                    sys.modules[__name__ + ".exceptions"], inspect.isclass):
                if class_name != obj["class_name"]:
                    continue
                if not issubclass(model, Exception):
                    continue

                obj = model(**obj)
                break

    return obj
