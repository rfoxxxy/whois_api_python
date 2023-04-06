
from whois_api.methods.base import MethodBase
from whois_api.types import UserAgent


class UserAgentMethod(MethodBase):
    async def info(self, useragent: str | None = None) -> UserAgent:
        return (await self.api_request("info", {"useragent": useragent})).output[0]
