tuto
=============================================================

beginer level cube

Installation
------------

Open the project in a terminal and run::

    pip install -e .

This will install the cube in your active virtual environment
as ``cubicweb-tuto``.

The following sections indicate additional steps when you
install this cube as a dependency or as an instance.

As a dependency
~~~~~~~~~~~~~~~

If you plan to use this cube as a dependency for your own cube,
add it to your ``__pkginfo__.py`` as follows::

    __depends__ = {
        # ... Your previous dependencies
        "cubicweb-tuto": None,
    }

If the target cube is already used as an instance, you need to migrate it
with the help of its python shell (replace ``YOUR_INSTANCE_NAME`` by your instance name)::

    cubicweb-ctl shell YOUR_INSTANCE_NAME

In the python prompt, enter the following command::

    add_cube("tuto")

Press ``Ctrl-D`` then restart your instance.
The cube should now be available in your instance.

As an instance
~~~~~~~~~~~~~~

If you plan to use this cube directly as an instance, create and start
your instance with the following commands (replace ``tuto-instance``
by the name of your choice)::

    cubicweb-ctl create tuto tuto-instance
    cubicweb-ctl start -D tuto-instance


Learn More
----------

Visit the `official documentation <https://cubicweb.readthedocs.io/en/4.1.0>`_
to learn more about CubicWeb.
