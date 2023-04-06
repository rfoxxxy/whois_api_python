
from typing import List

from whois_api.methods.base import MethodBase
from whois_api.types import Location


class LocationMethod(MethodBase):
    async def info_exists(self, location_id: int) -> bool:
        return (await self.api_request("info_exists", {"location_id": location_id})).output[0]

    async def info(self, location_id: int) -> Location:
        return (await self.api_request("info", {"location_id": location_id})).output[0]

    async def hierarchy(self, location_id: int, include_country: bool = True, include_continent: bool = False) -> List[Location]:
        return (await self.api_request("hierarchy", {"location_id": location_id,
                                                     "include_country": include_country,
                                                     "include_continent": include_continent})).output
