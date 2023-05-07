from whois_api.methods.base import MethodBase
from whois_api.types import Feature


class FeatureMethod(MethodBase):
    async def info_exists(self, fcode: str) -> bool:
        """The method allows you to check the existence of information about the classification of geographical objects by the fcode parameter.

        Args:
            fcode (str): Identifier for classifying geographical objects by type and characteristics.
                For example, PPL is a feature code for a city, and STM is for a stream.
                There are 9 feature classes and 645 feature codes in total.
                Most feature codes match the codes used by the US National Geospatial-Intelligence Agency (NGA). Not case sensitive.

        Returns:
            bool: Feature existence
        """
        return (
            await self.api_request("info_exists", {"fcode": fcode})
        ).output[0]

    async def info(self, fcode: str) -> Feature:
        """The method allows you to get information about the classification of geographical objects by the fcode parameter.

        Args:
            fcode (str): Identifier for classifying geographical objects by type and characteristics.
                For example, PPL is a feature code for a city, and STM is for a stream.
                There are 9 feature classes and 645 feature codes in total.
                Most feature codes match the codes used by the US National Geospatial-Intelligence Agency (NGA). Not case sensitive.

        Returns:
            Feature: Feature Information object
        """
        return (await self.api_request("info", {"fcode": fcode})).output[0]
