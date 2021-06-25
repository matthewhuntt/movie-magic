
import urllib.request
import json

with urllib.request.urlopen("https://api.themoviedb.org/3/movie/550?api_key=ef953584140e7c8e176e057b2e009fec") as url:
    owners = json.loads(url.read().decode())