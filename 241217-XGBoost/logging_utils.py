# logging_utils.py
import logging
import os

def get_logger(name, log_file='logs/app.log', level=logging.INFO):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

class StreamToLogger(object):
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level
    def write(self, message):
        if message.rstrip():
            self.logger.log(self.level, message.rstrip())
    def flush(self):
        pass
