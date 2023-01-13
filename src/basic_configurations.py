"""
You will notice that the logging module breaks PEP8 styleguide and uses camelCase naming conventions. This
is because it was adopted from Log4j, a logging utility in Java. It is a known issue in the package but by
the time it was decided to add it to the standard library, it had already been adopted by users and
changing it to meet PEP8 requirements would cause backwards compatibility issues.
"""
import python_logging

# first part of tutorial commented out because it can only be called once
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will be logged')

logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

#  if filemode is not specified, it defaults to append mode
