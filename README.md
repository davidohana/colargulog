# colargulog
Python Logging with Colored Arguments

<img src="https://miro.medium.com/max/1400/1*ZaOru_rZsnfNCQaPJ5D60g.png">

A Python 3 logging formatter that highlights each argument in the logging format string
with a different alternating color.  
Logging directives are written in the Python 3.2+ brace-format
instead of the legacy `%s` / `%d` / .. format that is traditionally accepted by Python logger.


Bootstrapping code:
```python
import logging
from colargulog import ColorizedArgsFormatter

root_logger = logging.getLogger()
console_handler = logging.StreamHandler(stream=sys.stdout)
console_format = "%(asctime)s - %(levelname)-8s - %(name)-25s - %(message)s"
colored_formatter = ColorizedArgsFormatter(console_format)
console_handler.setFormatter(colored_formatter)
root_logger.addHandler(console_handler)
```

Sample Logging code:
```python
logger = logging.getLogger(__name__)
logger.info("Hello World")
logger.info("Request from {} handled in {:.3f} ms", socket.gethostname(), 11)
logger.info("Request from {} handled in {:.3f} ms", "127.0.0.1", 33.1)
logger.info("My favorite drinks are {}, {}, {}, {}", "milk", "wine", "tea", "beer")
logger.debug("this is a {} message", logging.getLevelName(logging.DEBUG))
logger.info("this is a {} message", logging.getLevelName(logging.INFO))
logger.warning("this is a {} message", logging.getLevelName(logging.WARNING))
logger.error("this is a {} message", logging.getLevelName(logging.ERROR))
logger.critical("this is a {} message", logging.getLevelName(logging.CRITICAL))
logger.info("Does old-style formatting also work? %s it is, but no colors (yet)", True)
```

See my [Medium Story](https://medium.com/@davidoha/python-logging-colorize-your-arguments-41567a754ac?source=friends_link&sk=ef35bfb7ec017d58e358ebc99fe26bdf) for more information. 


Customization with different color mapping and additional alternating color:
<img src="https://miro.medium.com/max/1400/1*bWzogOG0_V597SKjFnAF7A.png">
 
### License: 
Apache-2.0