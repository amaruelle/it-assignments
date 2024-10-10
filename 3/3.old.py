def get_repeated_words(string):
    seen_words = set()
    repeated_words = set()
    for word in split_string(string):
        if word in seen_words:
            repeated_words.add(word)
        else:
            seen_words.add(word)
    return repeated_words