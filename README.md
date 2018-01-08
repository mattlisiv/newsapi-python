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

## Support

Feel free to make suggestions or provide feedback regarding the library. Thanks.
Reach out at [lisivickmatt@gmail.com]('mailto:lisivickmatt@gmail.com')