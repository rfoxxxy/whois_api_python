import logging
import typing

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


class TestLocation:
    async def test_info_exists_moscow(self, api: "WhoIS"):
        request = await api.location.info_exists(524894)
        assert request is True

    async def test_info_exists_false(self, api: "WhoIS"):
        request = await api.location.info_exists(0)
        assert request is False

    async def test_info_moscow(self, api: "WhoIS"):
        request = await api.location.info(524894)
        assert request.get_name_by_lang("rus").name == "Москва"  # type: ignore
        assert request.timezone == "Europe/Moscow"

    async def test_info_ny(self, api: "WhoIS"):
        request = await api.location.info(5128581)
        assert request.get_name_by_lang("rus").name == "Нью-Йорк"  # type: ignore
        assert request.timezone == "America/New_York"

    async def test_hierarchy_moscow(self, api: "WhoIS"):
        request = await api.location.hierarchy(524894)
        assert len(request) > 0

    async def test_hierarchy_ny(self, api: "WhoIS"):
        request = await api.location.hierarchy(5128581)
        assert len(request) > 0
