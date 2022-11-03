# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_in.txt', 'w+') as data:
    print('Введите строку из нескольких прозвольное количество раз повторяющихся букв, например DDDDjjjjjjjjjjjjKLLLLLL,')
    string = input('я сделаю RLE сжатие строки и ее восстановление в отдельные файлы:\n')
    data.write(string)

def compressing(string):
    compr_string = ''
    count = 1
    char = string[0]
    for i in range(1, len(string)):
        if string[i] == char:
            count += 1
        else:
            compr_string = compr_string + str(count) + char
            char = string[i]
            count = 1
    compr_string = compr_string + str(count) + char
    return compr_string

def decompressing(out_string):
    decompr_string = ''
    char_amount = 0
    for i in range(len(out_string)):
        if out_string[i].isdigit():
            char_amount += int(out_string[i])
            if out_string[i].isdigit() and out_string[i-1].isdigit():
                char_amount += (int(out_string[i-1])*10 - int(out_string[i-1]))
        else:
            decompr_string += out_string[i] * char_amount
            char_amount = 0
    return decompr_string

with open('file_compr.txt', 'w') as file1:
    compr_string = compressing(string)
    file1.write(compr_string)
    print(f'Сжатая строка:\t{compr_string} записана в файл file_compr.txt')

with open('file_compr.txt', 'r') as file1:
    out_string = file1.read()

with open('file_decompr.txt', 'w') as file2:
    decompr_string = decompressing(out_string)
    file2.write(decompr_string)
    print(f'Восстановленная строка:\t{decompr_string} записана в файл file_decompr.txt')



