from bson import ObjectId
from dataclasses import field, dataclass
from time import time

@dataclass
class YoutubeData:
  video_id: str = None
  c: float = field(default_factory=time)
  u: float = field(default_factory=time)
  title: str = ""
  description: str = ""
  published_on: float = 0.0
  video_url: str = ""
    