import os

# Написать программу для извлечения повторяющихся слов из одного файла и записи их в другой текстовый файл.

def split_string(string):
    word = ""
    for char in string:
        if char == " " or char == "\t":
            yield word
            word = ""
        else:
            word += char
    yield word

def join_string(words):
    string = ""
    for word in words:
        string += word + " "
    return string[:-1]

def get_repeated_words(string):
    def is_word_repeated(word, string):
        count = 0
        for w in split_string(string):
            if w == word:
                count += 1
            if count > 1:
                return True
        return False

    repeated_words = ""
    for word in split_string(string):
        if is_word_repeated(word, string) and word not in repeated_words:
            repeated_words += word + " "
    return repeated_words[:-1]

def get_repeated_words_from_file(file_name):
    with open(file_name, "r") as file:
        string = file.read()
    repeated_words = get_repeated_words(string)
    if repeated_words:
        with open("repeated_words.txt", "w") as file:
            file.write(repeated_words)
    else:
        print("Повторяющихся слов нет.")

file_name = input("Введите имя файла: ")
relative_path = os.path.join(os.path.dirname(__file__), file_name)
get_repeated_words_from_file(relative_path)