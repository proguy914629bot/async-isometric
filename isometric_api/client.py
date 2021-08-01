import aiohttp, yarl, asyncio, pathlib, typing
from io import BytesIO
from .errors import *
from .dataclass import *
from .isometric import *

class Client:
    """
    The base-client of the Isometric API.
    
    Parameters
    ----------
    session: :class:`aiohttp.ClientSession`
        The session used for querying to API endpoints.
        This defaults to making a brand new session.
    loop:
        The loop to be used. Default to a loop from
        `asyncio.get_event_loop()`

        ..note::
            This is not used in the current version. It
            will be used in a newer version in the future.
            
    Attributes
    ----------
    session: :class:`aiohttp.ClientSession`
        The session used for querying to API endpoints.
    loop:
        The loop to be used.
        
        .. note::
            This is not used in the current version. It
            will be used in a newer version in the future.
            
    url: :class:`str`
        The Base URL used to query endpoints.
    """
    
    __slots__ = ('_base_url', 'session', 'loop', 'url')
    
    def __init__(self, *, session: typing.Optional[aiohttp.ClientSession] = None, loop = None):
        self._base_url = yarl.URL(self._generate_url("https://jeyy-api.herokuapp.com/"))
        self.session = session or aiohttp.ClientSession()
        self.loop = loop or asyncio.get_event_loop()
    
    @property
    def url(self) -> str:
        """The Base URL used to query endpoints."""
        return str(self._base_url)
    
    @url.setter
    def set_url(self, value):
        self._base_url = yarl.URL(self._generate_url(value))
        
    async def _raise_error(resp):
        try:
            js = await resp.json()
        except:
            try:
                js = {'info': (await resp.text())}
            except:
                return
    
        raise IsometricError(resp, js.get('info', js))
        
    def _generate_url(self, url):
        uri = str(url)
        
        if uri.endswith("/"):
            uri = uri[:-1]
            
        return uri

    @property
    def isometric(self) -> Isometric:
        return Isometric(self)
