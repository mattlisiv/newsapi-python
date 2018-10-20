import requests
from newsapi.newsapi_auth import NewsApiAuth
from newsapi import const
from newsapi.newsapi_exception import NewsAPIException


class NewsApiClient(object):

    def __init__(self, api_key):
        self.auth = NewsApiAuth(api_key=api_key)

    def get_top_headlines(self, q=None, sources=None, language='en', country=None, category=None, page_size=None,
                          page=None):
        """
            Returns live top and breaking headlines for a country, specific category in a country, single source, or multiple sources..

            Optional parameters:
                (str) q - return headlines w/ specific keyword or phrase. For example:
                          'bitcoin', 'trump', 'tesla', 'ethereum', etc.

                (str) sources - return headlines of news sources! some Valid values are:
                                'bbc-news', 'the-verge', 'abc-news', 'crypto coins news',
                                'ary news','associated press','wired','aftenposten','australian financial review','axios',
				'bbc news','bild','blasting news','bloomberg','business insider','engadget','google news',
				'hacker news','info money,'recode','techcrunch','techradar','the next web','the verge' etc.

		(str) language - The 2-letter ISO-639-1 code of the language you want to get headlines for. Valid values are:
				 'ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'

                (str) country - The 2-letter ISO 3166-1 code of the country you want to get headlines! Valid values are:
                                'ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr',
                                'hk','hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz',
                                'ph','pl','pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us'

		(str) category - The category you want to get headlines for! Valid values are:
				 'business','entertainment','general','health','science','sports','technology'

		(int) page_size - The number of results to return per page (request). 20 is the default, 100 is the maximum.

		(int) page - Use this to page through the results if the total results found is greater than the page size.
        """

        # Define Payload
        payload = {}

        # Keyword/Phrase
        if q is not None:
            if type(q) == str:
                payload['q'] = q
            else:
                raise TypeError('keyword/phrase q param should be a of type str')

        # Sources
        if (sources is not None) and ((country is not None) or (category is not None)):
            raise ValueError('cannot mix country/category param with sources param.')

        # Sources
        if sources is not None:
            if type(sources) == str:
                payload['sources'] = sources
            else:
                raise TypeError('sources param should be of type str')

        # Language
        if language is not None:
            if type(language) == str:
                if language in const.languages:
                    payload['language'] = language
                else:
                    raise ValueError('invalid language')
            else:
                raise TypeError('language param should be of type str')

        # Country
        if country is not None:
            if type(country) == str:
                if country in const.countries:
                    payload['country'] = country
                else:
                    raise ValueError('invalid country')
            else:
                raise TypeError('country param should be of type str')

        # Category
        if category is not None:
            if type(category) == str:
                if category in const.categories:
                    payload['category'] = category
                else:
                    raise ValueError('invalid category')
            else:
                raise TypeError('category param should be of type str')

        # Page Size
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload['pageSize'] = page_size
                else:
                    raise ValueError('page_size param should be an int between 1 and 100')
            else:
                raise TypeError('page_size param should be an int')

        # Page
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload['page'] = page
                else:
                    raise ValueError('page param should be an int greater than 0')
            else:
                raise TypeError('page param should be an int')

        # Send Request
        r = requests.get(const.TOP_HEADLINES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()

    def get_everything(self, q=None, sources=None, domains=None, exclude_domains=None,
                       from_param=None, to=None, language=None, sort_by=None, page=None,
                       page_size=None):
        """
            Search through millions of articles from over 5,000 large and small news sources and blogs.

            Optional parameters:
                (str) q - return headlines w/ specified coin! Valid values are:
                            'bitcoin', 'trump', 'tesla', 'ethereum', etc

                (str) sources - return headlines of news sources! some Valid values are:
                            'bbc-news', 'the-verge', 'abc-news', 'crypto coins news',
                            'ary news','associated press','wired','aftenposten','australian financial review','axios',
			    'bbc news','bild','blasting news','bloomberg','business insider','engadget','google news',
		  	    'hacker news','info money,'recode','techcrunch','techradar','the next web','the verge' etc.

		(str) domains - A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to restrict the search to.

        (str) exclude_domains - A comma_seperated string of domains to be excluded from the search

		(str) from_param - A date and optional time for the oldest article allowed.
                                       (e.g. 2018-03-05 or 2018-03-05T03:46:15)

		(str) to - A date and optional time for the newest article allowed.

		(str) language - The 2-letter ISO-639-1 code of the language you want to get headlines for. Valid values are:
				'ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'

		(str) sort_by - The order to sort the articles in. Valid values are: 'relevancy','popularity','publishedAt'

		(int) page_size - The number of results to return per page (request). 20 is the default, 100 is the maximum.

		(int) page - Use this to page through the results if the total results found is greater than the page size.
        """

        # Define Payload
        payload = {}

        # Keyword/Phrase
        if q is not None:
            if type(q) == str:
                payload['q'] = q
            else:
                raise TypeError('keyword/phrase q param should be of type str')

        # Sources
        if sources is not None:
            if type(sources) == str:
                payload['sources'] = sources
            else:
                raise TypeError('sources param should be of type str')

        # Domains To Search
        if domains is not None:
            if type(domains) == str:
                payload['domains'] = domains
            else:
                raise TypeError('domains param should be of type str')

        if exclude_domains is not None:
            if isinstance(exclude_domains, str):
                payload['excludeDomains'] = exclude_domains
            else:
                raise TypeError('exclude_domains param should be of type str')

        # Search From This Date ...
        if from_param is not None:
            if type(from_param) == str:
                if (len(from_param)) >= 10:
                    for i in range(len(from_param)):
                        if (i == 4 and from_param[i] != '-') or (i == 7 and from_param[i] != '-'):
                            raise ValueError('from_param should be in the format of YYYY-MM-DD')
                        else:
                            payload['from'] = from_param
                else:
                    raise ValueError('from_param should be in the format of YYYY-MM-DD')
            else:
                raise TypeError('from_param should be of type str')

        # ... To This Date
        if to is not None:
            if type(to) == str:
                if (len(to)) >= 10:
                    for i in range(len(to)):
                        if (i == 4 and to[i] != '-') or (i == 7 and to[i] != '-'):
                            raise ValueError('to should be in the format of YYYY-MM-DD')
                        else:
                            payload['to'] = to
                else:
                    raise ValueError('to param should be in the format of YYYY-MM-DD')
            else:
                raise TypeError('to param should be of type str')

        # Language
        if language is not None:
            if type(language) == str:
                if language not in const.languages:
                    raise ValueError('invalid language')
                else:
                    payload['language'] = language
            else:
                raise TypeError('language param should be of type str')

        # Sort Method
        if sort_by is not None:
            if type(sort_by) == str:
                if sort_by in const.sort_method:
                    payload['sortBy'] = sort_by
                else:
                    raise ValueError('invalid sort')
            else:
                raise TypeError('sort_by param should be of type str')

        # Page Size
        if page_size is not None:
            if type(page_size) == int:
                if 0 <= page_size <= 100:
                    payload['pageSize'] = page_size
                else:
                    raise ValueError('page_size param should be an int between 1 and 100')
            else:
                raise TypeError('page_size param should be an int')

        # Page
        if page is not None:
            if type(page) == int:
                if page > 0:
                    payload['page'] = page
                else:
                    raise ValueError('page param should be an int greater than 0')
            else:
                raise TypeError('page param should be an int')

        # Send Request
        r = requests.get(const.EVERYTHING_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()

    def get_sources(self, category=None, language=None, country=None):
        """
            Returns the subset of news publishers that top headlines...

            Optional parameters:
                (str) category - The category you want to get headlines for! Valid values are:
				 'business','entertainment','general','health','science','sports','technology'

		(str) language - The 2-letter ISO-639-1 code of the language you want to get headlines for. Valid values are:
				'ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'

                (str) country - The 2-letter ISO 3166-1 code of the country you want to get headlines! Valid values are:
                                'ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr',
                                'hk','hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz',
                                'ph','pl','pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us'

				(str) category - The category you want to get headlines for! Valid values are:
						'business','entertainment','general','health','science','sports','technology'

        """

        # Define Payload
        payload = {}

        # Language
        if language is not None:
            if type(language) == str:
                if language in const.languages:
                    payload['language'] = language
                else:
                    raise ValueError('invalid language')
            else:
                raise TypeError('language param should be of type str')

        # Country
        if country is not None:
            if type(country) == str:
                if country in const.countries:
                    payload['country'] = country
                else:
                    raise ValueError('invalid country')
            else:
                raise TypeError('country param should be of type str')

                # Category
        if category is not None:
            if type(category) == str:
                if category in const.categories:
                    payload['category'] = category
                else:
                    raise ValueError('invalid category')
            else:
                raise TypeError('category param should be of type str')

        # Send Request
        r = requests.get(const.SOURCES_URL, auth=self.auth, timeout=30, params=payload)

        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()
