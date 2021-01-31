.. _tutorial:

Tutorial
=========
The following is a tutorial for using PyPixel.

Installation
*************
To install the module, simply use pip:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U pypixel-api

    # Windows
    py -3 -m pip install -U pypixel-api

Or, if you wish, you can install the development version off of GitHub:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U git+https://github.com/plun1331/PyPixel

    # Windows
    py -3 -m pip install -U git+https://github.com/plun1331/PyPixel

Obtaining an API Key
*********************
To use the module, you must first generate an API key.

1. Open Minecraft: Java Edition and connect to ``mc.hypixel.net``
2. Run the command ``/api new``. This will give you your API Key.

.. warning::
    ``/api new`` will invalidate your existing API key, if you have one.

.. warning::
    Your API key should remain private. If it is abused, it may get deleted
    and you may get banned from the Hypixel Network.


Creating a Script
******************
Now, actually using the module.

First we must import the module.

.. code:: py

    import PyPixel

Now, to use the module's features, we can initialize the ``Hypixel`` class.

.. code:: py

    import PyPixel

    hypixel = PyPixel.Hypixel(api_key="API Key")

Where ``"API Key"`` is the API key that you got in the previous section.

This is the simplest example of using the module, if you would like more you can find examples :ref:`here<examples>`.