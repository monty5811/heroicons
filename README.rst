======
iconic
======

.. image:: https://img.shields.io/github/workflow/status/monty5811/iconic/CI/main?style=for-the-badge
   :target: https://github.com/monty5811/iconic/actions?workflow=CI

.. image:: https://img.shields.io/codecov/c/github/monty5811/iconic/main?style=for-the-badge
   :target: https://app.codecov.io/gh/monty5811/iconic

.. image:: https://img.shields.io/pypi/v/iconic.svg?style=for-the-badge
   :target: https://pypi.org/project/iconic/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Use `iconic.app icons <https://iconic.app/>`__ in your Django and Jinja templates.

Requirements
------------

Python 3.6 to 3.9 supported.

Django 2.2 to 3.2 supported.

----

This was forked from `adamchainz/heroicons <https://github.com/adamchainz/heroicons>`_.

**Are your tests slow?**
Check out Adam's book `Speed Up Your Django Tests <https://gumroad.com/l/suydt>`__ which covers loads of best practices so you can write faster, more accurate tests.

----

Usage
-----

The ``iconic`` package supports both Django templates and Jinja2 templates.
Follow the appropriate guide below.

Django templates
~~~~~~~~~~~~~~~~

1. Install with ``python -m pip install iconic[django]``.

2. Add to your ``INSTALLED_APPS``:

   .. code-block:: python

       INSTALLED_APPS = [
           ...,
           'iconic',
           ...,
       ]

Now in your templates you can load the template library with:

.. code-block:: django

    {% load iconic %}

This provides a tag to render ``<svg>`` icons: ``iconic_icon``.
The tags take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `iconic.app grid <https://iconic.app/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed size: ``24``.

* Any number of keyword arguments.
  These will be added as HTML attributes to the output ``<svg>`` tag.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

For example, to render an outline “announcement” icon, at 48x48, with some extra CSS classes and a data attribute “controller”, you would write:

.. code-block:: django

    {% iconic_icon "announcement" size=48 class="h-4 w-4 inline" data_controller="announcement" %}

Jinja templates
~~~~~~~~~~~~~~~

1. Install with ``python -m pip install iconic[jinja]``.

2. Adjust your Jinja ``Environment`` to add the global function ``iconic``, imported from ``iconic.jinja``.
   For example:

   .. code-block:: python

       from iconic.jinja import iconic_icon
       from jinja2 import Environment

       env = Environment()
       env.globals.update(
           {
               "iconic_icon": iconic_icon,
           }
       )

Now in your templates you can call those two functions, which render ``<svg>`` icons corresponding to the two icon styles in the set.
The functions take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `iconic.app grid <https://iconic.app/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed size: ``24``.

* Any number of keyword arguments.
  These will be added as HTML attributes to the output ``<svg>`` tag.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

For example, to render an outline “announcement” icon, at 48x48, with some extra CSS classes and a data attribute “controller”, you would write:

.. code-block:: jinja

    {% iconic("announcement", size=48, class="h-4 w-4 inline", data_controller="announcement") %}
