import numpy as np

from compression.huffman import huffman


def chunk_text(text, size):
    mod = len(text) % size == 0
    text = text + '0' * (size - mod)
    return [text[i * size:(i + 1) * size] for i in range(int(len(text) / size))]


def decode_chunks(code, text):
    keys = list(code.keys())
    c_size = len(keys[0])
    assert all(len(x) == c_size for x in keys)

    chunks = chunk_text(text, size=c_size)
    return ''.join([code[c] for c in chunks])


def binary_combinations(size):
    res = ['0', '1']
    for _ in range(size - 1):
        res = ['0' + i for i in res] + ['1' + i for i in res]
    return res


def combinations(size, num_ones):
    C = binary_combinations(size)
    return [c for c in C if c.count('1') == num_ones]


def distribution(size, num_ones=1):
    keys = ['0' * size]
    ps = [0.99 ** size]

    for num in range(num_ones + 1):

        C = combinations(size, num)

        for c in C:
            keys.append(c)
            ps.append(0.99 ** (size - num) * 0.01 ** num)

    CC = {k: p for k, p in zip(keys, ps)}
    total = sum(CC.values())
    res = {c: CC[c] / total for c in CC}

    return res


def encode_in_chunks(text, size, num_ones):
    d_chunks = distribution(size, num_ones=num_ones)
    code = huffman(d_chunks)
    text = decode_chunks(code, text)

    return text


def average_experiment_chunks(runs=100):
    res = []

    for _ in range(runs):
        a = np.random.choice([0, 1], 10000, p=[0.99, 0.01])
        text = ''.join([str(i) for i in a])

        text = encode_in_chunks(text, 12, num_ones=3)
        text = encode_in_chunks(text, 2, num_ones=2)

        res.append(len(text))

    return np.mean(res)


def entropy_of_binary(data):
    alphabet = "01"
    frequencies = {c: data.count(c) for c in alphabet}
    print(frequencies)
    total = sum(frequencies.values())
    return np.sum([(-frequencies[c] / total) * np.log2(frequencies[c] / total) for c in alphabet])


if __name__ == "__main__":
    f = open("../texts/random01.txt", "r")
    text = f.read()
    orig_len = len(text)
    print("Original entropy", entropy_of_binary(text))
    text = encode_in_chunks(text, 16, num_ones=3)
    text = encode_in_chunks(text, 2, num_ones=2)
    print("Compressed entropy", entropy_of_binary(text))
    encoded_len = len(text)
    print(orig_len)
    print(encoded_len)
    print(encoded_len / orig_len)

    # print(average_experiment_chunks())
