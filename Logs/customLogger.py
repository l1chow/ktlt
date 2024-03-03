import logging

def custom_logger(name, log_file, level=logging.INFO):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Tạo một logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Tạo một file handler để ghi log ra file
    file_handler = logging.FileHandler(log_file,'w')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    
    # Thêm handler vào logger
    logger.addHandler(file_handler)
    
    return logger
