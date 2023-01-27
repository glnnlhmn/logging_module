import logging

# Bad!  Check out a more efficient alternative below.
logging.warning("To iterate is %s, to recurse %s" % ("human", "divine"))

# Better: formatting doesn't occur until it really needs to.
logging.warning("To iterate is %s, to recurse %s", "human", "divine")


"""
logging.warning(f'{name} raised an error')  

f-string available in Python 3.6+ but you should use the %s method

This support the lazy construction of the message string, which can be expensive to construct.

The method signature for Logger.warning() looks like this:

def warning(self, msg, *args, **kwargs)

"""