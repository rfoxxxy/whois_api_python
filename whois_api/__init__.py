
from email import header

import httpx
import orjson
import pkg_resources

from whois_api.methods.country import CountryMethod
from whois_api.methods.currency import CurrencyMethod
from whois_api.methods.feature import FeatureMethod
from whois_api.methods.ip import IPMethod
from whois_api.methods.language import LanguageMethod
from whois_api.methods.location import LocationMethod
from whois_api.methods.useragent import UserAgentMethod
from whois_api.types import APIResponse

__version__ = pkg_resources.get_distribution('whois_api').version


class WhoIS:  # pylint: disable=too-many-instance-attributes
    def __init__(self, api_url: str, api_timeout: int = 10) -> None:
        self.api_url = api_url.rstrip("/")
        self.api_timeout = api_timeout
        self.country = CountryMethod("country", self)
        self.currency = CurrencyMethod("currency", self)
        self.feature = FeatureMethod("feature", self)
        self.ip = IPMethod("ip", self)  # pylint: disable=invalid-name
        self.language = LanguageMethod("language", self)
        self.location = LocationMethod("location", self)
        self.useragent = UserAgentMethod("useragent", self)

    def __repr__(self) -> str:  # pragma: no cover
        return f'<WhoIS at {hex(id(self))}>'  # yapf: disable

    async def _make_request(self, method: str, params: dict | None):
        async with httpx.AsyncClient(headers={"User-Agent": f"whois_api/v{__version__}"}) as client:
            request = client.build_request("GET",
                                           f"{self.api_url}/api/{method}",
                                           params={k: v for k, v in params.items() if v is not None} if params else None,
                                           timeout=self.api_timeout)
            response = await client.send(request)
            return APIResponse(**orjson.loads(response.content))  # pylint: disable=no-member
