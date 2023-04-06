from whois_api.methods.base import MethodBase
from whois_api.types import Country
from whois_api.types.exceptions import APIException


class CountryMethod(MethodBase):
    async def info_exists(self, country_alpha: str | int | None = None,
                          country_fips: str | None = None,
                          country_location_id: int | None = None) -> bool:
        if not country_alpha and not country_fips and not country_location_id:
            raise APIException("one of optional parameters must be used")
        return (await self.api_request("info_exists", {"country_alpha": country_alpha,
                                                       "country_fips": country_fips,
                                                       "country_location_id": country_location_id})).output[0]

    async def info(self, country_alpha: str | int | None = None,
                   country_fips: str | None = None,
                   country_location_id: int | None = None) -> Country:
        if not country_alpha and not country_fips and not country_location_id:
            raise APIException("one of optional parameters must be used")
        return (await self.api_request("info", {"country_alpha": country_alpha,
                                                "country_fips": country_fips,
                                                "country_location_id": country_location_id})).output[0]

    async def is_neighbour(self, neighbour_1_country_alpha: str | int | None = None,  # pylint: disable=too-many-arguments
                           neighbour_1_country_fips: str | None = None,
                           neighbour_1_country_location_id: int | None = None,
                           neighbour_2_country_alpha: str | int | None = None,
                           neighbour_2_country_fips: str | None = None,
                           neighbour_2_country_location_id: int | None = None) -> bool:
        if not neighbour_1_country_alpha and not neighbour_1_country_fips and not neighbour_1_country_location_id:
            raise APIException("one of optional parameters must be used for neighbour_1")
        if not neighbour_2_country_alpha and not neighbour_2_country_fips and not neighbour_2_country_location_id:
            raise APIException("one of optional parameters must be used for neighbour_2")
        return (await self.api_request("is_neighbour", {"neighbour_1_country_alpha": neighbour_1_country_alpha,
                                                        "neighbour_1_country_fips": neighbour_1_country_fips,
                                                        "neighbour_1_country_location_id": neighbour_1_country_location_id,
                                                        "neighbour_2_country_alpha": neighbour_2_country_alpha,
                                                        "neighbour_2_country_fips": neighbour_2_country_fips,
                                                        "neighbour_2_country_location_id": neighbour_2_country_location_id})).output[0]
