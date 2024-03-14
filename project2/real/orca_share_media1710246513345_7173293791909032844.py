# Author: <Norbert Maksymilian Kania>
# Date: <05.03.24>
# Project: <Project 02>
# Acknowledgements:
# https://www.geeksforgeeks.org/string-rjust-ljust-python/
# https://docs.python.org/3/tutorial/datastructures.html

# importing statistics module, which has built-in min,max,mean and standard-deviation modules
import statistics

FILENAME1 = '01uM_E6.txt'
FILENAME2 = '1uM_E9.txt'
FILENAME3 = '10uM_E10.txt'
FILENAME4 = '30uM_E4.txt'
FILENAME5 = '100uM_E7.txt'
FILENAME6 = 'HOM_DMSO_D3.txt'

# LIST OF ALL FILENAMES - easier to use ;)
FILENAMES_LIST = FILENAME1, FILENAME2, FILENAME3, FILENAME4, FILENAME5, FILENAME6

#   CONSTANTS
LINES_TO_SKIP = 35  # hardcoded amount of lines, universal for these files, those lines do not contain data I'm interested in

# List of choices offered to user
CHOICE_LIST = "Area", "Areachange", "Elongation", "Distance moved", "Velocity"

# titles of experiments used in header, could be also achieved by using filename with propper stripping
STRING_OF_TITLES = '01uM_E6 1uM_E9 10uM_E10 30uM_E4 100uM_E7 HOM_DMSO_D3'

NR_OF_RESULT_COLUMNS = 6
COLUMN_WIDTH = 15  # coulmn width given in instructions
SEPARATOR = '-'  # separator used in printing the results

# length of separators (1+6)*15: choice column + 6 corresponding to file columns
SEPARATORS_LEN = 105

# delimiter used for separating values in file, (in our case it's semicolon delimited)
DELIMITER = ';'
ROUNDING = 3
#   POSITION CONSTANTS for easy adjusting the positions of corresponding data parameters from fields in line
AREA_POS = 4
AREACHANGE_POS = 5
ELONGATION_POS = 6
DISTANCE_MOVED_POS = 7
VELOCITY_POS = 8

#   FUNCTIONS


def is_number(string):
    """Function checking if string is number (int or float) and returning Boolean value"""
    # Quicker runtime could be achieved with just if string != '"-"': return True
    # but then it would not consider different possibilities of invalid non-numerical data
    try:
        float(string)
        return True
    except ValueError:
        return False


def sorter(FILENAME):
    """Function used for opening the files, sorting and filtering the Area, Areachange, Elongation, Distance moved, Velocity"""
    the_file = open(FILENAME, 'r')  # open given filename as read-only
    # skip lines that do not contain data
    for skip_that_line in range(LINES_TO_SKIP):
        # skipping by simply reading over to-skip lines, moving "DIGITAL CURSOR" til we reach usefull data
        line = the_file.readline()
    # creating empty lists to be used in for loop
    Area = []
    Areachange = []
    Elongation = []
    Distance_moved = []
    Velocity = []
    for line in the_file:  # reading line by line
        # splitting each line by delimiter- effectively creating list out of line
        splitted_line = line.split(DELIMITER)
        # checking viability of "cell" with if statement and appending the previously created lists with floats
        if is_number(splitted_line[AREA_POS]):
            Area.append(float(splitted_line[AREA_POS]))
        if is_number(splitted_line[AREACHANGE_POS]):
            Areachange.append(float(splitted_line[AREACHANGE_POS]))
        if is_number(splitted_line[ELONGATION_POS]):
            Elongation.append(float(splitted_line[ELONGATION_POS]))
        if is_number(splitted_line[DISTANCE_MOVED_POS]):
            Distance_moved.append(float(splitted_line[DISTANCE_MOVED_POS]))
        if is_number(splitted_line[VELOCITY_POS]):
            Velocity.append(float(splitted_line[VELOCITY_POS]))
    the_file.close()  # closing the file after function is done
    # returning the data we're interested in
    return Area, Areachange, Elongation, Distance_moved, Velocity


def list_builder(FILENAMES_LIST):
    """Functions that uses sorter function to create categories lists by file (combining parameters into lists) """
    list_of_areas = []
    list_of_areachanges = []
    list_of_elongations = []
    list_of_distances_moved = []
    list_of_velocities = []
    for i in FILENAMES_LIST:
        Area, Areachange, Elongation, Distance_moved, Velocity = sorter(i)
        list_of_areas.append(Area)
        list_of_areachanges.append(Areachange)
        list_of_elongations.append(Elongation)
        list_of_distances_moved.append(Distance_moved)
        list_of_velocities.append(Velocity)
    return list_of_areas, list_of_areachanges, list_of_elongations, list_of_distances_moved, list_of_velocities


def calculator(lista, choice):
    """Simple function that calculates and rounds the min,max,mean and st.dev from list of values using statistics package"""
    if choice == "Minimum":
        return round(min(lista), ROUNDING)
    if choice == "Maximum":
        return round(max(lista), ROUNDING)
    if choice == "Mean":
        return round(statistics.mean(lista), ROUNDING)
    if choice == "StdDev":
        return round(statistics.stdev(lista), ROUNDING)
    if choice == "Count":
        return len(lista)

# PRINTING FUNCTIONS


def calculations_printer(choosen_list):
    """Function using calculator function to print min,max,mean,st.dev statistics values neatly organised"""
    # Each statistics is printed with specified column width justed to the left
    print("Minimum".ljust(COLUMN_WIDTH), end='')
    # as we've chosen in what parameter (by function input) we're interested in, for loops will calculate statistics from chosen parameter
    # 6 columns for 6 corresponding filenames
    for column in range(NR_OF_RESULT_COLUMNS):
        print(str(calculator(choosen_list[column], "Minimum")).rjust(
            COLUMN_WIDTH), end='')
    print()
    print("Maximum".ljust(COLUMN_WIDTH), end='')
    for column in range(NR_OF_RESULT_COLUMNS):
        print(str(calculator(choosen_list[column], "Maximum")).rjust(
            COLUMN_WIDTH), end='')
    print()
    print("Mean".ljust(COLUMN_WIDTH), end='')
    for column in range(NR_OF_RESULT_COLUMNS):
        print(str(calculator(choosen_list[column], "Mean")).rjust(
            COLUMN_WIDTH), end='')
    print()
    print("StdDev".ljust(COLUMN_WIDTH), end='')
    for column in range(NR_OF_RESULT_COLUMNS):
        print(str(calculator(choosen_list[column], "StdDev")).rjust(
            COLUMN_WIDTH), end='')
    print()
    print("Count".ljust(COLUMN_WIDTH), end='')
    for column in range(NR_OF_RESULT_COLUMNS):
        print(str(calculator(choosen_list[column], "Count")).rjust(
            COLUMN_WIDTH), end='')
    print()
    print(SEPARATOR*SEPARATORS_LEN)


def menu_printer():
    """Super simple function for printing menu of numerical choices for paramaters and "quit" option"""
    print("Zebra fish analysis:")
    print(f"1: {CHOICE_LIST[0]}")
    print(f"2: {CHOICE_LIST[1]}")
    print(f"3: {CHOICE_LIST[2]}")
    print(f"4: {CHOICE_LIST[3]}")
    print(f"5: {CHOICE_LIST[4]}")
    print("6: Quit")


def experiment_names_printer():  
    """Super simple function that prints titles of experiments"""
    # I've created this function because printing file names is a repetitive task that can be handled by it
    # Splitting string of titles into list
    splitted = STRING_OF_TITLES.split()  
    # iterating through that list and printing titles of experiments with right just and specified column width
    for title in splitted:  
        print(title.rjust(COLUMN_WIDTH), end='')
    print()


def header_printer(choice):
    """Function printing what choice has been made and using experiment_names_printer"""
    print(SEPARATOR*SEPARATORS_LEN)
    if choice == list_of_areas:
        print(f"{CHOICE_LIST[0].upper()}".ljust(COLUMN_WIDTH), end='')
        experiment_names_printer()
    if choice == list_of_areachanges:
        print(f"{CHOICE_LIST[1].upper()}".ljust(COLUMN_WIDTH), end='')
        experiment_names_printer()
    if choice == list_of_elongations:
        print(f"{CHOICE_LIST[2].upper()}".ljust(COLUMN_WIDTH), end='')
        experiment_names_printer()
    if choice == list_of_distances_moved:
        print(f"{CHOICE_LIST[3].upper()}".ljust(COLUMN_WIDTH), end='')
        experiment_names_printer()
    if choice == list_of_velocities:
        print(f"{CHOICE_LIST[4].upper()}".ljust(COLUMN_WIDTH), end='')
        experiment_names_printer()
    print(SEPARATOR*SEPARATORS_LEN)

#   CODE


# Printing first menu displayed to the user
menu_printer()
# assuming that user chooses only integers between 1-6
selection = int(input("Selection: "))

if selection != 6:
    # Right after selecting option different than "quit" all categories are preloaded into memory
    list_of_areas, list_of_areachanges, list_of_elongations, list_of_distances_moved, list_of_velocities = list_builder(FILENAMES_LIST)
while selection != 6:  # while loop runs until user inputs 6 - which corresponds to "quit"
    if selection == 1:
        header_printer(list_of_areas)
        calculations_printer(list_of_areas)
    if selection == 2:
        header_printer(list_of_areachanges)
        calculations_printer(list_of_areachanges)
    if selection == 3:
        header_printer(list_of_elongations)
        calculations_printer(list_of_elongations)
    if selection == 4:
        header_printer(list_of_distances_moved)
        calculations_printer(list_of_distances_moved)
    if selection == 5:
        header_printer(list_of_velocities)
        calculations_printer(list_of_velocities)

    menu_printer()
    selection = int(input("Selection: "))