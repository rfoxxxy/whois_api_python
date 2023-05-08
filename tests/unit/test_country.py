import logging
import typing

import pytest

from whois_api.types.exceptions import MissingValueError

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


class TestCountry:
    async def test_info_exists_exception(self, api: "WhoIS"):
        with pytest.raises(MissingValueError) as exc_info:
            await api.country.info_exists()
        assert (
            exc_info.value.message
            == 'Parameter(s) "country_alpha" or "country_fips" or "country_location_id" must contain value(s).'
        )

    async def test_info_exists_ru(self, api: "WhoIS"):
        request_alpha = await api.country.info_exists(country_alpha="RU")
        request_fips = await api.country.info_exists(country_fips="RS")
        request_location_id = await api.country.info_exists(country_location_id=2017370)
        assert request_alpha is True
        assert request_fips is True
        assert request_location_id is True

    async def test_info_exists_us(self, api: "WhoIS"):
        request_alpha = await api.country.info_exists(country_alpha="US")
        request_fips = await api.country.info_exists(country_fips="US")
        request_location_id = await api.country.info_exists(country_location_id=6252001)
        assert request_alpha is True
        assert request_fips is True
        assert request_location_id is True

    async def test_info_exception(self, api: "WhoIS"):
        with pytest.raises(MissingValueError) as exc_info:
            await api.country.info()
        assert (
            exc_info.value.message
            == 'Parameter(s) "country_alpha" or "country_fips" or "country_location_id" must contain value(s).'
        )

    async def test_info_ru(self, api: "WhoIS"):
        request_alpha = await api.country.info(country_alpha="RU")
        request_fips = await api.country.info(country_fips="RS")
        request_location_id = await api.country.info(country_location_id=2017370)
        assert request_alpha.currency_alpha_3 == "RUB"
        assert request_fips.currency_alpha_3 == "RUB"
        assert request_location_id.currency_alpha_3 == "RUB"
        assert request_alpha == request_fips == request_location_id

    async def test_info_us(self, api: "WhoIS"):
        request_alpha = await api.country.info(country_alpha="US")
        request_fips = await api.country.info(country_fips="US")
        request_location_id = await api.country.info(country_location_id=6252001)
        assert request_alpha.currency_alpha_3 == "USD"
        assert request_fips.currency_alpha_3 == "USD"
        assert request_location_id.currency_alpha_3 == "USD"
        assert request_alpha == request_fips == request_location_id

    async def test_is_neighbour_1_exception(self, api: "WhoIS"):
        with pytest.raises(MissingValueError) as exc_info:
            await api.country.is_neighbour(neighbour_2_country_alpha="US")
        assert (
            exc_info.value.message
            == 'Parameter(s) "neighbour_1_country_alpha" or "neighbour_1_country_fips" or "neighbour_1_country_location_id" must contain value(s).'
        )

    async def test_is_neighbour_2_exception(self, api: "WhoIS"):
        with pytest.raises(MissingValueError) as exc_info:
            await api.country.is_neighbour(neighbour_1_country_alpha="US")
        assert (
            exc_info.value.message
            == 'Parameter(s) "neighbour_2_country_alpha" or "neighbour_2_country_fips" or "neighbour_2_country_location_id" must contain value(s).'
        )

    async def test_is_neighbour_ru_us(self, api: "WhoIS"):
        request = await api.country.is_neighbour(
            neighbour_1_country_alpha="RU", neighbour_2_country_alpha="US"
        )
        assert request is False

    async def test_is_neighbour_us_ca(self, api: "WhoIS"):
        request = await api.country.is_neighbour(
            neighbour_1_country_alpha="US", neighbour_2_country_alpha="CA"
        )
        assert request is True
