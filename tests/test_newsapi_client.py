import unittest
import os
from newsapi.newsapi_client import NewsApiClient


class NewsApiClientTest(unittest.TestCase):

    def setUp(self):
        key = os.environ.get('news_api_secret')
        self.api = NewsApiClient(key)

    def test_api_top_headline(self):
        # Raise TypeError if Keyword/Phrase param is not of type str
        q = 0
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(q=q)

        # Raise ValueError if sources param in not None and country param or category param is not None
        sources = 'techcrunch'
        country = 'us'
        category = 'business'
        with self.assertRaises(ValueError):
            self.api.get_top_headlines(sources=sources, country=country, category=category)

        # Raise TypeError if sources param is not of type str
        sources = 0
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(sources=sources)

        # Raise TypeError if language param is not of type str
        language = 0
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(language=language)

        # Raise ValueError if language param is invalid
        language = 'xx'
        with self.assertRaises(ValueError):
            self.api.get_top_headlines(language=language)

        # Raise TypeError if country param is not of type str
        country = 0
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(country=country)

        # Raise ValueError if country param is invalid
        country = 'xx'
        with self.assertRaises(ValueError):
            self.api.get_top_headlines(country=country)

        # Raises TypeError if category param is not of type str
        category = 0
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(category=category)

        # Raises ValueError if category param is invalid
        category = 'x0x'
        with self.assertRaises(ValueError):
            self.api.get_top_headlines(category=category)

        # Raises TypeError if page_size param is not an int
        page_size = '1'
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(page_size=page_size)

        # Raises ValueError if page_size param is less than zero(0) or greater than 100
        page_size = -1
        with self.assertRaises(ValueError):
            self.api.get_top_headlines(page_size=page_size)

        page_size = 1000
        with self.assertRaises(ValueError):
            self.api.get_top_headlines(page_size=page_size)

        # Raises a TypeError is page param is not an int
        page = '1'
        with self.assertRaises(TypeError):
            self.api.get_top_headlines(page=page)

        # Raises a ValueError if page param is less than zero(0)
        page = -1
        with self.assertRaises(ValueError):
            self.api.get_top_headlines(page=page)

    def test_api_get_everything(self):
        # Raise TypeError if Keyword/Phrase param is None
        q = 0
        with self.assertRaises(TypeError):
            self.api.get_everything(q=q)

        # Raise TypeError if sources param is not of type str
        sources = 0
        with self.assertRaises(TypeError):
            self.api.get_everything(sources=sources)

        # Raise TypeError is domains param is not of type str
        domains = 0
        with self.assertRaises(TypeError):
            self.api.get_everything(domains=domains)

        # Raise TypeError is exclude_domains param is not of type str
        exclude_domains = 0
        with self.assertRaises(TypeError):
            self.api.get_everything(exclude_domains=exclude_domains)

        # Raise TypeError is from_param param is not of type str
        from_param = 0
        with self.assertRaises(TypeError):
            self.api.get_everything(from_param=from_param)

        # Raise ValueError if param is not in the format YYYY-MM-DD
        from_param = '2016-6-4'
        with self.assertRaises(ValueError):
            self.api.get_everything(from_param=from_param)

        # Raise TypeError if to param is not of type str
        to = 1
        with self.assertRaises(TypeError):
            self.api.get_everything(to=to)

        # Raise ValueError if to param is not in the format YYYY-MM-DD
        to = '2016-6-24'
        with self.assertRaises(ValueError):
            self.api.get_everything(to=to)

        # Raise TypeError if language param is not of type str
        language = 0
        with self.assertRaises(TypeError):
            self.api.get_everything(language=language)

        # Raise ValueError if language param is invalid
        language = 'xx'
        with self.assertRaises(ValueError):
            self.api.get_everything(language=language)

        # Raise TypeError is sort_by param is not of type str
        sort_by = 1
        with self.assertRaises(TypeError):
            self.api.get_everything(sort_by=sort_by)

        # Raise ValueError if soft_by param is invalid
        sort_by = 'sort'
        with self.assertRaises(ValueError):
            self.api.get_everything(sort_by=sort_by)

        # Raises TypeError if page_size param is not an int
        page_size = '1'
        with self.assertRaises(TypeError):
            self.api.get_everything(page_size=page_size)

        # Raises ValueError if page_size param is less than zero(0) or greater than 100
        page_size = -1
        with self.assertRaises(ValueError):
            self.api.get_everything(page_size=page_size)

        page_size = 1000
        with self.assertRaises(ValueError):
            self.api.get_everything(page_size=page_size)

        # Raises a TypeError is page param is not an int
        page = '1'
        with self.assertRaises(TypeError):
            self.api.get_everything(page=page)

        # Raises a ValueError if page param is less than zero(0)
        page = -1
        with self.assertRaises(ValueError):
            self.api.get_everything(page=page)

    def test_api_get_sources(self):
        # Raise TypeError if language param is not of type str
        language = 0
        with self.assertRaises(TypeError):
            self.api.get_sources(language=language)

        # Raise ValueError if language param is invalid
        language = 'xx'
        with self.assertRaises(ValueError):
            self.api.get_sources(language=language)

        # Raise TypeError if country param is not of type str
        country = 0
        with self.assertRaises(TypeError):
            self.api.get_sources(country=country)

        # Raise ValueError if country param is invalid
        country = 'xx'
        with self.assertRaises(ValueError):
            self.api.get_sources(country=country)

        # Raises TypeError if category param is not of type str
        category = 0
        with self.assertRaises(TypeError):
            self.api.get_sources(category=category)

        # Raises ValueError if category param is invalid
        category = 'x0x'
        with self.assertRaises(ValueError):
            self.api.get_sources(category=category)
