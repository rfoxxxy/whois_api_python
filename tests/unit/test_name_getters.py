import logging
import typing

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


async def test_feature_name_getter(api: "WhoIS"):
    request = await api.feature.info("PPL")
    assert request.get_name_by_lang("rus").name == "населенный пункт"  # type: ignore
    assert request.get_name_by_lang("smth").name == "populated place"  # type: ignore


async def test_location_name_getter(api: "WhoIS"):
    request = await api.location.info(524894)
    assert request.get_name_by_lang("rus").name == "Москва"  # type: ignore
    assert request.get_name_by_lang("smth").name == "Moscow"  # type: ignore
