import logging

name = 'Ned'

logging.error('%s raised an error', name)

"""
logging.warning(f'{name} raised an error')  

f-string available in Python 3.6+ but you should use the %s method

This support the lazy construction of the message string, which can be expensive to construct.
"""