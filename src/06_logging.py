import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

"""
If exc_info is True, exception information is added to the logging message. 
This is useful for error messages so that the full stack trace is printed. 

The default is False.

Other DEBUG kwargs:
    stack_info: If True, adds the stack information to the log message.
    stacklevel: Specifies how many levels up the stack to walk to find the caller’s module.
    extra: A dictionary of values to add to the log record. (multithread servers where dealing  with different context
            for each thread.  Examine LogRecord attributes for more info)
"""