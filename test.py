from preprocess import *
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP("/home/stanford-corenlp-full-2018-10-05")
try:
    s = "I'm running, and he is running, too."
    words, matrix_raw = dependency_matrix(nlp, s)
    print(matrix_raw)

    print("----------------------------------------------------")
    matrix_0_1 = matrix_0_1(matrix_raw)
    print(matrix_0_1)

    print("----------------------------------------------------")
    type_index = {v : i for i, v in enumerate(dependencies)}
    matrix_index = matrix_index(matrix_raw)
    print(matrix_index)
except Exception as e:
    print(e)
finally:
    nlp.close()

glove_model = glove_to_word2vec("/root/PycharmProjects/coreNLP/glove.6B.100d.txt", "/root/PycharmProjects/coreNLP/word2vec.txt")
matrix_total = build_vector_matrix(glove_model, words, matrix_0_1)
print(matrix_total)