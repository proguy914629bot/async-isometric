import aiohttp, yarl, asyncio, pathlib, typing
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
        
        ..note::
        
            This is not used in the current version. It
            will be used in a newer version in the future.
            
    url: :class:`str`
        The base url to be used.
    """
    
    __slots__ = ('_base_url', 'session', 'loop', 'url')
    
    def __init__(self, *, session: typing.Optional[aiohttp.ClientSession] = None, loop = None):
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

    async def isometric(self, iso_code: str, *, save_to: str = None) -> IsometricData:
        """Runs an Isometric.
        This calls the `/isometric` endpoint to the API.
        
        Parameters
        ----------
        iso_code: :class:`str`
            The Isometric Code.
        save_to: :class:`str`
            Where to save the isometric file.
            Defaults to None (Doesn't save)
            
        Raises
        ------
        IsometricError
            This raises when a unknown error was found.
            
        Returns
        -------
        :class:`IsometricData`
            The Isometric data provided by the API.
        """
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
