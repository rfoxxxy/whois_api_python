import logging
import typing

import pytest

from whois_api.types.exceptions import OptionalParameterError

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


class TestLanguage:
    async def test_info_exists_rus(self, api: "WhoIS"):
        request = await api.language.info_exists("ru")
        assert request is True

    async def test_info_exists_false(self, api: "WhoIS"):
        request = await api.language.info_exists("smth")
        assert request is False

    async def test_info_ru(self, api: "WhoIS"):
        request = await api.language.info("ru")
        assert request.name == "Russian"
        assert request.native_name == "Русский"
        assert request.language_alpha_3 == "rus"

    async def test_info_eng(self, api: "WhoIS"):
        request = await api.language.info("eng")
        assert request.name == "English"
        assert request.language_alpha_3 == "eng"

    async def test_list_by_country_exception(self, api: "WhoIS"):
        with pytest.raises(OptionalParameterError) as exc_info:
            await api.language.list_by_country()
        assert str(exc_info.value) == 'one of optional parameters must be used'

    async def test_list_by_country_ru(self, api: "WhoIS"):
        request = await api.language.list_by_country("ru")
        assert len(request) > 0
        assert request[0].name == "Russian"
        assert request[0].native_name == "Русский"
        assert request[0].language_alpha_3 == "rus"

    async def test_list_by_country_us(self, api: "WhoIS"):
        request = await api.language.list_by_country("us")
        assert len(request) > 0
        assert request[0].name == "English"
        assert request[0].language_alpha_3 == "eng"

    async def test_exists_by_country_exception(self, api: "WhoIS"):
        with pytest.raises(OptionalParameterError) as exc_info:
            await api.language.exists_by_country("ru")
        assert str(exc_info.value) == 'one of optional parameters must be used'

    async def test_exists_by_country_ru_ru(self, api: "WhoIS"):
        request = await api.language.exists_by_country("ru", "ru")
        assert request is True

    async def test_not_exists_by_country_ru_us(self, api: "WhoIS"):
        request = await api.language.exists_by_country("ru", "us")
        assert request is False
