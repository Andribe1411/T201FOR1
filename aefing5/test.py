try:
    #filename = input('Filename: ')
    filename = 'aefing5/grimm.txt'
    input_file = open(filename, 'r')
    counter = 0
    story = ""
    line_number = int(input("line number: "))
    story_started = False
    for line in input_file:
        if counter == 4:
            if story_started and len(story.strip())>0:
                break
            else:
                story_started = True
        if story_started:
            story = story + line
        if len(line.strip()) == 0:
            counter +=1
        else:
            counter = 0
    print(story)
    input_file.close()
except:
    print("File not found")