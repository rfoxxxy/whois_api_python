from whois_api.methods.base import MethodBase
from whois_api.types import Feature


class FeatureMethod(MethodBase):
    async def info(self, fcode: str) -> Feature:
        return (await self.api_request("info", {"fcode": fcode})).output[0]
