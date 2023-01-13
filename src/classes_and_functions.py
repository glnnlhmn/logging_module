"""
Creating our own loggers.  We are using Logger, LogRecord, Handlers and Formatter classes

Loggers create LogRecords.  Handlers send LogRecords to a destination.
"""
import python_logging

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')  # This is a warning

# This code matches the text but not the video output in the tutorial (the video is wrong)
