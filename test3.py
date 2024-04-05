def find_matching_words(pattern, word_list, available_letters):
    matching_words = []
    
    # Determine if available letters are specified
    use_all_letters = len(available_letters) == 0
    
    # Adjust pattern for any_length matching and prepare for no pattern specified
    any_length = pattern.endswith('*')
    if any_length:
        pattern = pattern[:-1]  # Remove the '*' for matching
    use_any_pattern = len(pattern.strip('_')) == 0
    
    # Count occurrences of each letter in available_letters
    available_letter_counts = {}
    if not use_all_letters:
        for letter in available_letters:
            available_letter_counts[letter] = available_letter_counts.get(letter, 0) + 1

    for word in word_list:
        if use_any_pattern and len(word) != len(pattern) and not any_length:
            continue
        
        match = True
        word_counts = {}
        for letter in word:
            word_counts[letter] = word_counts.get(letter, 0) + 1
        
        if not use_all_letters:
            # Check if word can be formed with available_letters
            for letter, count in word_counts.items():
                if letter not in available_letter_counts or available_letter_counts[letter] < count:
                    match = False
                    break

        if match:
            matching_words.append(word)

    return matching_words

# Example usage
word_list = ["apple", "apply", "apace", "bat", "ball", "cat", "application", "applied", "mabba"]  # Extended word list
pattern = "_____"  # Pattern indicating any 5-letter word
available_letters = "aaabbbmmm"  # Letters available for constructing words
matching_words = find_matching_words(pattern, word_list, available_letters)
print("Matching words:", matching_words)
