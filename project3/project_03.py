# Author: <Andri Benedikt>
# Date: <04-04-2024>
# Project: <project_03>
# Acknowledgements: <autopep8>

# Næ í öll orðin úr csv skránni í lista
def get_words():
    all_words = []
    gogn = open('BIN_ordalisti.csv', 'r', encoding='UTF-8', newline='')
    for line in gogn:
        all_words.append(line.split(";")[0])
    gogn.close()
    return (all_words)


# Athuga hvort orðið passi við mynstrið
def word_matches_pattern(word, pattern):
    if len(word) != len(pattern) and pattern[-1] != "*" or len(word) < len(pattern)-1:
        return False
    elif pattern[-1] == "*":
        for location in range(len(pattern)-1):
            if word[location] != pattern[location] and pattern[location] != "_":

                return False
    else:
        for location in range(len(word)):
            if word[location] != pattern[location] and pattern[location] != "_":

                return False
    return True

# Athuga hvort orðið passi við stafina
def word_matches_letters(word, input_letters):
    letter_list = []
    for letter_add in input_letters:
        letter_list.append(letter_add)

    if len(input_letters) >= len(word):
        testcase = ""
        for word_letter in word:
            for letter in letter_list:
                if letter == word_letter:
                    testcase = testcase+letter
                    letter_list.remove(letter)
                    break
        if testcase == word:
            return True
        else:
            return False
    return False

# Fer í gegnum öll orð og athuga hvort þau passi við mynstur, stafi eða bæði
def get_match_list(letters, pattern):
    match_list = []
    words = get_words()
    last_word = ""
    for test_word in words:
        test_word = test_word.upper()
        if len(letters) == 0 and len(pattern) > 0:
            if word_matches_pattern(test_word, pattern) and test_word != last_word:
                match_list.append(test_word)
                last_word = test_word
        elif len(pattern) == 0 and len(letters) > 0:
            if word_matches_letters(test_word, letters) and test_word != last_word:
                match_list.append(test_word)
                last_word = test_word
        else:
            if word_matches_letters(test_word, letters) and word_matches_pattern(test_word, pattern) and test_word != last_word:
                match_list.append(test_word)
                last_word = test_word
    return match_list

# Athuga hvort að stafirnir sem eru settir inn séu leyfilegir
def allowed_letters(letters):
    return letters.isalpha()

# Athuga hvort að mynstrið sem er sett inn sé leyfilegt
def allowed_patterns(pattern):
    counter = 0
    for x in pattern:
        counter += 1
        if counter != len(pattern):
            if x.isalpha() == False and x != "_":
                return False
        else:
            if x.isalpha() == False and x != "_" and x != "*":
                return False
    return True

# Athuga hvort að það stafirnir og mynstrið virki saman
def letter_pattern_check(letters, pattern):
    for letter in pattern:
        if letter not in letters and letter != "_" and letter != "*":
            return False
    return True


# Valmynd 
test_pattern = ""
test_letters = ""
print("---------- Scrabble solver ----------")
while True:
    if len(test_letters) != 0 and len(test_pattern) != 0:
        if letter_pattern_check(test_letters, test_pattern) == False:
            print("Warning: The pattern does not match the letters!")
    print()
    if len(test_letters) != 0:
        print("Current letters: ", test_letters)
    if len(test_pattern) != 0:
        print("Current pattern: ", test_pattern)
    print("1: Define letters")
    print("2: Define pattern")
    print("3: Find match")
    print("4: Quit")
    selection = input("Selection: ")

    if selection == "1":
        # Tek inn stafi frá notanda
        while True:
            input_letters = input("Letters: ").upper()
            if allowed_letters(input_letters):
                test_letters = input_letters
                break
            else:
                print("Sorry, try again, this contained letters that are not allowed")

    elif selection == "2":
        # Tek inn mynstur frá notanda
        while True:
            input_pattern = input("Pattern: ").upper()
            if allowed_patterns(input_pattern):
                test_pattern = input_pattern
                break
            else:
                print("Sorry, try again, this pattern is not allowed")

    elif selection == "3":
        # prenta út orðin í stærðarröð
        matches = get_match_list(test_letters, test_pattern)
        matches.sort(key=len)
        if len(matches) == 0:
            print("Sorry, no matches found")
        for x in matches:
            if x == matches[-1]:
                print(x)
            else:
                print(x, end=", ")

    elif selection == "4":
        break
    else:
        print("Unknown selection, please try again")
