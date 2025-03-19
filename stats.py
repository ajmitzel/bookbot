def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    counts = {}

    for character in text:
        char = character.lower()
        if char in counts:
            counts[char] = counts[char] + 1
        else:
             counts[char] = 1
    return counts

def get_sorted_character_count(counts):
    return sorted(counts.items(), key = lambda count: count[1], reverse = True)