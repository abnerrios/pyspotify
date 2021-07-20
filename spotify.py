from typing import List
from requests import request
import json
import sys
from urllib.parse import urljoin

errors = {'LIST_LENGHT': 'ids length is bigger than the 50 allowed'}

class Tracks:
  """Spotify track catalog information."""
  def __init__(self, urlbase, headers):
    self.urlbase = urlbase
    self.headers = headers
  
  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.urlbase, path)

    response = request(method=method, url=url, headers=self.headers, data=payload)
    
    return response

  def get(self, track_id: int, ids: list):
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

  def audio_features(self, track_id: int, ids: list):
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


class Albums:
  """Spotify track catalog information."""
  def __init__(self, urlbase, headers):
    self.urlbase = urlbase
    self.headers = headers
  
  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.urlbase, path)

    response = request(method=method, url=url, headers=self.headers, data=payload)
    
    return response

  def get(self, album_id: int, ids: list):
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

class Artists:
  """Spotify track catalog information."""
  def __init__(self, urlbase, headers):
    self.urlbase = urlbase
    self.headers = headers
  
  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.urlbase, path)

    response = request(method=method, url=url, headers=self.headers, data=payload)
    
    return response

  def get(self, album_id: int, ids: list):
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


class Library:
  """Get a list of the items saved in the current Spotify user’s ‘Your Music’ library."""
  def __init__(self, urlbase, headers):
    self.urlbase = urlbase
    self.headers = headers
  
  def __request__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.urlbase, path)

    response = request(method=method, url=url, headers=self.headers, data=payload)
    
    return response

  def tracks(self, album_id: int, ids: list):
    """ Get Spotify catalog information for a single or several artists based on their Spotify IDs.
        For multiple artists provide Spotify IDs list on ids param  """
    querystring = None
    path = 'v1/me/artists/'

    if ids:
      if len(ids)<=50: 
        parameter = ','.join(ids)
        querystring = {'ids': parameter}
      else:
        raise IndexError(errors.get('LIST_LENGHT'))
    elif album_id:
      path = urljoin('v1/me/tracks/', album_id),

    return self.__request__(
      method = 'GET',
      path = path,
      querystring = querystring
    )

class spotify_api:
  def __init__(self, authorization_token):
    self.urlbase = 'https://api.spotify.com/'
    self.headers = {'Authorization': authorization_token}

  def __api__(self, **kwargs):
    path = kwargs.get('path')
    payload = kwargs.get('payload')
    method = kwargs.get('method')
    url = urljoin(self.urlbase, path)

    response = request(method=method, url=url, headers=self.headers, data=payload)
    
    return response
