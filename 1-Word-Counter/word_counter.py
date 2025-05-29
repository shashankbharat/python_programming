#!/usr/bin/python3
"""
Input:           A sentence from the user
Output:          Summary of words in the sentence- longest, shortest, frequency by length
Author:          Shashank Sharma
"""
import sys

def get_length(word_tuple):
    return word_tuple[1]

def show_words_summary(sentence):
    # Put the words into a list using split() - default separator is whitespace
    word_list = sentence.split()

    # List comprehension: (word, length)
    word_list = [(word, len(word)) for word in word_list]

    print("Unsorted word list as tuples of (word, word_length)")
    print(str(word_list))

    # Sorted by word length
    word_list.sort(key=get_length)
    print("\n-- Using list sort() to order the list by word length --\n")
    print(str(word_list))

    # Unique words only
    unique_words = list(set(word_list))
    unique_words.sort(key=get_length)
    print("\n-- Using set() to remove duplicates --\n")
    print(str(unique_words))

    # Count of words by length
    word_counts = {}
    for (word, word_length) in word_list:
        if word_length not in word_counts:
            word_counts[word_length] = 1
        else:
            word_counts[word_length] += 1
    print("\nWord_Length Number_of_words")
    print("-----------  ---------------")
    for (num_chars, num_words) in sorted(word_counts.items()):
        print(f"   {num_chars:<11}   {num_words}")

def get_and_verify__sentence():
    # Prompt user to enter a sentence
    sentence = input("\nPlease enter a sentence (words separated by spaces): ")
    if (len(sentence) == 0):
        print("No characters entered!")
        sys.exit(0)
    elif (" " not in sentence):
        print("Only one word entered!")
        sys.exitexit(0)
    else:
        return sentence


if __name__ == "__main__":
    sentence = get_and_verify__sentence()
    show_words_summary(sentence)