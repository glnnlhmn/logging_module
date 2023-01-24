"""
logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True, encoding=None)
"""

import logging
import logging.config

logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.debug('This is a debug message')

"""
file format: https://docs.python.org/3/library/configparser.html#module-configparser
"""