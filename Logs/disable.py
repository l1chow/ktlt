import logging

# Cấu hình level logging
logging.basicConfig(level=logging.DEBUG)

# Tạo một logger
logger = logging.getLogger(__name__)

# Thử ghi log ở mức DEBUG
logger.debug('This is a debug message')

# Ngăn chặn xử lý các yêu cầu nhật ký ở mức INFO hoặc thấp hơn
logging.disable(logging.INFO)

# Thử ghi log ở mức INFO (sẽ không được xử lý do đã bị vô hiệu hóa)
logger.info('This is an info message')

# Thử ghi log ở mức WARNING (vẫn được xử lý bình thường)
logger.warning('This is a warning message')

# Kích hoạt lại xử lý các yêu cầu nhật ký
logging.disable(logging.NOTSET)

# Thử ghi log ở mức INFO (lại được xử lý bình thường)
logger.info('This is another info message')
