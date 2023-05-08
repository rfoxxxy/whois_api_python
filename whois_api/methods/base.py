import typing

from whois_api.types import APIResponse

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover


class MethodBase:
    def __init__(self, name: str, client_instance: "WhoIS"):
        self.category_name = name
        self.__api = client_instance

    def make_method_name(self, method_name: str) -> str:
        return f"{self.category_name}.{method_name}"

    async def api_request(self, method_name: str, params: dict | None) -> APIResponse:
        """Make raw API request

        Args:
            method_name (str): API method name according to https://whois.neonteam.cc/docs
            params (dict, optional): Request params

        Raises:
            APIException: API error message

        Returns:
            APIResponse: API response object
        """
        response = await self.__api._make_request(  # pylint: disable=protected-access
            self.make_method_name(method_name), params
        )

        return response
