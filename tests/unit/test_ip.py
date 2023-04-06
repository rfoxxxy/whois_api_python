import logging
import typing

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


class TestIP:
    async def test_ip_info_germany(self, api: "WhoIS"):
        request = await api.ip.info("102.129.156.0", include_continent=True)
        # LOGGER.info(request)
        assert request.location[0].get_name_by_lang("rus").name == "Европа"  # type: ignore
        assert request.location[1].get_name_by_lang("rus").name == "Германия"  # type: ignore

    async def test_ip_info_russia(self, api: "WhoIS"):
        request = await api.ip.info("109.197.88.0", include_continent=True)
        # LOGGER.info(request)
        assert request.location[0].get_name_by_lang("rus").name == "Европа"  # type: ignore
        assert request.location[1].get_name_by_lang("rus").name == "Россия"  # type: ignore
