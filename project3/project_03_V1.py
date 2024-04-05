# Author: <Andri Benedikt>
# Date: <27-03-2024>
# Project: <project_03>
# Acknowledgements: <>

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



def get_words():
    all_words = []
    gogn = open('BIN_ordalisti.csv', 'r',encoding='UTF-8',newline='')
    for line in gogn:
        all_words.append(line.split(";")[0])
    gogn.close()
    return(all_words)

def find_matching_words(pattern, word_list, available_letters):
    if pattern == "":
        letter_counts = {}
        for letter in letters:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

        matching_words = []
        for word in word_list:
            temp_counts = letter_counts.copy()  # Make a copy of letter counts for each word
            valid = True
            for letter in word:
                if letter in temp_counts and temp_counts[letter] > 0:
                    temp_counts[letter] -= 1
                else:
                    valid = False
                    break
            if valid:
                matching_words.append(word)
    else:
        matching_words = []
        
        use_all_letters = len(available_letters) == 0
        
        available_letter_counts = {}
        if not use_all_letters:
            for letter in available_letters:
                available_letter_counts[letter] = available_letter_counts.get(letter, 0) + 1

        any_length = pattern.endswith('*')
        if any_length:
            pattern = pattern[:-1] 

        for word in word_list:
            if not any_length and len(word) != len(pattern):
                continue
            if any_length and len(word) < len(pattern):
                continue

            match = True
            if not use_all_letters:
                word_counts = {}
                for letter in word:
                    word_counts[letter] = word_counts.get(letter, 0) + 1

                for letter, count in word_counts.items():
                    if available_letter_counts.get(letter, 0) < count:
                        match = False
                        break

            for i in range(min(len(pattern), len(word))):
                if pattern[i] != "_" and pattern[i] != word[i]:
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
    for x in pattern:
        if x not in available_letters and x != "_" and x != "*":
            print("Warning: The pattern does not match the letters!")
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
        pattern = ""
        while len(pattern) == 0:
            input_pattern = input("Pattern: ")
            if pattern_check(input_pattern):
                pattern = input_pattern
            else:
                print("Sorry, try again, this pattern is not allowed")

    elif selection == "3":
        matching_words = find_matching_words(pattern, words, available_letters)
        last_word = ""
        if len(matching_words) == 0:
            print("Sorry, no matches found")
        for word in sorted(matching_words,key=len):
            if word == last_word:
                continue
            else:
                last_word = word
                if word == sorted(matching_words,key=len)[-1]:
                    print(word.upper())
                else:
                    print(word.upper(),end=", ")
    elif selection == "4":
        break
    else:
        print("Unknown selection, please try again")