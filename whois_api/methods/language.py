from typing import List

from whois_api.methods.base import MethodBase
from whois_api.types import Language
from whois_api.types.exceptions import APIException


class LanguageMethod(MethodBase):
    async def info_exists(self, language_alpha: str) -> bool:
        return (await self.api_request("info_exists", {"language_alpha": language_alpha})).output[0]

    async def info(self, language_alpha: str) -> Language:
        return (await self.api_request("info", {"language_alpha": language_alpha})).output[0]

    async def list_by_country(self, country_alpha: str | int | None = None,
                              country_fips: str | None = None,
                              country_location_id: int | None = None) -> List[Language]:
        if not country_alpha and not country_fips and not country_location_id:
            raise APIException("one of optional parameters must be used")
        return (await self.api_request("list_by_country", {"country_alpha": country_alpha,
                                                           "country_fips": country_fips,
                                                           "country_location_id": country_location_id})).output

    async def exists_by_country(self, language_alpha: str,
                                country_alpha: str | int | None = None,
                                country_fips: str | None = None,
                                country_location_id: int | None = None) -> List[Language]:
        if not country_alpha and not country_fips and not country_location_id:
            raise APIException("one of optional parameters must be used")
        return (await self.api_request("exists_by_country", {"language_alpha": language_alpha,
                                                             "country_alpha": country_alpha,
                                                             "country_fips": country_fips,
                                                             "country_location_id": country_location_id})).output[0]
