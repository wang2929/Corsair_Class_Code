from requests_oauthlib import OAuth1
import requests
import os
import pprint

"""
1. CREATE A .env FILE
  - API KEY (var)
  - SECRET KEY (var)
2. CREATE A .gitignore FILE
  - .env
  - __pycache__
  - .venv
3. dotenv `load_dotenv`
4. `load_dotenv` path to the `.env` file
5. utilize os to enter the `environ` which returns a dict of key, val pairs
"""


class NounProjectAPI:
    """
    Interacts with the Noun Project API
    URL: https://thenounproject.com/api/
    ACCEPTS: `search_param` of type `str` that should describe the noun you want a icon for
    RETURNS: `str` url for the icons location
    MUST HAVE IN `.env` file:
    - API KEY
    - SECRET KEY
    """
    API_KEY = os.environ.get("API_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PP = pprint.PrettyPrinter(indent=1, depth=2)
        
    def get_img(self, search_param:str) -> str:
        try:
            if not self.API_KEY:
                raise Exception("You are missing an API Key from the Noun Project")
            if not self.SECRET_KEY:
                raise Exception("You are missing a SECRET KEY from the Noun Project")

            auth = OAuth1(self.API_KEY, self.SECRET_KEY )
            endpoint = f"https://api.thenounproject.com/v2/icon?query={search_param}"

            response = requests.get(endpoint, auth=auth)
            response = response.json()
            self.PP.pprint(response.get("icons")[0].get("thumbnail_url"))
            return response.get("icons")[0].get("thumbnail_url")
        except Exception as e:
            print(e)
            return ''
    
    def __call__(self, search_param:str) -> str:
        return self.get_img(search_param)
