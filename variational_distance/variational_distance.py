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


def calc_variational_distance(books):
    for p in books:
        print(" ")
        for q in books:
            # Print for latex table
            print(np.round(total_variation_distance(p, q), 4), end=" ")
    print(" ")


def calc_collision_probabilities(books):
    for _p in books:
        print(np.round(collision_probability(_p), 4), end=" ")
    print(" ")


def identify_perm_cipher_lang(pc_freq_np, books):
    for _p in books:
        print(np.round(total_variation_distance(pc_freq_np, _p), 4), end=" ")
    print(" ")


if __name__ == "__main__":
    print("Order of printed probabilities:")
    print(glob.glob('../texts/Alice*.txt'))

    norm_freq_books = []
    for link in glob.glob('../texts/Alice*.txt'):
        _text = open(link)
        letter_freq_np = counter_to_numpy(lf.get_letter_freqs(_text, print_results=False, normalize=True))
        norm_freq_books.append(letter_freq_np)

    perm_cipher = open('../texts/permuted_cipher.txt')
    pc_freq_np = counter_to_numpy(lf.get_letter_freqs(perm_cipher, print_results=False, normalize=True))

    print("Total Variation Distance")
    calc_variational_distance(norm_freq_books)
    print("--" * 40)
    print("Collision Probabilities")
    calc_collision_probabilities(norm_freq_books)
    print("--" * 40)
    print("Identify Permuted Cipher")
    identify_perm_cipher_lang(pc_freq_np, norm_freq_books)
    print("--" * 40)
    print("Collision Probability Permuted Cipher")
    calc_collision_probabilities([pc_freq_np])
