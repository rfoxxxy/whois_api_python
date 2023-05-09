import logging
import typing

import pytest

from whois_api.types.exceptions import InvalidValueError

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


class TestCurrency:
    async def test_info_exists_rub(self, api: "WhoIS"):
        request = await api.currency.info_exists("RUB")
        assert request is True

    async def test_info_exists_false(self, api: "WhoIS"):
        with pytest.raises(InvalidValueError) as exc_info:
            await api.currency.info_exists("SMTH")
        assert (
            str(exc_info.value) == 'Parameter(s) "currency_alpha" are invalid.'
        )

    async def test_info_rub(self, api: "WhoIS"):
        request = await api.currency.info("RUB")
        assert request.currency_alpha_3 == "RUB"

    async def test_info_byn(self, api: "WhoIS"):
        request = await api.currency.info("BYN")
        assert request.currency_alpha_3 == "BYN"
