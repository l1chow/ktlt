from customLogger import custom_logger

# Cấu hình logger
logger = custom_logger('my_logger', 'app2.log')

# Sử dụng logger để ghi log
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
