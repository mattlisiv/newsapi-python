# newsapi-python

A Python client for the [News API](https://newsapi.org/docs/).

[![License](https://img.shields.io/github/license/mattlisiv/newsapi-python.svg)](https://github.com/mattlisiv/newsapi-python/blob/master/LICENSE.txt)
[![PyPI](https://img.shields.io/pypi/v/newsapi-python.svg)](https://pypi.org/project/newsapi-python/)
[![Status](https://img.shields.io/pypi/status/newsapi-python.svg)](https://pypi.org/project/newsapi-python/)
[![Python](https://img.shields.io/pypi/pyversions/newsapi-python.svg)](https://pypi.org/project/newsapi-python)

## License

Provided under [MIT License](https://github.com/mattlisiv/newsapi-python/blob/master/LICENSE.txt) by Matt Lisivick.

```
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## General

This is a Python client library for [News API V2](https://newsapi.org/).
The functions and methods for this library should mirror the
endpoints specified by the News API [documentation](https://newsapi.org/docs/endpoints).

## Installation

Installation for the package can be done via `pip`:

```bash
$ python -m pip install newsapi-python
```

## Usage

After installation, import the client class into your project:

```python
from newsapi import NewsApiClient
```

Initialize the client with your API key:

```python
api = NewsApiClient(api_key='XXXXXXXXXXXXXXXXXXXXXXX')
```

### Endpoints

An instance of `NewsApiClient` has three instance methods corresponding to three News API endpoints.

#### Top Headlines

Use `.get_top_headlines()` to pull from the [`/top-headlines`](https://newsapi.org/docs/endpoints/top-headlines) endpoint:

```python
api.get_top_headlines(sources='bbc-news')
```

#### Everything

Use `.get_everything()` to pull from the [`/everything`](https://newsapi.org/docs/endpoints/everything) endpoint:

```python
api.get_everything(q='bitcoin')
```

#### Sources

Use `.get_sources()` to pull from the [`/sources`](https://newsapi.org/docs/endpoints/sources) endpoint:

```python
api.get_sources()
```

## For Windows users printing to _cmd_ or _powershell_

You will encounter an error if you attempt to print the .json() object to the command line. This is because the '{', '}' curly braces to be printed to the console.
This becomes especially annoying if developers wish to get 'under the hood'.

Here is the error:

```
UnicodeEncodeError: 'charmap' codec can't encode character '\u2019' in position 1444: character maps to <undefined>
```

This can be fixed by:
    - installing 'win-unicode-console'
        `py -mpip install win-unicode-console`
    - then running it while calling your python script...
        `py -mrun myPythonScript.py`

Another option is hardcoding your console to only print in utf-8. This is a bad idea, as it could ruin many other scripts and/or make errors MUCH more difficult to track.
[More information](https://stackoverflow.com/questions/5419/python-unicode-and-the-windows-console/32176732#32176732).


## Support

Feel free to make suggestions or provide feedback regarding the library. Thanks.
Reach out at [lisivickmatt@gmail.com]('mailto:lisivickmatt@gmail.com')
