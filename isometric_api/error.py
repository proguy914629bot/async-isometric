class IsometricError(Exception):
    """The base exception for the Isometric API.
    
    Attributes
    ----------
    resp: :class:`aiohttp.ClientResponse`
        The response used to make the call to the API.
    error :class:`str`
        The error sent by the API.
    status :class:`int`
        The status code of the response.
    """
    def __init__(self, resp, error):
        self.resp = resp
        self.error = error
        self.status = resp.status
        super().__init__("Status code %s: %s" % (str(self.status), str(self.error)))
