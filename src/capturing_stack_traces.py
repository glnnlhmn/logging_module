import python_logging

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
"""