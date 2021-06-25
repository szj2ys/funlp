import sys
sys.path.append('..')
from funlp import TextRank4Sentence
import codecs
import datetime
mod = TextRank4Sentence(use_w2v=False,tol=0.0001)

text = codecs.open('../datasets/input/当前中国经济实现完全数字化，小微企业的投资机会将是蓝海.txt', 'r', 'utf-8').read()
print('摘要:')
start_time = datetime.datetime.now()
po=mod.summarize(text, 10)
print(po)
print(datetime.datetime.now() - start_time)
