import aiohttp, yarl

class Client:
    def __init__(self, *, session: aiohttp.ClientSession = None, loop = None):
        self._base_url = yarl.URL("https://jeyy-api.herokuapp.com/")
    
    @property
    def url(self) -> str:
        return str(self._base_url)
    
    @url.setter
    def set_url(self, value):
        self._base_url = yarl.URL(str(value))
