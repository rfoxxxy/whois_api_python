# [WhoIS](https://whois.neonteam.cc) API Wrapper

[![codecov](https://codecov.io/gh/rfoxxxy/whois_api_python/branch/main/graph/badge.svg?token=TXL1BPQB06)](https://codecov.io/gh/rfoxxxy/whois_api_python)
[![Python 3.10](https://img.shields.io/badge/python-^3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://mit-license.org/)

API Documentation: [whois.neonteam.cc/docs](https://whois.neonteam.cc/docs)

## Installation

```bash
pip3 install git+https://github.com/rfoxxxy/whois_api_python
```
or
```bash
poetry add git+https://github.com/rfoxxxy/whois_api_python
```

## Usage example

```python
import asyncio
from whois_api import WhoIS
whois = WhoIS()


async def main():
    ip_info = await whois.ip.info("1.0.0.1")
    print("Estonian:", ip_info.fmt_location("est"))
    print("Russian:", ip_info.fmt_location("rus"))


asyncio.run(main())
```

