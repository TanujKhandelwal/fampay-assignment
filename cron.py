import time
from db import get_db_obj
from request import get_youtube_data
from youtube_data import YoutubeData
from datetime import datetime
from bson import ObjectId
import datetime

db = get_db_obj()

def search_cronjob():
  while True:
    yt_data = get_youtube_data("cricket").get("items", [])
    arr = []
    for item in yt_data:
      if not item["id"]["kind"] == "youtube#video":
        continue
      video_id = item["id"]["videoId"]
      data = db.YoutubeData.find_one({"video_id": video_id})
      if data:
        continue
      snippet = item.get("snippet", {})
      obj = YoutubeData()
      obj.video_id = video_id
      obj.title = snippet.get("title")
      obj.description = snippet.get("description")
      obj.video_url = "https://www.youtube.com/watch?v=" + video_id
      obj.published_on = datetime.datetime.strptime(snippet.get("publishTime"),"%Y-%m-%dT%H:%M:%SZ").timestamp()*1000
      arr.append(obj.__dict__)
    if len(arr):
      db.YoutubeData.insert_many(arr)
    time.sleep(10)
      
if __name__ == '__main__':
  db.YoutubeData.create_index('video_id', unique = True)
  db.YoutubeData.create_index('published_on')
  db.YoutubeData.create_index([("title", "text"), ("description", "text")])
  search_cronjob()