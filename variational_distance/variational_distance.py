import numpy as np
import glob

from letter_frequencies import letter_freqs as lf


def total_variation_distance():
    pass


if __name__ == "__main__":
    books = []
    for link in glob.glob('../texts/Alice*.txt')
        _text = open(link)
        books.append(lf.get_letter_freqs(_text, False))


    for book in books:
        total_variation_distance()


