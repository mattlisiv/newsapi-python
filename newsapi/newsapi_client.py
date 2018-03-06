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
        """
            Returns live top and breaking headlines for a country, specific category in a country, single source, or multiple 				sources..
            
            Optional parameters:
                (str) q - return headlines w/ specified coin! Valid values are:
                            'bitcoin', 'etheremum', 'ripple', 'bitcoin cash', etc.
                            
                (str) sources - return headlines of news sources! some Valid values are:
                            'bbc-news', 'the-verge', 'abc-news', 'crypto coins news',
                            'ary news','associated press','wired','aftenposten','australian financial review','axios',
							'bbc news','bild','blasting news','bloomberg','business insider','engadget','google news',
							'hacker news','info money,'recode','techcrunch','techradar','the next web','the verge' etc.
							
				(str) language - The 2-letter ISO-639-1 code of the language you want to get headlines for. Valid values are:
								'ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'
                            
                (str) country - The 2-letter ISO 3166-1 code of the country you want to get headlines! Valid values are:
                                'ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr',    									'hk','hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz','ph' 									'pl','pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us'
								
				(str) category - The category you want to get headlines for! Valid values are:
								'business','entertainment','general','health','science','sports','technology'
								
				(int) page_size - The number of results to return per page (request). 20 is the default, 100 is the maximum. 
								
				(int) page - Use this to page through the results if the total results found is greater than the page size.										
        """
        
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
	"""
            Search through millions of articles from over 5,000 large and small news sources and blogs.
            
            Optional parameters:
                (str) q - return headlines w/ specified coin! Valid values are:
                            'bitcoin', 'etheremum', 'ripple', 'bitcoin cash', etc.
                            
                (str) sources - return headlines of news sources! some Valid values are:
                            'bbc-news', 'the-verge', 'abc-news', 'crypto coins news',
                            'ary news','associated press','wired','aftenposten','australian financial review','axios',
			    'bbc news','bild','blasting news','bloomberg','business insider','engadget','google news',
		  	    'hacker news','info money,'recode','techcrunch','techradar','the next web','the verge' etc.
							
		(str) domains - A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to restrict the 								search to. 
		(str) from_parameter - A date and optional time for the oldest article allowed.(e.g. 2018-03-05 or 													2018-03-05T03:46:15)
				
		(str) to - A date and optional time for the newest article allowed.
							
		(str) language - The 2-letter ISO-639-1 code of the language you want to get headlines for. Valid values are:
				'ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'
								
		(str) sort_by - The order to sort the articles in. Valid values are: 'relevancy','popularity','publishedAt',
				'relevancy'
								
		(int) page_size - The number of results to return per page (request). 20 is the default, 100 is the maximum.		
		(int) page - Use this to page through the results if the total results found is greater than the page size.										
        """
					   
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
					   
	"""
            Returns the subset of news publishers that top headlines...
            
            Optional parameters:
			
		(str) language - The 2-letter ISO-639-1 code of the language you want to get headlines for. Valid values are:
				'ar','de','en','es','fr','he','it','nl','no','pt','ru','se','ud','zh'
                            
                (str) country - The 2-letter ISO 3166-1 code of the country you want to get headlines! Valid values are:
                                'ae','ar','at','au','be','bg','br','ca','ch','cn','co','cu','cz','de','eg','fr','gb','gr',    									'hk','hu','id','ie','il','in','it','jp','kr','lt','lv','ma','mx','my','ng','nl','no','nz','ph' 									'pl','pt','ro','rs','ru','sa','se','sg','si','sk','th','tr','tw','ua','us'
								
				(str) category - The category you want to get headlines for! Valid values are:
						'business','entertainment','general','health','science','sports','technology'
																	
        """			   
					   
        # Define Payload
        payload = {}
        payload['category'] = category
        payload['language'] = language
        payload['country'] = country

        # Send Request
        LOGGER.debug("Params %s", payload)
        r = requests.get(self.url + '/sources', auth=self.auth, timeout=30, params=payload)
        return r.json()
