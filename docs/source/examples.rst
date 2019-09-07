.. _examples:

Example :class:`NewsApiClient` Usage
====================================

This page is a tutorial-by-example for using the :class:`NewsApiClient` class.

Basic Usage
-----------

The top-level :class:`NewsApiClient` class allows you to access News API endpoints.  Initialize the client with your API key::

    import os
    from newsapi import NewsApiClient

    # An API key; for example: "74f9e72a4bfd4dbaa0cbac8e9a17d34a"
    key = os.environ["news_api_secret"]

    api = NewsApiClient(api_key=key)

The only required parameter is an `API key <https://newsapi.org/register>`_.  You can also pass a persistent ``session`` object; see `Using a Dedicated Session`_.

Accessing the `/top-headlines` Endpoint
---------------------------------------

Use :meth:`newsapi.NewsApiClient.get_top_headlines` to pull from the `/top-headlines` endpoint::

    api.get_top_headlines()
    api.get_top_headlines(q="hurricane")
    api.get_top_headlines(category="sports")
    api.get_top_headlines(sources="abc-news,ars-technica", page_size=50)

Accessing the `/everything` Endpoint
------------------------------------

Use :meth:`newsapi.NewsApiClient.get_everything` to pull from the `/everything` endpoint::

    api.get_everything("hurricane OR tornado", sort_by="relevancy", language="en")
    api.get_everything("(hurricane OR tornado) AND FEMA", sort_by="relevancy")


Accessing the `/sources` Endpoint
---------------------------------

Use :meth:`newsapi.NewsApiClient.get_sources` to pull from the `/sources` endpoint::

    api.get_sources()
    api.get_sources(category="technology")
    api.get_sources(country="ru")
    api.get_sources(category="health", country="us")
    api.get_sources(language="en", country="in")

Using a Dedicated Session
-------------------------

By default, each method call from :class:`NewsApiClient` uses a new TCP session (and ``requests.Session`` instance).
This is not ideal if you'd like to call endpoints multiple times,
whereas using a single session can provide connection-pooling and cookie persistence.

To use a single session across multiple method calls, pass the session object to :class:`NewsApiClient`::

    import requests

    with requests.Session() as session:
        # Use a single session for multiple requests.  Using a 'with'
        # context manager closes the session and TCP connection after use.
        api = NewsApiClient(api_key=key, session=session)
        data1 = api.get_top_headlines(category="technology")
        data2 = api.get_everything(q="facebook", domains="mashable.com,wired.com")

Date Inputs
-----------

The optional parameters ``from_param`` and ``to`` used in :meth:`newsapi.NewsApiClient.get_everything`
allow you to constrain the result set to articles published within a given span.

You can pass a handful of different types:

- ``datetime.date``
- ``datetime.datetime`` (assumed to be in UTC time)
- ``str`` formated as either ``%Y-%m-%d`` (e.g. *2019-09-07*) or ``%Y-%m-%dT%H:%M:%S`` (e.g. *2019-09-07T13:04:15*)
- ``int`` or ``float`` (assumed represents a Unix timestamp)
- ``None`` (the default, in which there is no constraint)

Here are a few valid examples::

    import datetime as dt

    api.get_everything(
        q="hurricane",
        from_param=dt.date(2019, 9, 1),
        to=dt.date(2019, 9, 3),
    )

    api.get_everything(
        q="hurricane",
        from_param=dt.datetime(2019, 9, 1, hour=5),
        to=dt.datetime(2019, 9, 1, hour=15),
    )

    api.get_everything(
        q="hurricane",
        from_param="2019-08-01",
        to="2019-09-15",
    )

    api.get_everything(
        q="hurricane",
        from_param="2019-08-01",
        to="2019-09-15",
    )

    api.get_everything(
        q="venezuela",
        from_param="2019-08-01T10:30:00",
        to="2019-09-15T14:00:00",
    )
