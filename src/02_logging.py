import logging

# create logger and set the logging level
logging.basicConfig(level=logging.DEBUG)

"""
Valid options for level are:
DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future
(e.g. ‘disk space low’). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.


Logging levels are just integers. 
The default level is WARNING
DEBUG = 10, INFO = 20, WARNING = 30, ERROR = 40, CRITICAL = 50
"""


# Run the same code
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

