import logging
import sys
import os

def get_logger():
    """Получить настроенный логгер"""
    logger_name = os.environ.get('LOGGER_NAME', 'nuudel_app')
    log_level = os.environ.get('LOG_LEVEL', 'DEBUG')
    
    logger = logging.getLogger(logger_name)
    
    if logger.handlers:
        return logger
    
    # Настройка уровня из переменной окружения
    level = getattr(logging, log_level.upper(), logging.DEBUG)
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    
    # Разный формат для разных окружений
    if os.environ.get('VERCEL'):
        # Для Vercel - простой формат
        formatter = logging.Formatter('%(levelname)s - %(funcName)s - %(message)s')
    else:
        # Для локальной разработки - подробный формат
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s'
        )
    
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    
    return logger

# Единственный экземпляр логгера
logger = get_logger()