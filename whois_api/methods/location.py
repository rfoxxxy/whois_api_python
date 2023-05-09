from typing import List

from whois_api.methods.base import MethodBase
from whois_api.types import Location


class LocationMethod(MethodBase):
    category_name = "location"

    async def info_exists(self, location_id: int) -> bool:
        """The method allows you to check the existence of information about a geographical object by the location_id parameter.

        Args:
            location_id (int): A unique identifier of a geographical object in the GeoNames database,
                which consists of digits. For example, 524894 is the location_id for Moscow.

        Returns:
            bool: Information existence
        """
        return (
            await self.api_request("info_exists", {"location_id": location_id})
        ).output[0]

    async def info(self, location_id: int) -> Location:
        """The method allows you to get information about a geographical object by the location_id parameter.

        Args:
            location_id (int): A unique identifier of a geographical object in the GeoNames database,
                which consists of digits. For example, 524894 is the location_id for Moscow.

        Returns:
            Location: Location Information object
        """
        return (
            await self.api_request("info", {"location_id": location_id})
        ).output[0]

    async def hierarchy(
        self,
        location_id: int,
        include_country: bool = True,
        include_continent: bool = False,
    ) -> List[Location]:
        """The method allows you to get a hierarchy of geographical objects by the location_id parameter.

        Args:
            location_id (int): A unique identifier of a geographical object in the GeoNames database,
                which consists of digits. For example, 524894 is the location_id for Moscow.
            include_country (bool, optional): The parameter determines whether the country should be included in the hierarchy of locations.
                Defaults to True.
            include_continent (bool, optional): The parameter determines whether to include the continent in the hierarchy of locations.
                Defaults to False.

        Returns:
            List[Location]: List of Location objects
        """
        return (
            await self.api_request(
                "hierarchy",
                {
                    "location_id": location_id,
                    "include_country": include_country,
                    "include_continent": include_continent,
                },
            )
        ).output
