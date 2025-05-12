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

def sort_on(dict):
    return dict["num"]

def get_sorted_chars_list(text):
    chars = get_chars_dict(text)
    chars_list = []
    for char, num in chars.items():
        if char.isalpha():
            chars_list.append({"char":char, "num":num})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list