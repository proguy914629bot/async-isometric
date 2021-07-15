import asyncio # For running corountines
from isometric_api import Client # Import the Client class

cli = Client() # Initiate the Client

async def run(): # Make the corountine
    iso = await cli.isometric("11111 11111 11411 11411 11411 11411 31441 33144 23114 23314 22314- 0 0555 0505 0535- 0 0565 0606 0535- 0 0555 0555 0555") # Run the isometric

    iso.fp # --> `io.BytesIO` object.
    iso.resp # --> `aiohttp.ClientResponse` object.

asyncio.run(run()) # Run the corountine function we made above.
