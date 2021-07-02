# *_*coding:utf-8 *_*
'''
Descri：
'''
import gensim, os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()


sentences = MySentences('../datasets/input')  # a memory-friendly iterator
# model = gensim.models.Word2Vec(sentences, min_count=1)
model = gensim.models.Word2Vec(iter=1,min_count=1, size=200, workers=4)  # an empty model, no training yet
model.build_vocab(sentences)  # can be a non-repeatable, 1-pass generator
# model.train(sentences)  # can be a non-repeatable, 1-pass generator
model.save('gensm.model')  # save model
# print(
# model.most_similar('中国')
# )   # check similar

# new_model = gensim.models.Word2Vec.load('/tmp/mymodel')  # load model

