import logging
# initialize the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
log_format = '%(levelname)s -> %(message)s'
console_handler.setFormatter(logging.Formatter(log_format))


def hypotenuse(a, b):
    h = round(((a ** 2 + b ** 2) ** 0.5), 2) 
    # call the logger
    logger.addHandler(console_handler)
    logger.info(f'Hypotenuse of %d and %d is %.2f', a, b, h)
    # logging.basicConfig(format='%(levelname)s -> %(message)s')
    # logging.info(f'Hypotenuse of {a} and {b} is {h}')

    return h

