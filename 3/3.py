# 7. Ввести строку, выяснить, нет ли повторяющихся слов, и вывести их, если они есть. Можно считать, что все слова имеют длину ровно 3 символа.
default_string = "cat dog cat dog cat dog fat full feed fina fina"
default_string_tab = "cat\tdog\tcat\tdog\tcat\tdog\tfat\tfull\tfeed\tfina\tfina"

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

string = input("Введите строку: ") or default_string_tab
repeated_words = get_repeated_words(string)
if repeated_words:
    print("Повторяющиеся слова:", repeated_words)
else:
    print("Повторяющихся слов нет.")