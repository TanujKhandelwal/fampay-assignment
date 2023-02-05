from flask import Flask
from request import get_youtube_data
from cron import search_cronjob
from db import get_db_obj
import pymongo

app = Flask(__name__)
db = get_db_obj()

@app.route('/search/<search_text>') 
@app.route('/search/<search_text>/<page_no>')
def search(search_text, page_no = 1):
    page_no = int(page_no)
    items_per_page = 5
    offset = (page_no - 1) * items_per_page 
    response = list(db.YoutubeData.find({ "$text" : { "$search" : search_text, "$caseSensitive": False, "$diacriticSensitive": False }}).sort([('published_on', pymongo.DESCENDING)]).skip(offset).limit(items_per_page))
    return {"results":[{"title": r["title"], "description": r["description"], "video_url": r["video_url"], "published_on": r["published_on"]} for r in response]}

if __name__ == '__main__':
    app.run(debug=True, port=1000)