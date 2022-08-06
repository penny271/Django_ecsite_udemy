# logging

import logging

#- __name__とするとファイル間で被ることなく、どのファイルのロガーかわかるので推奨)
logger = logging.getLogger(__name__)
# loggerの閾値
logger.setLevel(logging.DEBUG)

#- handler
s_handler = logging.StreamHandler() # ターミナルへの標準出力のハンドラー
f_handler = logging.FileHandler('logging2.log', encoding='utf-8', mode='w') # ファイルへの出力(utf-8), mode='w'とする

#- handlerのログレベル
s_handler.setLevel(logging.DEBUG) # s_handlerのログレベルをDEBUGに設定
f_handler.setLevel(logging.ERROR) # f_handlerのログレベルをWARNINGに設定

#- Formatter
s_formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s') # ログのフォーマットを設定

f_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s') # ログのフォーマットを設定 s_handler.setFormatter(s_formatter) # s_handlerにフォーマットを設定

#- handlerにformatterを設定
s_handler.setFormatter(s_formatter) # s_handlerにフォーマットを設定
f_handler.setFormatter(f_formatter) # f_handlerにフォーマットを設定

#- loggerにs_handlerを設定
logger.addHandler(s_handler) # loggerにs_handlerを設定
logger.addHandler(f_handler) # loggerにf_handlerを設定

logger.debug('デバッグログ')
logger.info('インフォログ')
logger.warning('ワーニングログ')
logger.error('エラーログ')
logger.critical('クリティカルログ')

a = 10
b = 0
try:
    c = a/b
except Exception as e:
    #- exc_info=True とするとどこでエラーが発生したか記述される
    logger.error(e, exc_info=True)