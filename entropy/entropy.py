########### YOU DO NOT HAVE TO EDIT THIS PART #########

from collections import Counter
import math
import string
import re

import numpy as np

import collections


def parse_text(input_text):
    if input_text is None:
        # open the input file, which was added as input.txt in the menu on the left.
        input_text = open("../texts/Jack.txt")
    data = input_text.read().lower()

    regex = re.compile('[^a-z ]')
    data = regex.sub('', data)

    return data


def entropy_of_text(input_text=None):
    data = parse_text(input_text)
    ## create a dictionary containing the frequencies for all characters (incl. space)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequencies = {c: data.count(c) for c in alphabet}
    total = sum(frequencies.values())

    upper_bound = np.sum([1 / 27 * np.log2(27) for c in alphabet])
    print(upper_bound)

    entropy_single = np.sum([(-frequencies[c] / total) * np.log2(frequencies[c] / total) for c in alphabet])
    print(entropy_single)


def conditional_entropy_of_text(input_text=None):
    data = parse_text(input_text)

    ## create a dictionary containing the frequencies for all characters (incl. space)
    alphabet = "abcdefghijklmnopqrstuvwxyz "

    N = len(data)
    pair_counter = collections.Counter()

    frequencies = {c: data.count(c) for c in alphabet}
    total = sum(frequencies.values())
    single_props = {c: frequencies[c] / total for c in alphabet}

    c_pairs = [(data[i], data[i + 1]) for i in range(N - 1)]

    total_counts_cond = 0
    for pair in c_pairs:
        pair_counter[pair] += 1
        total_counts_cond += 1

    cond_entropy = 0
    for y in alphabet:
        py = single_props[y]
        for x in alphabet:
            if pair_counter[(y, x)] > 0:
                cond_xy = pair_counter[(y, x)] / total_counts_cond
                _cd = cond_xy * np.log2(py / cond_xy)
                cond_entropy += _cd


def word_entropy(input_text=None):
    data = parse_text(input_text)
    print(data)
    words_text = data.split()

    word_counter = collections.Counter()

    total_counts = 0
    for word in words_text:
        word_counter[word] += 1
        total_counts += 1

    entropy_word = np.sum(
        [(-word_counter[word] / total_counts) * np.log2(word_counter[word] / total_counts) for word in word_counter])
    print(entropy_word)


def cross_entropy_letters(input_text=None):
    data = parse_text(input_text)

    ## create a dictionary containing the frequencies for all characters (incl. space)
    alphabet = "abcdefghijklmnopqrstuvwxyz "

    N = len(data)
    pair_counter = collections.Counter()

    frequencies = {c: data.count(c) for c in alphabet}
    total = sum(frequencies.values())
    single_props = np.asarray([frequencies[c] / total for c in alphabet])[:, np.newaxis]
    ind_pxy = single_props @ single_props.T

    c_pairs = [(data[i], data[i + 1]) for i in range(N - 1)]

    total_counts_cond = 0
    for pair in c_pairs:
        pair_counter[pair] += 1
        total_counts_cond += 1

    cross_entropy = 0
    for i, y in enumerate(alphabet):
        for j, x in enumerate(alphabet):
            indpxy = ind_pxy[i, j]
            if pair_counter[(y, x)] > 0:
                cond_xy = pair_counter[(y, x)] / total_counts_cond
                _cd = -cond_xy * np.log2(indpxy)
                cross_entropy += _cd

    print(cross_entropy)


if __name__ == "__main__":
    # conditional_entropy_of_text()
    cross_entropy_letters()
    # word_entropy()
