import requests
from constants import YOUTUBE_AUTH_KEY

def get_youtube_data(search_text):
  try:
    response = requests.get(url="https://www.googleapis.com/youtube/v3/search", params={'key':YOUTUBE_AUTH_KEY,'part':"snippet", "q": search_text, "maxResults": 25}).json()
    return response
  except Exception as e:
    print(e)
  return []