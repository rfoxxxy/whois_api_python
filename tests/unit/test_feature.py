import logging
import typing

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


class TestFeature:
    async def test_info_exists_ppl(self, api: "WhoIS"):
        request = await api.feature.info_exists("PPL")
        assert request is True

    async def test_info_exists_false(self, api: "WhoIS"):
        request = await api.feature.info_exists("SMTH")
        assert request is False

    async def test_info_ppl(self, api: "WhoIS"):
        request = await api.feature.info("PPL")
        assert request.fclass == "P"
        assert request.fcode == "PPL"
        assert request.get_name_by_lang("rus").name == "населенный пункт"  # type: ignore
        assert request.get_name_by_lang("rus").description == "место, где живут люди (город, село, поселок и т. п.)"  # type: ignore
