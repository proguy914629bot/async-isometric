import asyncio # For running corountines
from isometric_api import Client # Import the Client class

cli = Client() # Initiate the class

asyncio.run(cli.isometric("11111 11111 11411 11411 11411 11411 31441 33144 23114 23314 22314- 0 0555 0505 0535- 0 0565 0606 0535- 0 0555 0555 0555", save_to='/path/to/file.png')) # Run the isometric.
