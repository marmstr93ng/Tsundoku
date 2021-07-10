import requests
import json
from typing import Dict, Any

class GoogleBooks(object):
    """See: https://developers.google.com/books/docs/v1/using#WorkingVolumes"""

    def __init__(self):
        self._base_url = "https://www.googleapis.com/books/v1"
    
    def search(self, search_term: str, max_results: int = 1) -> Dict[str, Any]:
        path = "/volumes"
        resp = requests.get(self._base_url+path, params={"q" : search_term, "maxResults" : max_results})
        if self._resp_check(resp):
            return json.loads(resp.content)
    
    def _resp_check(self, resp: requests.models.Response) -> bool:
        if resp.status_code == 200:
            return True
        else:
            raise Exception("{} - {}".format(resp.status_code, resp.url))
