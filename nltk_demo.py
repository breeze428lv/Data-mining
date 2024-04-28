from collections.abc import Mapping
import pandas as pd
import pygraphviz as pgv
import numpy as np

from stanfordcorenlp import StanfordCoreNLP
# nlp = StanfordCoreNLP(r'/mnt/f/CMBNLP/stanford-corenlp-full-2018-02-27/', lang='zh')
## 这里是coreNLP的路径，英文去掉 lang='zh'

nlp = StanfordCoreNLP(r'venv/lib/python3.8/site-packages/stanford-corenlp-full-2018-02-27/')


# from pycorenlp import StanfordCoreNLP
# from nltk.tree import Tree
# from nltk.parse.stanford import StanfordDependencyParser

# nlp = StanfordCoreNLP('http://localhost:9000')
def stanfordparserdemo(sentence):
    res = ''

    # print(nlp.word_tokenize(sentence))
    # print(nlp.pos_tag(sentence))
    # print(nlp.ner(sentence))

    txt = nlp.parse(sentence)


    lines = txt.split('\n')
    for line in lines:
        segs = line.split('(')

        line_str = segs[0]
        for seg in segs[1:]:
            blank_tag = True

            sub_segs = seg.split(' ')
            if len(sub_segs) > 1:
                line_str += sub_segs[1].replace(')', '') + ' '
                if blank_tag:
                    blank_tag = False

        if not blank_tag:
            res += line_str + '\n'

    print(res)


if __name__ == "__main__":
    # stanfordparserdemo('The boy put tortoise on the rug.')
    stanfordparserdemo('The boy with whom I am playing basketball thinks that he likes the red rug which looks so beautiful.')
    # NLTKparserfordependancies('The boy put tortoise on the rug.')

