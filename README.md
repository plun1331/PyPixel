# PyPixel

[![Discord Server Invite](https://discord.com/api/guilds/766123673425281025/embed.png)](https://discord.gg/k6fgvUn3aF)
[![PyPI version info](https://img.shields.io/pypi/v/pypixel-api.svg)](https://pypi.python.org/pypi/pypixel-api)
[![PyPI supported Python versions](https://img.shields.io/pypi/pyversions/pypixel-api.svg)](https://pypi.python.org/pypi/pypixel-api)
[![Documentation Status](https://readthedocs.org/projects/pypixel/badge/?version=latest)](https://pypixel.readthedocs.io/en/latest/?badge=latest)

An asynchronous wrapper for the Hypixel API.



# Installation

**Python 3.6 or higher is required**

You can install the package with the following command.

```sh
# Linux/macOS
python3 -m pip install -U pypixel-api

# Windows
py -3 -m pip install -U pypixel-api
```
Or, you can install the development version from the GitHub:

```shell
# Linux/macOS
python3 -m pip install -U git+https://github.com/plun1331/PyPixel

# Windows
py -3 -m pip install -U git+https://github.com/plun1331/PyPixel
```

# Examples
You can find some examples [in our documentation](https://pypixel.readthedocs.io/en/latest/examples.html)

# Changelog
## 0.1.7
- Added documentation: [pypixel.readthedocs.io](https://pypixel.readthedocs.io/en/latest/examples.html)

## 0.1.6
- Add some methods

## 0.1.5
- Released to PyPI

## 0.1.4a
- Added a changelog
- Introduced SkyBlock Profiles
- Added 3 new fuctions to `.Hypixel` (`.get_name(uuid)`, `.get_uuid(name)`, and `.get_profiles(uuid)`)
- Deleted `Other.py` in favor of a submodule, `utils`
- Moved the `send_request()` method to `.Hypixel` and renamed it `_send()`
- Added a new requirement, `NBT` (Used for parsing NBT data).
- Added some exception classes.
- Started subclassing `object` for no paticular reason.




