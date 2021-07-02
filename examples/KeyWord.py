from funlp import TextRank4Words
import codecs

rank4words = TextRank4Words(tol=0.0001,window=2)

text = codecs.open('../datasets/input/当前中国经济实现完全数字化，小微企业的投资机会将是蓝海.txt', 'r', 'utf-8').read()

po=rank4words.summarize(text, 1000)
print(list(po))
