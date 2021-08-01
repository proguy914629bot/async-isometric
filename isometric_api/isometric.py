import typing
from .dataclass import *

class Isometric:
    """
    The Isometric Class.
    """
    def __init__(self, client):
        self._client = client
        
    async def run(self, iso_code: str, *, save_to: str = None) -> IsometricData:
        """Runs an Isometric.
        
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
        uri = str(self._client._base_url)
        async with self.session.get(f'{uri}/isometric', params={"iso_code": str(iso_code)}) as resp:
            if not resp.content_type.startswith("image/"):
                await self._client._raise_error(resp)
            
            fp = BytesIO(await resp.read())
            if save_to:
                path = pathlib.Path(str(save_to))
                path.write_bytes(fp.getbuffer())
            else:
                path = None
                
            return IsometricData(resp, fp, path)
        
    async def __call__(self, iso_code: str, *, save_to: str = None) -> IsometricData:
        """Runs an Isometric.
        
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
        return self.run(iso_code, save_to=save_to)
    
    async def codes(self) -> typing.List[str]:
        """Gets the codes of the Isometric.
        
        Raises
        ------
        IsometricError
            This raises when a unknown error was found.
            
        Returns
        -------
        List[:class:`str`]
            The isometric codes.
        """
        uri = str(self._client._base_url)
        async with self._client.session.get(f'{uri}/isometric/codes') as resp:
            try:
                js = await resp.json()
            except:
                await self._client._raise_error(resp)
                
            return js.get('iso_codes')
