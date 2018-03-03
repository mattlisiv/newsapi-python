import logging

import requests
from newsapi.newsapi_auth import NewsApiAuth


LOGGER = logging.getLogger()


class NewsApiClient(object):

    def __init__(self, api_key, api_url='https://newsapi.org/v2/'):
        self.url = api_url.rstrip('/')
        self.auth = NewsApiAuth(api_key=api_key)

    def get_top_headlines(self, q=None, sources=None, language=None, country=None, category=None, page_size=None,
                          page=None):
        # Define Payload
        payload = {}
        payload['q'] = q
        payload['sources'] = ','.join(sources) if sources else None
        payload['language'] = language
        payload['country'] = country
        payload['category'] = category
        payload['pageSize'] = page_size
        payload['page'] = page

        # Send Request
        LOGGER.debug("Params %s", payload)
        r = requests.get(self.url + '/top-headlines', auth=self.auth, timeout=30, params=payload)
        return r.json()

    def get_everything(self, q=None, sources=None, domains=None, from_parameter=None, to=None, language=None,
                       sort_by=None, page=None, page_size=None):
        # Define Payload
        payload = {}
        payload['q'] = ','.join(q) if q else None
        payload['sources'] = ','.join(sources) if sources else None
        payload['domains'] = ','.join(domains) if domains else None
        payload['from'] = from_parameter
        payload['to'] = to
        payload['language'] = ','.join(language) if language else None
        payload['sortBy'] = sort_by
        payload['page'] = page
        payload['pageSize'] = page_size

        # Send Request
        LOGGER.debug("Params %s", payload)
        r = requests.get(self.url + '/everything', auth=self.auth, timeout=30, params=payload)
        return r.json()

    def get_sources(self, category=None, language=None, country=None):
        # Define Payload
        payload = {}
        payload['category'] = category
        payload['language'] = language
        payload['country'] = country

        # Send Request
        LOGGER.debug("Params %s", payload)
        r = requests.get(self.url + '/sources', auth=self.auth, timeout=30, params=payload)
        return r.json()
