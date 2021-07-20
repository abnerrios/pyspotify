import os
from pyxportify import Api
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN') 
spotify = Api(authorization_token=token)

if __name__=='__main__':
  #TODO
  pass