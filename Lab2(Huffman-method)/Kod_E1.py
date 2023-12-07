import matplotlib.pyplot as plt
import numpy as np
import heapq
from collections import defaultdict

def calculate_entropy(data):
    probabilities = [data.count(symbol) / len(data) for symbol in set(data)]
    entropy = -sum(p * np.log2(p) for p in probabilities)
    return entropy

def build_huffman_tree(data,lenS ):
    frequencies = defaultdict(int)
    for symbol in data:
        frequencies[symbol] += 1

    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    for i in range(lenS ):
        while len(heap[0][1][1]) < 8:
            heap[0][1][1] += '0'
       
    print(heapq[0][1][1])

    return heap[0][1:]

def huffman_compress(data, huffman_tree):
    encoding_dict = dict(huffman_tree)
    encoded_data = ''.join(encoding_dict[symbol] for symbol in data)
    return encoded_data

def calculate_compression_ratio(original_size, compressed_size):
    return original_size / compressed_size

def split_string(input_string):

    substrings = [input_string[i:i+8] for i in range(0, len(input_string), 8)]


    if len(substrings[-1]) < 8:
        substrings[-1] = substrings[-1].ljust(8, '0')
    return substrings


def split_stringG(input_string,new_length2):

    substrings = [input_string[i:i+new_length2] for i in range(0, len(input_string), new_length2)]


    if len(substrings[-1]) < new_length2:
        substrings[-1] = substrings[-1].ljust(new_length2, '0')

    return substrings
#data = "abracadabra"

input_file = '1.txt'
with open(input_file, 'r') as input_file_data:

    data = input_file_data.read()
eight_bit_strs = [bin(ord(char))[2:].zfill(8) for char in data]


new_length2 = 3

input_arrayG = ""
for i in eight_bit_strs:
    input_arrayG += i
input_arrayK = split_stringG(input_arrayG,new_length2)
print(input_arrayK)
lenS = len(data)
# энтропию Шеннона'''
shannon_entropy = calculate_entropy(data)

# дерево Хаффмана
huffman_tree = build_huffman_tree(data,lenS )
print(huffman_tree)
# Кодируем данные Хаффманом
compressed_data = huffman_compress(data, huffman_tree)

# Рассчитываем энтропию Б
b_entropy = calculate_entropy(compressed_data)

# Рассчитываем коэффициент сжатия
compression_ratio = calculate_compression_ratio(len(data) * 8, len(compressed_data))
print(split_string(compressed_data))
out_file ='2.txt'

bin_binary_data = split_string(compressed_data)

with open(out_file, 'w', encoding='utf-8') as file:
    for data in bin_binary_data:

        ascii_character = chr(int(data, 2))

        file.write(ascii_character)
    
''''
# Строим графики
plt.figure(figsize=(10, 6))

# График энтропии Шеннона и Б
plt.subplot(2, 1, 1)
plt.bar(["Shannon Entropy", "B Entropy"], [shannon_entropy, b_entropy])
plt.title("Shannon and B Entropy")

# График коэффициента сжатия
plt.subplot(2, 1, 2)
plt.bar(["Compression Ratio"], [compression_ratio])
plt.title("Compression Ratio")

plt.tight_layout()
plt.show()
'''
