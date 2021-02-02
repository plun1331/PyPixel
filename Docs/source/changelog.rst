Changelog
==========

0.1.9
******
* Added support for the ``/resources/achievements`` endpoint.
* Added a kwarg to bypass API key validation.
* Added this changelog to the documentation.
* Added a new method, ``getGameName(game)``
* Added a new file in utils that contains game names/IDs

0.1.8
******
* The module will now return ``None`` instead of having the value simply be missing.

0.1.7
******
* Added documentation: [pypixel.readthedocs.io](https://pypixel.readthedocs.io/en/latest/)

0.1.6
******
* Add some methods

0.1.5
******
* Released to PyPI

0.1.4
******
* Added a changelog
* Introduced SkyBlock Profiles
* Added 3 new fuctions to ``.Hypixel`` (``.get_name(uuid)``, ``.get_uuid(name)``, and `.get_profiles(uuid)`)
* Deleted ``Other.py`` in favor of a submodule, ``utils``
* Moved the ``send_request()`` method to ``.Hypixel`` and renamed it ``_send()``
* Added a new requirement, ``NBT`` (Used for parsing NBT data).
* Added some exception classes.
* Started subclassing ``object`` for no paticular reason.