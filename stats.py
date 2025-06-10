def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    characters = {}
    for char in text.lower():
        if char.isalpha() and char not in [" ", "\n"]:
            characters[char] = characters.get(char, 0) + 1
    return characters


def print_report(text, count_words, count_characters):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {text}...")
    print("----------- Word Count ------------")
    print(f"Found {count_words} total words")
    print("----------- Character Count ------------")
    for char, count in sorted(count_characters.items()):
        print(f"{char}: {count}")
    print("============= END ===============")
