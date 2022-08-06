# logging

import logging
import logging.handlers

logger = logging.getLogger(__name__)

# RotatingFileHandler: ログローテーションをサポートしたファイルHandler
r_handler = logging.handlers.RotatingFileHandler(
    'logs/rotation_file.log',
    maxBytes=1000,
    backupCount=5,
    encoding='utf-8'
)

t_handler = logging.handlers.TimedRotatingFileHandler(
    'logs/rotation_time_file.log',
    when='S', # M(分), D(日)
    interval=10, # ローテ―トする間隔
    backupCount=5, # バックアップするファイル数
    encoding='utf-8'
)

logger.setLevel(logging.DEBUG)

sample_formatter = logging.Formatter('%(name)s-%(asctime)s-%(levelname)s-%(message)s')
r_handler.setFormatter(sample_formatter)
t_handler.setFormatter(sample_formatter)
logger.addHandler(r_handler)
logger.addHandler(t_handler)

import time

for _ in range(1000):
    logger.debug('デバッグログ')
    logger.info('インフォログ')
    logger.warning('ワーニングログ')
    logger.error('エラーログ')
    logger.critical('クリティカルログ')
    time.sleep(1)



# logger.debug('デバッグログ')
# logger.info('インフォログ')
# logger.warning('ワーニングログ')
# logger.error('エラーログ')
# logger.critical('クリティカルログ')

# #- logger.conf内の qualname=samplelogger を指定している
# logger = logging.getLogger('samplelogger')

# logger.debug('デバッグログ')
# logger.info('インフォログ')
# logger.warning('ワーニングログ')
# logger.error('エラーログ')
# logger.critical('クリティカルログ')