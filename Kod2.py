import random
import tkinter as tk

def open_file(input_file):
    with open(input_file, 'r') as input_file_data:

        input_str = input_file_data.read()

    eight_bit_strs = [bin(ord(char))[2:].zfill(8) for char in input_str]

    return eight_bit_strs

def generate_random_binary(length):

    random_binary = ''.join(random.choice('01') for _ in range(length))
    return random_binary

#генератор словаря
def process_input_array(input_array, new_length):

    unique_numbers = {}
    result_array = []
    for binary_number in input_array:
        if binary_number not in unique_numbers:
            while True:
                
                generate_random_bin = generate_random_binary(new_length)
                if generate_random_bin not in list(unique_numbers.values()):
                    unique_numbers[binary_number] = generate_random_bin
                    result_array.append((binary_number, unique_numbers[binary_number]))
                    break

    return unique_numbers
#Кодируем файл
def out(input_array, result):
    result_array2 = []
    for binary_number in input_array:
        result_array2.append (result[binary_number])
    return result_array2

# разбиваем по 8 символов
def split_string(input_string):

    substrings = [input_string[i:i+8] for i in range(0, len(input_string), 8)]


    if len(substrings[-1]) < 8:
        substrings[-1] = substrings[-1].ljust(8, '0')

    return substrings

def write_binary_txt(bin_binary_data, out_file):

    with open(out_file, 'w', encoding='utf-8') as file:
        for data in bin_binary_data:

            ascii_character = chr(int(data, 2))

            file.write(ascii_character)

def compression_ratio(input_array, out_array ):
    return ((len(input_array)*8)/(len(out_array)*8))
def main(new_length, input_file, out_file, dictionary_file):

    input_array = open_file(input_file)

    if 2**new_length < len(input_array):
        print("Символов больше чем можно закодировать ", new_length ," бит(ами).")
        return 0 
    result = process_input_array(input_array, new_length)
    print("Словарь:")
    print(result)
    with open(dictionary_file, 'w') as file:
        file.write(str(result))
    #print("///////////////")
    print("Начальный файл:")
    print(input_array)
    
    out_array = out(input_array, result)
    print("Закодированный файл:")
    print(out_array)

    #разбиваем строку по 8 бит
    str_binary_data = ""
    for binary_data in out_array:
        str_binary_data += str(binary_data) 
    bin_binary_data = split_string(str_binary_data)
    print("Выходной файл:")
    print(bin_binary_data)
    write_binary_txt(bin_binary_data, out_file)
    print("Коэффициент сжатия: ", compression_ratio(input_array, bin_binary_data))
    print("Ok")
    return compression_ratio(input_array, bin_binary_data)


def on_button_click():
    new_length1 = int(new_length.get())
    input_file1 = input_file.get()
    out_file1 = out_file.get()
    dictionary_file1 = dictionary_file.get()
    
    input_text = main(new_length1, input_file1, out_file1, dictionary_file1)
    result_label.config(text=input_text)

root = tk.Tk()
root.title("Кодировщик")

# создаем  поля ввода
input_file = tk.Entry(root, width=100)
out_file = tk.Entry(root, width=100)
dictionary_file = tk.Entry(root, width=100)
new_length = tk.Entry(root, width=100)

#кнопка
button = tk.Button(root, text="Запустить", command=on_button_click)

result_label2 = tk.Label(root, text="Исходный файл:")
result_label3 = tk.Label(root, text="Выходной файл:")
result_label4 = tk.Label(root, text="Словарь:")
result_label5 = tk.Label(root, text="Число бит:")
result_label1 = tk.Label(root, text="Коэффициент сжатия: ")
#метка для вывода
result_label = tk.Label(root, text=" ")

#размещение в окне
result_label2.pack(pady=5)
input_file.pack(pady=5)
result_label3.pack(pady=5)
out_file.pack(pady=5)
result_label4.pack(pady=5)
dictionary_file.pack(pady=5)
result_label5.pack(pady=5)
new_length.pack(pady=5)
button.pack(pady=10)
result_label1.pack(pady=5)
result_label.pack(pady=10)

root.mainloop()
'''
new_length = 4
input_file = '1.txt'
out_file = '2.txt'
dictionary_file = '3.txt' 
main(new_length, input_file, out_file, dictionary_file)
'''

