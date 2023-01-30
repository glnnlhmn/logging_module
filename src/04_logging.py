import logging

"""
Example can be uncommented and run one at a time to see output

All examples are using default output to the console
"""
# # example 1
# logging.basicConfig(format='%(process)d - %(levelname)s - %(message)s')
# logging.warning('This is a warning message')

# # example 2
# logging.basicConfig(
#     format='%(asctime)s - %(message)s',
#     level=logging.INFO
# )
# logging.info('Admin logged in')

# # example 3 add date and time format
# logging.basicConfig(
#     format='%(asctime)s - %(message)s',
#     datefmt='%d-%b-%y %H:%M:%S',
# )
# logging.warning('Admin logged out')
