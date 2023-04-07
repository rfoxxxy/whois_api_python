from __future__ import annotations

import datetime
from typing import List, Optional, TypeVar, Union

from pydantic import BaseModel  # pylint: disable=no-name-in-module

A = TypeVar("A", bool, "APIError", "Language", "Feature", "FeatureName", "Currency", "Country",
            "Location", "LocationName", "LocationAirportCode", "LocationLink", "IP",
            "UserAgent", "Browser", "OS")


class APIResponse(BaseModel):
    success: bool
    output: List[A]
    execution_time: str
    throttling_time: str


class APIError(BaseModel):
    parameters: List[str]
    status_code: int
    message: str


class Language(BaseModel):
    language_alpha_2: Optional[str]
    language_alpha_3: str
    name: str
    native_name: Optional[str]


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
            ), None
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
    native_name: Optional[str]
    symbol: Optional[str]


class Country(BaseModel):
    country_alpha_2: str
    country_alpha_numeric: str
    fips: str
    emoji: str
    area: Optional[float]
    population: Optional[int]
    continent_alpha_2: str
    top_level_domain: Optional[str]
    currency_alpha_3: Optional[str]
    phone_alpha: Optional[int]
    location_id: int


class LocationName(BaseModel):
    language_alpha_3: Optional[str]
    name: str
    is_preferred: bool
    is_short: bool
    is_colloquial: bool
    is_historic: bool
    historic_from: Optional[int]
    historic_to: Optional[int]


class LocationAirportCode(BaseModel):
    airport_code_type: str
    airport_code: str


class LocationLink(BaseModel):
    language_alpha_3: Optional[str]
    url: str


class Location(BaseModel):
    location_id: int
    name: List[LocationName]
    latitude: float
    longitude: float
    fcode: Optional[str]
    country_alpha_2: Optional[str]
    admin_1_location_id: Optional[int]
    admin_2_location_id: Optional[int]
    population: Optional[int]
    elevation: Optional[int]
    gtopo30: int
    timezone: Optional[str]
    postal_code: List[str]
    abbreviation: List[str]
    airport_code: List[LocationAirportCode]
    link: List[LocationLink]
    updated_at: datetime.date

    def get_name_by_lang(self, language_alpha_3: str) -> LocationName | None:
        name = sorted(
            filter(
                lambda e: e.language_alpha_3 == language_alpha_3
                and e.is_colloquial is False
                and e.is_historic is False,
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
        location_hierarchy = [x.get_name_by_lang(language_alpha_3).name for x in self.location if x is not None]  # type: ignore
        return ", ".join(sorted(set(location_hierarchy), key=location_hierarchy.index))


class Browser(BaseModel):
    family: Optional[str]
    version: Optional[str]


class OS(BaseModel):
    family: Optional[str]
    version: Optional[str]


class UserAgent(BaseModel):
    family: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    os: OS
    browser: Browser


APIResponse.update_forward_refs()
