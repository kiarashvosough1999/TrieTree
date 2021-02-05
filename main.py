# !/usr/bin/env python3
from Trie import Trie


def instruction():
    print("enter 0 to input text")
    print("enter 1 after you entered your text to search a word inside it")


def start_menu():
    trie = None
    while True:
        instruction()
        _input = input("Enter your option:\n")
        val = int(_input)
        if val == 0:
            del trie
            trie = Trie()
            trie.from_input()  # user input text in prompt
        elif val == 2:
            if not trie:
                print("no text input")
            else:
                trie.search_from_input()  # search


if __name__ == '__main__':
    start_menu()
