# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def write_file(line:str, name:str):
    '''
    Запись строк в файл
    '''
    with open(name, 'w', encoding = 'utf-8') as f:
        f.write(line)

def read_file(name:str):#не дописано
    
    





def get_encode(s):
    encoding = ''
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count +=1
            i+=1
        encoding += str(count) + s[i]
        i +=1
    return encoding

def get_decode(s):
    decoding = ''
    i=0
    while i < len(s):
        num = ''
        while i+1 < len(s) and s[i].isdigit == True:
            num += s[i]
            i +=1
        decoding += int(num)*s[i]
        num = ''
        i += 1
    return decoding

file_name = 'filetask05041.txt'
string_input = read_file(file_name) 
file_name_encode = 'filetask05052.txt'
string_input_encode = get_encode(string_input)
write_file(string_input_encode, file_name_encode)
string_output = read_file(file_name_encode)
string_output_decode = get_decode(string_output)
print(string_output_decode)



