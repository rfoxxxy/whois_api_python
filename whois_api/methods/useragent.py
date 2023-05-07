from whois_api.methods.base import MethodBase
from whois_api.types import UserAgent


class UserAgentMethod(MethodBase):
    async def info(self, useragent: str | None = None) -> UserAgent:
        """The method allows you to get information about the user's browser and operating system by the useragent parameter.

        Args:
            useragent (str, optional): A string that identifies the browser type and version, operating system, and other user characteristics.
                For example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36.
                If no useragent is specified, the value is taken from the header. Defaults to None.

        Returns:
            UserAgent: UserAgent Information object
        """
        return (
            await self.api_request("info", {"useragent": useragent})
        ).output[0]
