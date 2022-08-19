import logging
import sys


def get_logger(log_file_name):
    """
    Creates log handler
    :param
        log_file_name: Filename to stores logs
    :return:
        log handler
    """
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log_file = logging.Formatter('%(asctime)s - '
                                 '%(levelname)s - %(message)s')
    log_console = logging.Formatter('%(asctime)s - '
                                    '%(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_console)
    log.addHandler(stream_handler)
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setFormatter(log_file)
    log.addHandler(file_handler)
    return log
