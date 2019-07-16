# stanfordcorenlp 所有依存关系列表
dependencies = [
    "acomp", "advcl", "advmod", "agent", "amod",
    "appos", "aux", "auxpass", "cc", "ccomp",
    "conj", "cop", "csubj", "csubjpass", "dep",
    "det", "discourse", "dobj", "expl", "goeswith",
    "iobj", "mark", "mwe", "neg", "nn", "npadvmod",
    "nsubj", "nsubjpass", "num", "number", "parataxis",
    "pcomp", "pobj", "poss", "possessive", "preconj",
    "predet", "prep", "prepc", "prt", "punct",
    "quantmod", "rcmod", "ref", "ROOT", "tmod",
    "vmod", "xcomp", "xsubj"
]

depType_index = {v: i for i, v in enumerate(dependencies)}