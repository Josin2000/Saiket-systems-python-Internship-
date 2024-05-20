import re
from collections import Counter

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except IOError:
        print(f"Error: An IOError occurred while reading the file at {file_path}.")
        return None

def count_lines(text):
    return len(text.splitlines())

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words), Counter(words)

def count_characters(text):
    return len(text)

def display_results(line_count, word_count, character_count, word_frequency):
    
    print(f"Number of lines: {line_count}")
    print(f"Number of words: {word_count}")
    print(f"Number of characters: {character_count}")
    print("Word frequency:")
    for word, freq in word_frequency.most_common(10):  
        print(f"{word}: {freq}")

def main():
    file_path = 'inputtask6.txt'  
    text = read_file(file_path)
    
    if text is not None:
        line_count = count_lines(text)
        word_count, word_frequency = count_words(text)
        character_count = count_characters(text)
        
        display_results(line_count, word_count, character_count, word_frequency)

if __name__ == "__main__":
    main()
