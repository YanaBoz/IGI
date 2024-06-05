# Program: Text analysis(4 task)
# Lab: Lab 1
# Version: 1.0
# Bozhko Yana
# 02.05.2024

def count_lowercase_letters(string):
    count = 0
    for char in string:
        if char.islower():
            count += 1

    return count


def find_first_word_with_letter(string, letter):
    words = string.split()
    for i, word in enumerate(words):
        if letter in word:
            return word, i

    return None, -1


def remove_words_starting_with(string, letter):
    words = string.split()
    filtered_words = []
    for word in words:
        if not word.startswith(letter):
            filtered_words.append(word)

    return " ".join(filtered_words)


def task4():
    string = input("x: ")

    # �)
    lowercase_count = count_lowercase_letters(string)
    print(f"lowercase: {lowercase_count}")

    # �)
    first_word_with_v, index = find_first_word_with_letter(string, 'v')
    if first_word_with_v is None:
        print("no'v'.")
    else:
        print(f"first word 'v': '{first_word_with_v}', number: {index+1}")

    # �)
    filtered_string = remove_words_starting_with(string, 's')
    print(f"without 's': '{filtered_string}'")


if __name__ == "__main__":
    task4()

