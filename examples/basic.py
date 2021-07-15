import asyncio
from isometric_api import Client

cli = Client()

async def run():
    iso = await cli.isometric("11111 11111 11411 11411 11411 11411 31441 33144 23114 23314 22314- 0 0555 0505 0535- 0 0565 0606 0535- 0 0555 0555 0555")

    iso.fp # --> `io.BytesIO` object.
    iso.resp # --> `aiohttp.ClientResponse` object.

asyncio.run(run())
