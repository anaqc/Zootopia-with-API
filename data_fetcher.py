import requests
import os
from dotenv import load_dotenv


# Load Environment Variables
load_dotenv()

# Constants
# Access Environment Variables
API_KEY = os.getenv("API_KEY")
API_URL = 'https://api.api-ninjas.com/v1/animals?name={}'


def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  url = API_URL.format(animal_name)
  response = requests.get(url, headers={'X-Api-Key': API_KEY})
  if response.status_code == requests.codes.ok:
      return response.json()

  else:
      print("Error:", response.status_code, response.text)