from whois_api.methods.base import MethodBase
from whois_api.types import IP


class IPMethod(MethodBase):
    async def info(
        self,
        ip: str | None = None,
        include_country: bool = True,
        include_continent: bool = False,
    ) -> IP:  # pylint: disable=invalid-name
        """The method allows you to get information about the IP by the ip parameter.

        Args:
            ip (str, optional): IPv4 or IPv6 device identifier on the Internet,
                written in decimal format with delimiters.
                For example, 192.168.0.1 or 8.8.8.8. Defaults to None.
            include_country (bool, optional): The parameter determines whether the country should be included in the hierarchy of locations.
                Defaults to True.
            include_continent (bool, optional): The parameter determines whether to include the continent in the hierarchy of locations.
                Defaults to False.

        Returns:
            IP: IP Information object
        """
        return (
            await self.api_request(
                "info",
                {
                    "ip": ip,
                    "include_country": include_country,
                    "include_continent": include_continent,
                },
            )
        ).output[0]
