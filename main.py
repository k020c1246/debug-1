#loggingを使う方法
import logging

# ログレベルを DEBUG に変更。
# logger.logにログを出力する。
logging.basicConfig(filename='logger.log', level=logging.DEBUG)
# logを出力しない場合は、この下の行のコメントを外す
# logging.disable(logging.CRITICAL)

logging.debug('program begins.')

sum = 0
logging.debug('sum = {}'.format(sum))

# sum 1 through 100
for i in range(1,101):
   sum += i
   logging.debug('sum = {}, i = {}'.format(sum, i))

print('SUM_1^100 = {}'.format(sum))

logging.debug('program ends.')
