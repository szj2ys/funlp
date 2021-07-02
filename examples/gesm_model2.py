# *_*coding:utf-8 *_*
'''
Descri：https://radimrehurek.com/gensim/models/word2vec.html#introduction
'''
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models import Phrases

# Train a bigram detector.
bigram_transformer = Phrases(common_texts,min_count=1)
## Apply the trained MWE detector to a corpus, using the result to train a Word2vec model.
model = Word2Vec(sentences=bigram_transformer[common_texts],iter=2, size=100, window=5, min_count=1, workers=4)
# model = Word2Vec(sentences=common_texts,iter=2, size=100, window=5, min_count=1, workers=4)
model.save("word2vec.model")


# If you save the model you can continue training it later
model = Word2Vec.load("word2vec.model")
model.train([["hello", "world"]], total_examples=1, epochs=1)

# The trained word vectors are stored in a KeyedVectors instance, as model.wv
vector = model.wv['computer']  # get numpy vector of a word
sims = model.wv.most_similar('computer', topn=10)  # get other similar words
print(sims)



