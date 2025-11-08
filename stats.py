def get_number_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    character_count = {}
    for line in file_contents:
        for character in line:
            ch = character.lower()
            if ch in character_count:
                character_count[ch] += 1
            else:
                character_count[ch] = 1
    return character_count

def sort_on(items):
    return items["num"]

def get_sorted_list_dictionary(char_dictionary):
    the_list = []
    for ch, count in char_dictionary.items():
        the_list.append({"char": ch, "num": count})
    the_list.sort(reverse=True, key=sort_on)
    return the_list

