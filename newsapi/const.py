"""Constants and allowed parameter values specified in the News API."""

TOP_HEADLINES_URL = "https://newsapi.org/v2/top-headlines"
EVERYTHING_URL = "https://newsapi.org/v2/everything"
SOURCES_URL = "https://newsapi.org/v2/sources"

#: The 2-letter ISO 3166-1 code of the country you want to get headlines for.  If not specified,
#: the results span all countries.
countries = {
    "ae",
    "ar",
    "at",
    "au",
    "be",
    "bg",
    "br",
    "ca",
    "ch",
    "cn",
    "co",
    "cu",
    "cz",
    "de",
    "eg",
    "es",
    "fr",
    "gb",
    "gr",
    "hk",
    "hu",
    "id",
    "ie",
    "il",
    "in",
    "is",
    "it",
    "jp",
    "kr",
    "lt",
    "lv",
    "ma",
    "mx",
    "my",
    "ng",
    "nl",
    "no",
    "nz",
    "ph",
    "pk",
    "pl",
    "pt",
    "ro",
    "rs",
    "ru",
    "sa",
    "se",
    "sg",
    "si",
    "sk",
    "th",
    "tr",
    "tw",
    "ua",
    "us",
    "ve",
    "za",
    "zh",
}

#: The 2-letter ISO-639-1 code of the language you want to get articles for.  If not specified,
#: the results span all languages.
languages = {"ar", "en", "cn", "de", "es", "fr", "he", "it", "nl", "no", "pt", "ru", "sv", "se", "ud", "zh"}

#: The category you want to get articles for.  If not specified,
#: the results span all categories.
categories = {"business", "entertainment", "general", "health", "science", "sports", "technology"}

#: The order to sort article results in.  If not specified, the default is ``"publishedAt"``.
sort_method = {"relevancy", "popularity", "publishedAt"}
