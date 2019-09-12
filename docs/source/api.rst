.. _api:

API Reference
=============

.. module:: newsapi-python

This page is a technical reference to the public classes, exceptions, and data
defined in newsapi-python.

While newsapi-python makes every effort to keep up with the API,
please consider the official News API `docs <https://newsapi.org/docs>`_
as the canonical News API reference.

Classes
-------

.. autoclass:: newsapi.NewsApiClient
   :members:

Exceptions
----------

.. autoexception:: newsapi.newsapi_exception.NewsAPIException

Constants
---------

The :mod:`newsapi.const` module holds constants and allowed parameter values specified in the official News API documentation.

.. autodata:: newsapi.const.languages

.. autodata:: newsapi.const.countries

.. autodata:: newsapi.const.categories

.. autodata:: newsapi.const.sort_method
