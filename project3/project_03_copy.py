# Author: <Andri Benedikt>
# Date: <27-03-2024>
# Project: <project_03>
# Acknowledgements: <>



def get_words():
    all_words = []
    gogn = open('BIN_ordalisti.csv', 'r',encoding='UTF-8',newline='')
    for line in gogn:
        all_words.append(line.split(";")[0])
    gogn.close()
    return(all_words)

def pattern_check(input_string):
    if not input_string:
        return False
    
    end_index = len(input_string)
    last_char_is_asterisk = input_string[-1] == "*"
    if last_char_is_asterisk:
        end_index -= 1  

    for i in range(end_index):
        char = input_string[i]
        if not char.isalpha() and char != "_":
            return False

    return True

def find_matching_words(pattern, word_list, available_letters):
    matching_words = []
    use_all_letters = len(available_letters) == 0
    any_length = pattern.endswith('*') or pattern == "" 


    available_letter_counts = {}
    for letter in available_letters:
        available_letter_counts[letter] = available_letter_counts.get(letter, 0) + 1

    for word in word_list:
        if not any_length and len(word) != len(pattern):
            continue
        if any_length and pattern and len(word) < len(pattern) - 1:
            continue

        word_counts = {letter: word.count(letter) for letter in set(word)}
        
        if use_all_letters or pattern == "" or pattern.endswith('*'):
            if all(available_letter_counts.get(letter, 0) >= count for letter, count in word_counts.items()):
                matching_words.append(word)
        else:

            match = True
            for i in range(min(len(pattern), len(word))):
                pat_char, word_char = pattern[i], word[i]
                if pat_char != "_" and pat_char != word_char:
                    match = False
                    break
                if pat_char == "_" and available_letter_counts.get(word_char, 0) < word_counts[word_char]:
                    match = False
                    break
            if match:
                matching_words.append(word)

    return matching_words





pattern = ""
available_letters = "" 
words = get_words()
print("---------- Scrabble solver ----------")
while True:
    stop = False
    for x in pattern:
        if x not in available_letters and x != "_" and x != "*":
            print("Warning: The pattern does not match the letters!")
            stop = True
            break
    print()

    if len(available_letters) >0:
        print("Current letters: ",available_letters.upper())
    if len(pattern) >0:
        print("Current pattern: ",pattern.upper())
    print("1: Define letters")
    print("2: Define pattern")
    print("3: Find match")
    print("4: Quit")
    selection = input("Selection: ")

    if selection == "1":
        while len(available_letters) ==0:
            letters = input("Letters: ")
            if letters.isalpha():
                available_letters = letters
            else:
                print("Sorry, try again, this contained letters that are not allowed")

    elif selection == "2":
        while len(pattern) == 0:
            input_pattern = input("Pattern: ")
            if pattern_check(input_pattern):
                pattern = input_pattern
            else:
                print("Sorry, try again, this pattern is not allowed")

    elif selection == "3":
        matching_words = find_matching_words(pattern, words, available_letters)
        last_word = ""
        if stop:
            print("Sorry, no matches found")
            continue
        for word in sorted(matching_words, key=len):
            if word == last_word:
                continue
            else:
                last_word = word
                if word == sorted(matching_words, key=len)[-1]:
                    print(word.upper())
                else:
                    print(word.upper(),end=", ")
    elif selection == "4":
        break
    else:
        print("Unknown selection, please try again")