class IsometricData:
    """A read-only isometric data.
    
    ..warning::
        Do not create/initiate this class yourself.
        
        This class is only used to have read-only data
        from the API.
        
    Attributes
    ----------
    resp: :class:`aiohttp.ClientResponse`
        The response used to query to the API.
    fp: :class:`io.BytesIO`
        The BytesIO class representing the buffer
        of the Isometric image.
    path: typing.Optional[:class:`pathlib.Path`]
        The path used. This can be ``None`` when
        `save_to` argument in `Client.isometric` is None.
    """
    def __init__(self, response, fp, path):
        self.resp = response
        self.fp = fp
        self.path = path
