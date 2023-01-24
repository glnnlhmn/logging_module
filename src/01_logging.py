import logging
"""Basic logging to demonstrate the default values of the logging module."""


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# root is the name of the default logger
print(f'logging.root.level: {logging.root.level}')


"""Output:

WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
"""



