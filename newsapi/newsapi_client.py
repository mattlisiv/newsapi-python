from __future__ import unicode_literals

import requests

from newsapi import const
from newsapi.newsapi_auth import NewsApiAuth
from newsapi.newsapi_exception import NewsAPIException
from newsapi.utils import is_valid_string, stringify_date_param


class NewsApiClient(object):
    """The core client object used to fetch data from News API endpoints.

    :param api_key: Your API key, a length-32 UUID string provided for your News API account.
        You must `register <https://newsapi.org/register>`_ for a News API key.
    :type api_key: str

    :param session: An optional :class:`requests.Session` instance from which to execute requests.
        **Note**: If you provide a ``session`` instance, :class:`NewsApiClient` will *not* close the session
        for you.  Remember to call ``session.close()``, or use the session as a context manager, to close
        the socket and free up resources.
    :type session: `requests.Session <https://2.python-requests.org/en/master/user/advanced/#session-objects>`_ or None
    """

    def __init__(self, api_key, session=None):
        self.auth = NewsApiAuth(api_key=api_key)
        if session is None:
            self.request_method = requests
        else:
            self.request_method = session

    def get_top_headlines(  # noqa: C901
        self, q=None, qintitle=None, sources=None, language="en", country=None, category=None, page_size=None, page=None
    ):
        """Call the `/top-headlines` endpoint.

        Fetch live top and breaking headlines.

        This endpoint provides live top and breaking headlines for a country, specific category in a country,
        single source, or multiple sources. You can also search with keywords.  Articles are sorted by the earliest
        date published first.

        :param q: Keywords or a phrase to search for in the article title and body.  See the official News API
            `documentation <https://newsapi.org/docs/endpoints/everything>`_ for search syntax and examples.
        :type q: str or None

        :param qintitle: Keywords or a phrase to search for in the article title and body.  See the official News API
            `documentation <https://newsapi.org/docs/endpoints/everything>`_ for search syntax and examples.
        :type q: str or None

        :param sources: A comma-seperated string of identifiers for the news sources or blogs you want headlines from.
            Use :meth:`NewsApiClient.get_sources` to locate these programmatically, or look at the
            `sources index <https://newsapi.org/sources>`_.  **Note**: you can't mix this param with the
            ``country`` or ``category`` params.
        :type sources: str or None

        :param language: The 2-letter ISO-639-1 code of the language you want to get headlines for.
            See :data:`newsapi.const.languages` for the set of allowed values.
            The default for this method is ``"en"`` (English).  **Note**: this parameter is not mentioned in the
            `/top-headlines documentation <https://newsapi.org/docs/endpoints/top-headlines>`_ as of Sep. 2019,
            but *is* supported by the API.
        :type language: str or None

        :param country: The 2-letter ISO 3166-1 code of the country you want to get headlines for.
            See :data:`newsapi.const.countries` for the set of allowed values.
            **Note**: you can't mix this parameter with the ``sources`` param.
        :type country: str or None

        :param category: The category you want to get headlines for.
            See :data:`newsapi.const.categories` for the set of allowed values.
            **Note**: you can't mix this parameter with the ``sources`` param.
        :type category: str or None

        :param page_size: Use this to page through the results if the total results found is
            greater than the page size.
        :type page_size: int or None

        :param page: The number of results to return per page (request).
            20 is the default, 100 is the maximum.
        :type page: int or None

        :return: JSON response as nested Python dictionary.
        :rtype: dict
        :raises NewsAPIException: If the ``"status"`` value of the response is ``"error"`` rather than ``"ok"``.
        """

        payload = {}

        # Keyword/Phrase
        if q is not None:
            if is_valid_string(q):
                payload["q"] = q
            else:
                raise TypeError("keyword/phrase q param should be of type str")

        # Keyword/Phrase in Title
        if qintitle is not None:
            if is_valid_string(qintitle):
                payload["qintitle"] = qintitle
            else:
                raise TypeError("keyword/phrase qintitle param should be of type str")

        # Sources
        if (sources is not None) and ((country is not None) or (category is not None)):
            raise ValueError("cannot mix country/category param with sources param.")

        # Sources
        if sources is not None:
            if is_valid_string(sources):
                payload["sources"] = sources
            else:
                raise TypeError("sources param should be of type str")

        # Language
        if language is not None:
            if is_valid_string(language):
                if language in const.languages:
                    payload["language"] = language
                else:
                    raise ValueError("invalid language")
            else:
                raise TypeError("language param should be of type str")

        # Country
        if country is not None:
            if is_valid_string(country):
                if country in const.countries:
                    payload["country"] = country
                else:
                    raise ValueError("invalid country")
            else:
                raise TypeError("country param should be of type str")

        # Category
        if category is not None:
            if is_valid_string(category):
                if category in const.categories:
                    payload["category"] = category
                else:
                    raise ValueError("invalid category")
            else:
                raise TypeError("category param should be of type str")

        # Page Size
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload["pageSize"] = page_size
                else:
                    raise ValueError("page_size param should be an int between 1 and 100")
            else:
                raise TypeError("page_size param should be an int")

        # Page
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload["page"] = page
                else:
                    raise ValueError("page param should be an int greater than 0")
            else:
                raise TypeError("page param should be an int")

        # Send Request
        r = self.request_method.get(const.TOP_HEADLINES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()

    def get_everything(  # noqa: C901
        self,
        q=None,
        qintitle=None,
        sources=None,
        domains=None,
        exclude_domains=None,
        from_param=None,
        to=None,
        language=None,
        sort_by=None,
        page=None,
        page_size=None,
    ):
        """Call the `/everything` endpoint.

        Search through millions of articles from over 30,000 large and small news sources and blogs.

        :param q: Keywords or a phrase to search for in the article title and body.  See the official News API
            `documentation <https://newsapi.org/docs/endpoints/everything>`_ for search syntax and examples.
        :type q: str or None

        :param qintitle: Keywords or a phrase to search for in the article title and body.  See the official News API
            `documentation <https://newsapi.org/docs/endpoints/everything>`_ for search syntax and examples.
        :type q: str or None

        :param sources: A comma-seperated string of identifiers for the news sources or blogs you want headlines from.
            Use :meth:`NewsApiClient.get_sources` to locate these programmatically, or look at the
            `sources index <https://newsapi.org/sources>`_.
        :type sources: str or None

        :param domains:  A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com)
            to restrict the search to.
        :type domains: str or None

        :param exclude_domains:  A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com)
            to remove from the results.
        :type exclude_domains: str or None

        :param from_param: A date and optional time for the oldest article allowed.
            If a str, the format must conform to ISO-8601 specifically as one of either
            ``%Y-%m-%d`` (e.g. *2019-09-07*) or ``%Y-%m-%dT%H:%M:%S`` (e.g. *2019-09-07T13:04:15*).
            An int or float is assumed to represent a Unix timestamp.  All datetime inputs are assumed to be UTC.
        :type from_param: str or datetime.datetime or datetime.date or int or float or None

        :param to: A date and optional time for the newest article allowed.
            If a str, the format must conform to ISO-8601 specifically as one of either
            ``%Y-%m-%d`` (e.g. *2019-09-07*) or ``%Y-%m-%dT%H:%M:%S`` (e.g. *2019-09-07T13:04:15*).
            An int or float is assumed to represent a Unix timestamp.  All datetime inputs are assumed to be UTC.
        :type to: str or datetime.datetime or datetime.date or int or float or None

        :param language: The 2-letter ISO-639-1 code of the language you want to get headlines for.
            See :data:`newsapi.const.languages` for the set of allowed values.
        :type language: str or None

        :param sort_by: The order to sort articles in.
            See :data:`newsapi.const.sort_method` for the set of allowed values.
        :type sort_by: str or None

        :param page: The number of results to return per page (request).
            20 is the default, 100 is the maximum.
        :type page: int or None

        :param page_size: Use this to page through the results if the total results found is
            greater than the page size.
        :type page_size: int or None

        :return: JSON response as nested Python dictionary.
        :rtype: dict
        :raises NewsAPIException: If the ``"status"`` value of the response is ``"error"`` rather than ``"ok"``.
        """

        payload = {}

        # Keyword/Phrase
        if q is not None:
            if is_valid_string(q):
                payload["q"] = q
            else:
                raise TypeError("keyword/phrase q param should be of type str")

        # Keyword/Phrase in Title
        if qintitle is not None:
            if is_valid_string(qintitle):
                payload["qintitle"] = qintitle
            else:
                raise TypeError("keyword/phrase qintitle param should be of type str")

        # Sources
        if sources is not None:
            if is_valid_string(sources):
                payload["sources"] = sources
            else:
                raise TypeError("sources param should be of type str")

        # Domains To Search
        if domains is not None:
            if is_valid_string(domains):
                payload["domains"] = domains
            else:
                raise TypeError("domains param should be of type str")

        if exclude_domains is not None:
            if isinstance(exclude_domains, str):
                payload["excludeDomains"] = exclude_domains
            else:
                raise TypeError("exclude_domains param should be of type str")

        # Search From This Date ...
        if from_param is not None:
            payload["from"] = stringify_date_param(from_param)

        # ... To This Date
        if to is not None:
            payload["to"] = stringify_date_param(to)

        # Language
        if language is not None:
            if is_valid_string(language):
                if language not in const.languages:
                    raise ValueError("invalid language")
                else:
                    payload["language"] = language
            else:
                raise TypeError("language param should be of type str")

        # Sort Method
        if sort_by is not None:
            if is_valid_string(sort_by):
                if sort_by in const.sort_method:
                    payload["sortBy"] = sort_by
                else:
                    raise ValueError("invalid sort")
            else:
                raise TypeError("sort_by param should be of type str")

        # Page Size
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload["pageSize"] = page_size
                else:
                    raise ValueError("page_size param should be an int between 1 and 100")
            else:
                raise TypeError("page_size param should be an int")

        # Page
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload["page"] = page
                else:
                    raise ValueError("page param should be an int greater than 0")
            else:
                raise TypeError("page param should be an int")

        # Send Request
        r = self.request_method.get(const.EVERYTHING_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()

    def get_sources(self, category=None, language=None, country=None):  # noqa: C901
        """Call the `/sources` endpoint.

        Fetch the subset of news publishers that /top-headlines are available from.

        :param category: Find sources that display news of this category.
            See :data:`newsapi.const.categories` for the set of allowed values.
        :type category: str or None

        :param language: Find sources that display news in a specific language.
            See :data:`newsapi.const.languages` for the set of allowed values.
        :type language: str or None

        :param country: Find sources that display news in a specific country.
            See :data:`newsapi.const.countries` for the set of allowed values.
        :type country: str or None

        :return: JSON response as nested Python dictionary.
        :rtype: dict
        :raises NewsAPIException: If the ``"status"`` value of the response is ``"error"`` rather than ``"ok"``.
        """

        payload = {}

        # Language
        if language is not None:
            if is_valid_string(language):
                if language in const.languages:
                    payload["language"] = language
                else:
                    raise ValueError("invalid language")
            else:
                raise TypeError("language param should be of type str")

        # Country
        if country is not None:
            if is_valid_string(country):
                if country in const.countries:
                    payload["country"] = country
                else:
                    raise ValueError("invalid country")
            else:
                raise TypeError("country param should be of type str")

        # Category
        if category is not None:
            if is_valid_string(category):
                if category in const.categories:
                    payload["category"] = category
                else:
                    raise ValueError("invalid category")
            else:
                raise TypeError("category param should be of type str")

        # Send Request
        r = self.request_method.get(const.SOURCES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()
