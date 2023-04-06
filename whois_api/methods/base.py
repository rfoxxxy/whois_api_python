import typing

from whois_api.types import APIResponse
from whois_api.types.exceptions import APIException

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover


class MethodBase:
    def __init__(self, name: str, client_instance: "WhoIS"):
        self.category_name = name
        self.__api = client_instance

    def make_method_name(self, method_name: str) -> str:
        return f"{self.category_name}.{method_name}"

    async def api_request(self, method_name: str, params: dict | None) -> APIResponse:
        response = await self.__api._make_request(self.make_method_name(method_name), params)  # pylint: disable=protected-access
        if not response.success:
            raise APIException(response.output[0].message)
        return response
