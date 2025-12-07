def get_number_of_words(word: str):
    words_arr = word.split()
    return len(words_arr)

def get_number_of_times_char_appear(word: str):
    lower_word = word.lower()
    split_word = lower_word.split()
    result = {}

    for word in split_word:
        split_w = list(word)
        for w in split_w:
            is_exist:bool = result.get(w)
            if is_exist:
                result[w] += 1
            else:
                result.update({w: 1})

    return result

def sorted_dict(item_dict: dict):
    result = []
    
    for c, n in item_dict.items():
        new_dict:dict = {"char": c, "num": n}
        result.append(new_dict)

    result.sort(reverse=True, key=lambda k: k["num"])
    return result