from whois_api.methods import MethodBase
from whois_api.types import Currency


class CurrencyMethod(MethodBase):
    async def info_exists(self, currency_alpha: str | int) -> bool:
        """The method allows you to check the existence of currency information by the currency_alpha parameter.

        Args:
            currency_alpha (str | int): A three-letter or numeric currency code according to the ISO 4217 standard,
                for example, USD for the US dollar or EUR for the euro. Not case sensitive.

        Returns:
            bool: Currency existence
        """
        return (await self.api_request("info_exists", {"currency_alpha": currency_alpha})).output[0]

    async def info(self, currency_alpha: str | int) -> Currency:
        """The method allows you to get information about the currency by the currency_alpha parameter.

        Args:
            currency_alpha (str | int): A three-letter or numeric currency code according to the ISO 4217 standard,
                for example, USD for the US dollar or EUR for the euro. Not case sensitive.

        Returns:
            Currency: Currency Information object
        """
        return (await self.api_request("info", {"currency_alpha": currency_alpha})).output[0]
