from typing import List
from requests import request
import json
from urllib.parse import urljoin
from requests.api import head

errors = {'LIST_LENGHT': 'ids length is bigger than the 50 allowed'}

class _Tracks:
  """Spotify track catalog information."""
  def __init__(self, urlbase, headers):
    self.__urlbase = urlbase
    self.__headers = headers
  
  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.__urlbase, path)
    result = None 
    
    try:
      response = request(method=method, url=url, headers=self.__headers, data=payload)
      
      if response.status_code<400:
        content = response.content
        result = json.loads(content)
      else:
        raise ConnectionError(response.status_code, response.text)
    except Exception as error:
      print(error)

    return result

  def get(self, track_id: int, ids: List):
    """ Get Spotify catalog information for a single or multiple track identified by their unique Spotify IDs.
        For multiple tracks provide Spotify IDs list on ids param  """
    querystring = None
    path = 'v1/tracks/'

    if ids:
      parameter = ','.join(ids)
      querystring = {'ids': parameter}
    elif track_id:
      path = urljoin('v1/tracks/', track_id),

    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )

  def audio_features(self, track_id: int, ids: List):
    """Get a detailed audio analysis for a single track identified by its unique Spotify ID."""
    
    querystring = None
    path = 'v1/audio-features/'

    if ids:
      if len(ids)<=50: 
        parameter = ','.join(ids)
        querystring = {'ids': parameter}
      else:
        raise IndexError(errors.get('LIST_LENGHT'))
    elif track_id:
      path = urljoin('v1/audio-features/', track_id),
    
    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )
    
  def audio_analysis(self, track_id: int):
    """Get a detailed audio analysis for a single track identified by its unique Spotify ID."""
    
    querystring = None
    path = urljoin('v1/audio-analysis/', track_id)
    
    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )


class _Albums:
  """Spotify track catalog information."""
  def __init__(self, urlbase, headers):
    self.__urlbase = urlbase
    self.__headers = headers
  
  
  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.__urlbase, path)
    result = None 
    
    try:
      response = request(method=method, url=url, headers=self.__headers, data=payload)
      
      if response.status_code<400:
        content = response.content
        result = json.loads(content)
      else:
        raise ConnectionError(response.status_code, response.text)
    except Exception as error:
      print(error)

    return result

  def get(self, album_id: int, ids: List):
    """ Get Spotify catalog information for a single or multiple albums identified by their Spotify IDs.
        For multiple albums provide Spotify IDs list on ids param  """
    querystring = None
    path = 'v1/albums/'

    if ids:
      if len(ids)<=50: 
        parameter = ','.join(ids)
        querystring = {'ids': parameter}
      else:
        raise IndexError(errors.get('LIST_LENGHT'))
    elif album_id:
      path = urljoin('v1/albums/', album_id),

    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )

class _Artists:
  """Spotify track catalog information."""
  def __init__(self, urlbase, headers):
    self.__urlbase = urlbase
    self.__headers = headers
  
  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.__urlbase, path)
    result = None 
    
    try:
      response = request(method=method, url=url, headers=self.__headers, data=payload)
      
      if response.status_code<400:
        content = response.content
        result = json.loads(content)
      else:
        raise ConnectionError(response.status_code, response.text)
    except Exception as error:
      print(error)

    return result

  def get(self, album_id: int, ids: List):
    """ Get Spotify catalog information for a single or several artists based on their Spotify IDs.
        For multiple artists provide Spotify IDs list on ids param  """
    querystring = None
    path = 'v1/artists/'

    if ids:
      if len(ids)<=50: 
        parameter = ','.join(ids)
        querystring = {'ids': parameter}
      else:
        raise IndexError(errors.get('LIST_LENGHT'))
    elif album_id:
      path = urljoin('v1/artists/', album_id),

    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )


class _Library:
  """Get a list of the items saved in the current Spotify user’s ‘Your Music’ library."""
  def __init__(self, urlbase, headers):
    self.__urlbase = urlbase
    self.__headers = headers

  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.__urlbase, path)
    result = None 
    
    try:
      response = request(method=method, url=url, headers=self.__headers, data=payload)
      
      if response.status_code<400:
        content = response.content
        result = json.loads(content)
      else:
        raise ConnectionError(response.status_code, response.text)
    except Exception as error:
      print(error)

    return result

  def albums(self, limit: int = 20, offset: int = 0):
    """ Get a list of the albums saved in the current Spotify user’s ‘Your Music’ library. """
    # adjust the limit for max allowed 
    if limit>50:
      limit = 50
    
    querystring = {'limit': limit, 'offset': offset}
    path = 'v1/me/albums/'

    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )

  def tracks(self, limit: int = 20, offset: int = 0):
    """ Get a list of the songs saved in the current Spotify user’s ‘Your Music’ library. """
    # adjust the limit for max allowed 
    if limit>50:
      limit = 50
    
    querystring = {'limit': limit, 'offset': offset}
    path = 'v1/me/tracks/'

    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )

class Api:
  def __init__(self, authorization_token):
    urlbase = 'https://api.spotify.com/'
    headers = {'Authorization': f'Bearer {authorization_token}'}

    self.tracks = _Tracks(urlbase=urlbase, headers=headers)
    self.albums = _Albums(urlbase=urlbase, headers=headers)
    self.artists = _Artists(urlbase=urlbase, headers=headers)
    self.library = _Library(urlbase=urlbase, headers=headers)