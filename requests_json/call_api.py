import requests
import json

BASE_URI = "https://api.github.com"

def get_uri(uri):
    response = requests.get(BASE_URI + uri)

    """ 
    Helper function: raise an error if response code is a:
     - Client Error (HTTP 4xx), or a
     - Server Error (HTTP 5xx)
    """
    response.raise_for_status()

    return response.json()


data = get_uri("/users/glasnt")
print(data["blog"])

