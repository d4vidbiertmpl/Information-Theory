import numpy as np
import glob

from letter_frequencies import letter_freqs as lf


def counter_to_numpy(counter):
    counter_np = np.zeros(len(counter))
    for i, uni_c in enumerate(np.arange(ord('a'), ord('z') + 1)):
        key = chr(uni_c)
        counter_np[i] = counter[key]
    return counter_np


def total_variation_distance(P, Q):
    return 0.5 * np.sum(np.absolute(P - Q))


def collision_probability(P):
    return np.sum(np.square(P))


if __name__ == "__main__":
    books = []
    for link in glob.glob('../texts/Alice*.txt'):
        _text = open(link)
        letter_freq_np = counter_to_numpy(lf.get_letter_freqs(_text, print_results=False, normalize=True))
        books.append(letter_freq_np)

    # for p in books:
    #     print("New Book")
    #     for q in books:
    #         print(total_variation_distance(p, q))

    # for p in books:
    #     print(collision_probability(p))

    perm_cipher = open('../texts/permuted_cipher.txt')
    pc_freq_np = counter_to_numpy(lf.get_letter_freqs(perm_cipher, print_results=False, normalize=True))
    for q in books:
        print(total_variation_distance(pc_freq_np, q))


