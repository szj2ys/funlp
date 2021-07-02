import sys
sys.path.append('..')
from funlp import TextRank4Sentence
import codecs

rank4sent = TextRank4Sentence(use_w2v=False,tol=0.0001)

text = codecs.open('../datasets/input/当前中国经济实现完全数字化，小微企业的投资机会将是蓝海.txt', 'r', 'utf-8').read()

po=rank4sent.summarize(text, 2)
# print(list(po))
print(''.join(list(po)))

