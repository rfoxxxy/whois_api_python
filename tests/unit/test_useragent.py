import logging
import typing

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


class TestUserAgent:
    async def test_info_none(self, api: "WhoIS"):
        request = await api.useragent.info()
        assert request.os.family == "Other"
        assert request.browser.family == "Other"

    async def test_info_mac_safari(self, api: "WhoIS"):
        request = await api.useragent.info("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15")
        assert request.os.family == "Mac OS X"
        assert request.os.version == "10.15.7"
        assert request.browser.family == "Safari"
        assert request.browser.version == "16.2"
