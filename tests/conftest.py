import os
import sys

import pytest

from whois_api import WhoIS

os.environ["DISABLE_UVLOOP"] = "True"

sys.path.append('./')


@pytest.fixture(scope="session")
def api(request):
    return WhoIS("https://whois.neonteam.cc", 10)
