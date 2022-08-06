# logging

import logging
import logging.config

#- 下記からファイルを読み込む
logging.config.fileConfig(fname='conf/logger.conf')

#- __name__とするとファイル間で被ることなく、どのファイルのロガーかわかるので推奨)
logger = logging.getLogger(__name__)

logger.debug('デバッグログ')
logger.info('インフォログ')
logger.warning('ワーニングログ')
logger.error('エラーログ')
logger.critical('クリティカルログ')

#- logger.conf内の qualname=samplelogger を指定している
logger = logging.getLogger('samplelogger')

logger.debug('デバッグログ')
logger.info('インフォログ')
logger.warning('ワーニングログ')
logger.error('エラーログ')
logger.critical('クリティカルログ')