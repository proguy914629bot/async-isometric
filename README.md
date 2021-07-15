A async wrapper to the Isometric API (https://jeyy-api.herokuapp.com/)

# Guide:
Here are guides on how to do stuff with the Isometric API Wrapper.

## Installation:
This package is currently not in PyPi, so you need to install from github.
You also need Git.

To install this package, all you need to do is:
```sh
pip install git+https://github.com/proguy914629bot/isometric-api
```

## Examples:
Here are some examples that can help!

### Basic Isometic Example
```py
from isometric_api import Client

cli = Client()

await cli.isometric("11111 11111 11411 11411 11411 11411 31441 33144 23114 23314 22314- 0 0555 0505 0535- 0 0565 0606 0535- 0 0555 0555 0555")
```
