""
This file is check words

Create by: Voskanyan Feliks

Date: 21.06.2024
"""

import argparse
import re
import enchant
import os
def get_arguments():
    """
    Function: get_arguments
    Brief: The function is get 2 argument, filename for
           read text, output file for read
    Params: filename`name of file with text,
            output file `name of file for write correct text
    Return: filename, output filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True,
                        help="This is a input file name with text")
    parser.add_argument('-o', '--output', required=True,
                        help="Please input file for finish text")
    args = parser.parse_args()
    filename = args.file
    output_file = args.output
    return filename, output_file

def open_file(filename):
    """
    Function: open_file
    Brief: The function is open file and read text
    Params: filename`name of file with text
    Return: list of lines with words
    """
    if os.path.exists(filename):
        with open(filename, encoding='utf-8') as ffile:
            list_lines = ffile.readlines()
        return list_lines
    return

def check_words(content):
    """
    Function: check_words
    Brief: The function is check every word and if word not
           correct, user input word and in text change
    Params: content `list of lines with words
    Return: list of lines with correct words
    """
    try:
        dicnary = enchant.Dict("en_US")
        updated_lines = []

        for line in content:
            words = re.findall(r'\b\w+\b', line)
            corrected_line = line
            for word in words:
                if not dicnary.check(word):
                    print(f"The wrong word: {word}")
                    suggestions = dicnary.suggest(word)
                    suggestions_str = ", ".join(suggestions[:5])
                    print(f"Choose the right word for '{word}': {suggestions_str}")
                    while True:
                        new_word = input().strip()
                        if new_word in suggestions:
                            corrected_line = re.sub(r'\b{}\b'.format(re.escape(word)), new_word, corrected_line)
                            break
                        else:
                            print(f"Please choose a word from the suggestions: {suggestions_str}")
            updated_lines.append(corrected_line)

        return updated_lines

    except Exception as error:
        print(error)

def write_in_file(filename, content):
    """
    Function: write_in_file
    Brief: The function is open file and write correct text
    Params: output file for new text, content `with new correct words
    Return: None
    """
    if os.path.exists(filename):
        with open(filename, "w", encoding='utf-8') as ffile:
            for line in content:
                ffile.write(line)
    else:
        print("File not found")
def main():
    """
    Function: main
    """
    try:
        filename, output_file = get_arguments()
        content = open_file(filename)
        cnt = check_words(content)
        write_in_file(output_file, cnt)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()

