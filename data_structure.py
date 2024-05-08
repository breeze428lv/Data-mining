# version 1.04
import random
from collections.abc import Mapping
import pandas as pd
# import pygraphviz as pgv
import numpy as np
import csv
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

from collections import Counter
from collections import namedtuple
from dataclasses import dataclass
import matplotlib.pyplot as plt
# from scratch.probability import inverse_normal_cdf
from scratch import*
from typing import List, Dict, NamedTuple, Optional
import datetime
from dateutil.parser import parse

class TreeNode(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def insert(self, root, node):
        if root is None:
            return node
        if node.data < root.data:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)
            return root

    def mid_order(self, root):
        node = root
        stack = []
        res = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.data)
            node = node.right
        return res


def f20240508a():
    data = [5, 1, 2, 3, 6, 8, 9]
    root = TreeNode(data[0])
    tree = BinaryTree()
    for i in data[1:]:
        tree.insert(root, TreeNode(i))

    print(tree.mid_order(root))

if __name__ == "__main__":
    f20240508a()