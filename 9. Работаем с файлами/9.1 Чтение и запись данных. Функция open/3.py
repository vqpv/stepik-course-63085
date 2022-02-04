from string import punctuation


def longest_word_in_file(file_name):
    clean_words = []
    with open(file_name, encoding='utf-8') as f:
        text = f.read()
        words = text.split()
    for word in words:
        word = word.strip(punctuation)
        clean_words.append(word)
    return max(clean_words[::-1], key=len)
