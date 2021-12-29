import logging

# playwright logging level
GERAPY_PLAYWRIGHT_LOGGING_LEVEL = logging.WARNING

# playwright timeout
GERAPY_PLAYWRIGHT_DOWNLOAD_TIMEOUT = 30

# playwright browser window
GERAPY_PLAYWRIGHT_WINDOW_WIDTH = 1400
GERAPY_PLAYWRIGHT_WINDOW_HEIGHT = 700

# playwright browser default ua
GERAPY_PLAYWRIGHT_DEFAULT_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

# playwright settings
GERAPY_PLAYWRIGHT_HEADLESS = True
GERAPY_PLAYWRIGHT_CHANNEL = None
GERAPY_PLAYWRIGHT_EXECUTABLE_PATH = None
GERAPY_PLAYWRIGHT_SLOW_MO = None
# GERAPY_PLAYWRIGHT_IGNORE_DEFAULT_ARGS = False
# GERAPY_PLAYWRIGHT_HANDLE_SIGINT = True
# GERAPY_PLAYWRIGHT_HANDLE_SIGTERM = True
# GERAPY_PLAYWRIGHT_HANDLE_SIGHUP = True
GERAPY_PLAYWRIGHT_DEVTOOLS = False
GERAPY_PLAYWRIGHT_PRETEND = True

# playwright args
GERAPY_PLAYWRIGHT_DISABLE_EXTENSIONS = True
GERAPY_PLAYWRIGHT_HIDE_SCROLLBARS = True
GERAPY_PLAYWRIGHT_MUTE_AUDIO = True
GERAPY_PLAYWRIGHT_NO_SANDBOX = True
GERAPY_PLAYWRIGHT_DISABLE_SETUID_SANDBOX = True
GERAPY_PLAYWRIGHT_DISABLE_GPU = True

# ignore resource types, ResourceType will be one of the following: ``document``,
# ``stylesheet``, ``image``, ``media``, ``font``, ``script``,
#  ``texttrack``, ``xhr``, ``fetch``, ``eventsource``, ``websocket``,
#  ``manifest``, ``other``.
GERAPY_PLAYWRIGHT_IGNORE_RESOURCE_TYPES = []
GERAPY_PLAYWRIGHT_SCREENSHOT = None
GERAPY_PLAYWRIGHT_SLEEP = 0
GERAPY_ENABLE_REQUEST_INTERCEPTION = False


GERAPY_CHECK_PLAYWRIGHT_INSTALLED = False
