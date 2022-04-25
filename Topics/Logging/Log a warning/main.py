import logging
# logger = logging.getLogger()
# logger.setLevel(logging.WARNING)
# console_handler = logging.StreamHandler()
# log_format = '%(levelname)s:%(message)s'
# console_handler.setFormatter(logging.Formatter(log_format))
# logger.addHandler(console_handler)
# logger.warning('Your application stopped working. Trying to restart!')
logging.basicConfig(format='%(levelname)s: %(message)s')
logging.warning('Your application stopped working. Trying to restart!')
