# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('words.txt', 'r') as fin:
    for line in fin:
        words = line.split()
        for word in words:
            if "abc" in word:
                words.remove(word)
        sentense = " ".join(words)
        print(sentense)


# name_file = 'hw0501.txt'
# name_file2 = 'hw0502.txt'
# string_input = 'Сижу за решеткой в абв темнице сырой, скормленный в абв неволе абвер орел молодой'
# function.write_file(string_input, name_file)
# string_output = function.read_file(name_file)
# string_output = list(filter(lambda x: not 'абв' in x, string_output.split()))
# string_output = ' '.join(string_output)
# function.write_file(string_output, name_file2)
