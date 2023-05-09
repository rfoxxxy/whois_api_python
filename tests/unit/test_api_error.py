import logging
import typing

import pytest

from whois_api.types.exceptions import LocationNotFoundError, MissingValueError

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


async def test_api_error(api: "WhoIS"):
    with pytest.raises(MissingValueError) as exc_info:
        await api.location.api_request("info", {})
    assert (
        exc_info.value.message
        == 'Parameter(s) "location_id" must contain value(s).'
    )


async def test_api_not_found_error(api: "WhoIS"):
    with pytest.raises(LocationNotFoundError) as exc_info:
        await api.location.info(0)
    assert exc_info.value.message == "Location not found."
