from whois_api.methods.base import MethodBase
from whois_api.types import Currency


class CurrencyMethod(MethodBase):
    async def info_exists(self, currency_alpha: str | int) -> bool:
        return (await self.api_request("info_exists", {"currency_alpha": currency_alpha})).output[0]

    async def info(self, currency_alpha: str | int) -> Currency:
        return (await self.api_request("info", {"currency_alpha": currency_alpha})).output[0]
