import aiohttp, yarl, asyncio, pathlib
from io import BytesIO
from .errors import *
from .dataclass import *

async def raise_error(resp):
    try:
        js = await resp.json()
    except:
        try:
            js = {'info': (await resp.text())}
        except:
            return
    
    raise IsometricError(resp, js.get('info', js))

class Client:
    def __init__(self, *, session: aiohttp.ClientSession = None, loop = None):
        self._base_url = yarl.URL("https://jeyy-api.herokuapp.com/")
        self.session = session or aiohttp.ClientSession()
        self.loop = loop or asyncio.get_event_loop()
    
    @property
    def url(self) -> str:
    """The Base URL used for the API."""
        return str(self._base_url)
    
    @url.setter
    def set_url(self, value):
        self._base_url = yarl.URL(str(value))

    async def isometric(self, iso_code: str, *, save_to: str = None):
        uri = str(self._base_url)
        async with self.session.get(uri, params={"iso_code": str(iso_code)}) as resp:
            if not resp.content_type.startswith("image/"):
                await raise_error(resp)
            
            fp = BytesIO(await resp.read())
            if save_to:
                path = pathlib.Path(str(save_to))
                path.write_bytes(fp.getbuffer())
            else:
                path = None
                
            return IsometricData(resp, fp, path)
