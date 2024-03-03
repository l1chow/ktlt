import logging

logger = logging.getLogger('my_logger')

# Thiết lập cấp độ logging cho logger
logger.setLevel(logging.DEBUG)

# Tạo một formatter để định dạng thông điệp log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Tạo một handler để xử lý việc ghi log ra file
file_handler = logging.FileHandler('app1.log','w')
file_handler.setLevel(logging.DEBUG)  # Thiết lập cấp độ của handler

# Gắn formatter với handler
file_handler.setFormatter(formatter)

# Thêm handler vào logger
logger.addHandler(file_handler)

# Sử dụng logger để ghi log
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
