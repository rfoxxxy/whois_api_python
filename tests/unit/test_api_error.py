import logging
import typing

import pytest

from whois_api.types.exceptions import APIException

if typing.TYPE_CHECKING:
    from whois_api import WhoIS  # pragma: no cover

LOGGER = logging.getLogger(__name__)


async def test_api_error(api: "WhoIS"):
    with pytest.raises(APIException) as exc_info:
        await api.location.api_request("info", {})
    assert str(exc_info.value) == "Parameter(s) \"location_id\" must contain values."