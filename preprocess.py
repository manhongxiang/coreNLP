import pandas as pd
from define import *
import os

VECTOR_SIZE = 100

#----------------------dependency matrix--------------------
def dependency_matrix(nlp, sentence):
    words = list(map(lambda x: x.lower(), nlp.word_tokenize(sentence)))
    words.insert(0, '$$$')  #表示root
    dependicies = nlp.dependency_parse(sentence)
    # print(dependicies)

    dep_matrix = pd.DataFrame(0, index=range(len(words)), columns=range(len(words)))
    for dep_type, source, target in dependicies:
        dep_matrix.iloc[source, target] = dep_type

    return words, dep_matrix

def matrix_0_1(matrix_raw):
    return matrix_raw.applymap(lambda x : 1 if x != 0 else 0)

def matrix_index(matrix_raw):
    return matrix_raw.applymap(lambda x: depType_index.get(x, -1) if x != 0 else 0)

#----------------------glove operations--------------------
from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

def glove_to_word2vec(glove_file, word2vec_file):
    '''给定glove模型的txt文件，返回用gensium加载的word2vec模型'''
    if not os.path.exists(word2vec_file):
        glove_file = datapath(glove_file)
        word2vec_file = get_tmpfile(word2vec_file)
        glove2word2vec(glove_file, word2vec_file)
    else:   #若已生成word2ve模型文件，则不需要再次生成
        word2vec_file = get_tmpfile(word2vec_file)

    model = KeyedVectors.load_word2vec_format(word2vec_file)
    return model

def build_vector_matrix(model, words, matrix):
    result = pd.DataFrame(0, index=range(len(words)), columns=range(VECTOR_SIZE))
    for i, word in enumerate(words):
        if i == 0:  # 跳过第一个符号词
            continue
        result.loc[i] = model[word]
    print("result.shape:", result.shape)
    print("matrix.shape:", matrix.shape)
    result = result.join(matrix, rsuffix="_dep")
    print("after joining:", result.shape)

    return result