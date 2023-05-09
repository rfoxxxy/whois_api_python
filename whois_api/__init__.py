import inspect

import httpx_cache
import orjson
import pkg_resources

from whois_api.methods import (
    CountryMethod,
    CurrencyMethod,
    FeatureMethod,
    IPMethod,
    LanguageMethod,
    LocationMethod,
    UserAgentMethod,
)
from whois_api.types import APIResponse, exceptions

__version__ = pkg_resources.get_distribution("whois_api").version


class WhoIS:  # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        api_url: str = "https://whois.neonteam.cc",
        api_timeout: int = 60,
        use_cache: bool = True,
        cache_time: int = 900,
    ) -> None:
        """WhoIS API Wrapper main class

        Args:
            api_url (str, optional): API URL. Defaults to "https://whois.neonteam.cc".
            api_timeout (int, optional): API response timeout. Defaults to 60.
            use_cache (bool, optional): Use response caching. Defaults to True.
            cache_time (int, optional): Cache time in seconds. Defaults to 900.
        """
        self.api_url = api_url.rstrip("/")
        self.api_timeout = api_timeout
        self.use_cache = use_cache
        self.cache_time = cache_time
        self.country = CountryMethod(self)
        self.currency = CurrencyMethod(self)
        self.feature = FeatureMethod(self)
        self.ip = IPMethod(self)  # pylint: disable=invalid-name
        self.language = LanguageMethod(self)
        self.location = LocationMethod(self)
        self.useragent = UserAgentMethod(self)

    def __repr__(self) -> str:  # pragma: no cover
        return (
            f"<{self.__class__.__name__} at {hex(id(self))}>"  # yapf: disable
        )

    async def _make_request(self, method: str, params: dict | None):
        async with httpx_cache.AsyncClient(
            headers={
                "User-Agent": f"whois_api/v{__version__}",
                "cache-control": f"max-age={self.cache_time}"
                if self.use_cache
                else "no-cache",
            },
            cache=httpx_cache.FileCache(),
        ) as client:
            request = client.build_request(
                "GET",
                f"{self.api_url}/api/{method}",
                params={k: v for k, v in params.items() if v is not None}
                if params
                else None,
                timeout=self.api_timeout,
            )
            response = await client.send(request)
            data = orjson.loads(response.content)  # pylint: disable=no-member
            if not data["success"] and len(data["output"]) == 1:
                known_exception = (
                    any(  # doing magic and probably needs rewrite
                        (exception_class := obj)
                        and name == data["output"][0]["class_name"]
                        for name, obj in [
                            (name, obj)
                            for name, obj in inspect.getmembers(
                                exceptions, inspect.isclass
                            )
                            if obj.__module__ == "whois_api.types.exceptions"
                        ]
                    )
                )
                if known_exception:
                    data_dicted = dict(
                        filter(
                            lambda e: e[0] != "class_name",
                            data["output"][0].items(),
                        )
                    )
                    raise exception_class(**dict(data_dicted))
                raise exceptions.UnexpectedError(  # pragma: no cover
                    status_code=data["output"][0].get("status_code", 503),
                    message=data["output"][0].get("message", ""),
                )
            return APIResponse(**data)
