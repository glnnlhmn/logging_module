"""
Creating our own loggers.

Note: can’t be configured using basicConfig().
"""
import logging

# Create a custom logger named 'example_logger'
logger = logging.getLogger("example_logger")

logger.warning("This is a warning")  # This is a warning

# root is the name of the default logger
print(f"logging.root.level: {logging.root.level}")

# root is the name of the default logger
print(f"logger instance of logging: {logger}, level: {logger.root.level}")
