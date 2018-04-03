# newsapi-python
A Python client for the [News API](https://newsapi.org/docs/)

##### Provided under MIT License by Matt Lisivick.
*Note: this library may be subtly broken or buggy. The code is released under
the MIT License – please take the following message to heart:*
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## General 

This is a Python client library for News API V2. The functions for the library should mirror the
endpoints from the [documentation](https://newsapi.org/docs/endpoints). 


## Installation
Installation for the package can be done via pip.

```commandline
    pip install newsapi-python
```

## Usage

After installation, import client into your project:

```python
from newsapi import NewsApiClient
```

Initialize the client with your API key:

```python
api = NewsApiClient(api_key='XXXXXXXXXXXXXXXXXXXXXXX')
```

### Endpoints
 
#### Top Headlines

```python
api.get_top_headlines(sources='bbc-news')
```
#### Everything

```python
api.get_everything(q='bitcoin')
```
#### Sources

```python
api.get_sources()
```

## For Windows users printing to _cmd_ or _powershell_

You will encounter an error if you attempt to print the .json() object to the command line. This is because the '{', '}' curly braces to be printed to the console.
This becomes especially annoying if developers wish to get 'under the hood'.

Here is the error:
    UnicodeEncodeError: 'charmap' codec can't encode character '\u2019' in position 1444: character maps to <undefined>

This can be fixed by:
    - installing 'win-unicode-console'
        `py -mpip install win-unicode-console`
    - then running it while calling your python script...
        `py -mrun myPythonScript.py`

Another option is hardcoding your console to only print in utf-8. This is a bad idea, as it could ruin many other scripts and/or make errors MUCH more difficult to track.
[More information](https://stackoverflow.com/questions/5419/python-unicode-and-the-windows-console/32176732#32176732


## Support

Feel free to make suggestions or provide feedback regarding the library. Thanks.
Reach out at [lisivickmatt@gmail.com]('mailto:lisivickmatt@gmail.com')
