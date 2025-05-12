def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def get_chars_dict(text):
    chars = {}
    for c in text.lower():
        if c not in chars:
            chars[c] = 0
        chars[c] += 1
    return(chars)