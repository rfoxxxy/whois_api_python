from whois_api.methods.base import MethodBase
from whois_api.types import IP


class IPMethod(MethodBase):
    async def info(self, ip: str = None, include_country: bool = True, include_continent: bool = False) -> IP:  # pylint: disable=invalid-name
        return (await self.api_request("info", {"ip": ip,
                                                "include_country": include_country,
                                                "include_continent": include_continent})).output[0]
