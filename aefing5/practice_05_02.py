sentence = input("Sentence: ")
for x,y in enumerate(sentence):
    if y.isupper():
        new_sentence = sentence[x:]+" "+sentence[:x]
        print(new_sentence.lower())
