# Author: <Andri Benedikt>
# Date: <28-02-2024>
# Project: <project_02>
# Acknowledgements: <autopep8 fyrir formatting, ChatGpt fyrir debugging og Github copilot fyrir endurtekningar>
import statistics
FOLDER = "project2/real/"
# FOLDER = "project2/"
# FOLDER = ""
FILE_EXTENSION = ".txt"
FILE_ONE = "01uM_E6"
FILE_TWO = "1uM_E9"
FILE_THREE = "10uM_E10"
FILE_FOUR = "30uM_E4"
FILE_FIVE = "100uM_E7"
FILE_SIX = "HOM_DMSO_D3"

OUTPUT_SPACING = 15
NUMBER_OF_FILES = 6
ROUND_VALUE = 3

AREA_COULUMN = 4
AREACHANGE_COULUMN = 5
ELONGATION_COULUMN = 6
DISTANCE_COULUMN = 7
VELOCITY_COULUMN = 8

CHOICE_ONE = "1"
CHOICE_TWO = "2"
CHOICE_THREE = "3"
CHOICE_FOUR = "4"
CHOICE_FIVE = "5"
CHOICE_SIX = "6"


def main():
    menu()


def menu():
    on = True
    while on:
        print("Zebra fish analysis:")
        print(f"{CHOICE_ONE}: Area")
        print(f"{CHOICE_TWO}: Areachange")
        print(f"{CHOICE_THREE}: Elongation")
        print(f"{CHOICE_FOUR}: Distance moved")
        print(f"{CHOICE_FIVE}: Velocity")
        print(f"{CHOICE_SIX}: Quit")
        choice = input("Selection: ")

        if choice == CHOICE_ONE:
            print_area_table()
        elif choice == CHOICE_TWO:
            print_areachange_table()
        elif choice == CHOICE_THREE:
            print_elongation_table()
        elif choice == CHOICE_FOUR:
            print_distance_table()
        elif choice == CHOICE_FIVE:
            print_velocity_table()
        elif choice == CHOICE_SIX:
            on = False
        else:
            print("Invalid choice")


def print_area_table():
    file_one_list = area(FILE_ONE)
    file_two_list = area(FILE_TWO)
    file_three_list = area(FILE_THREE)
    file_four_list = area(FILE_FOUR)
    file_five_list = area(FILE_FIVE)
    file_six_list = area(FILE_SIX)
    print_table("AREA", file_one_list, file_two_list, file_three_list,
                file_four_list, file_five_list, file_six_list)


def print_areachange_table():
    file_one_list = areachange(FILE_ONE)
    file_two_list = areachange(FILE_TWO)
    file_three_list = areachange(FILE_THREE)
    file_four_list = areachange(FILE_FOUR)
    file_five_list = areachange(FILE_FIVE)
    file_six_list = areachange(FILE_SIX)
    print_table("AREACHANGE", file_one_list, file_two_list,
                file_three_list, file_four_list, file_five_list, file_six_list)


def print_elongation_table():
    file_one_list = elongation(FILE_ONE)
    file_two_list = elongation(FILE_TWO)
    file_three_list = elongation(FILE_THREE)
    file_four_list = elongation(FILE_FOUR)
    file_five_list = elongation(FILE_FIVE)
    file_six_list = elongation(FILE_SIX)
    print_table("ELONGATION", file_one_list, file_two_list,
                file_three_list, file_four_list, file_five_list, file_six_list)


def print_distance_table():
    file_one_list = distance(FILE_ONE)
    file_two_list = distance(FILE_TWO)
    file_three_list = distance(FILE_THREE)
    file_four_list = distance(FILE_FOUR)
    file_five_list = distance(FILE_FIVE)
    file_six_list = distance(FILE_SIX)
    print_table("DISTANCE MOVED", file_one_list, file_two_list,
                file_three_list, file_four_list, file_five_list, file_six_list)


def print_velocity_table():
    file_one_list = velocity(FILE_ONE)
    file_two_list = velocity(FILE_TWO)
    file_three_list = velocity(FILE_THREE)
    file_four_list = velocity(FILE_FOUR)
    file_five_list = velocity(FILE_FIVE)
    file_six_list = velocity(FILE_SIX)
    print_table("VELOCITY", file_one_list, file_two_list,
                file_three_list, file_four_list, file_five_list, file_six_list)


def open_file(file: str) -> object:
    try:
        input_file = open(FOLDER+file+FILE_EXTENSION, 'r')
        return input_file
    except:
        print(f"Can't open the file {file}")
        return None


def close_file(file: object) -> None:
    file.close()


def get_field_list(file : object, field_number : int) -> list:
    field_list = []
    line_count = 0
    for line in file:
        line_count += 1
        line = line.split(";")
        if line_count == 1:
            header_lines = int(line[1].strip('"'))
        elif line_count > header_lines:
            field_values = line[field_number].strip('"')

            if field_values != "-":
                field_list.append(float(field_values))
    return field_list


def adjust_printing(value : float) -> str:
    return str(round(value, ROUND_VALUE)).rjust(OUTPUT_SPACING)


def get_min(field_list: list)-> float:
    return min(field_list)


def get_max(field_list: list)-> float:
    return max(field_list)


def get_mean(field_list: list)-> float:
    return statistics.mean(field_list)


def get_stdDev(field_list: list)-> float:
    return statistics.stdev(field_list)


def get_count(field_list: list)-> int:
    return len(field_list)


def print_table(field : str, list_one : list, list_two: list, list_three: list, list_four: list, list_five: list, list_six: list) -> None:
    dash_line_length = OUTPUT_SPACING*(NUMBER_OF_FILES+1)
    print("-"*dash_line_length)
    print(f'{field.ljust(OUTPUT_SPACING)}{FILE_ONE.rjust(OUTPUT_SPACING)}{FILE_TWO.rjust(OUTPUT_SPACING)}{FILE_THREE.rjust(
        OUTPUT_SPACING)}{FILE_FOUR.rjust(OUTPUT_SPACING)}{FILE_FIVE.rjust(OUTPUT_SPACING)}{FILE_SIX.rjust(OUTPUT_SPACING)}')
    print("-"*dash_line_length)
    print(f'{"Minimum".ljust(OUTPUT_SPACING)}{adjust_printing(get_min(list_one))}{adjust_printing(get_min(list_two))}{adjust_printing(
        get_min(list_three))}{adjust_printing(get_min(list_four))}{adjust_printing(get_min(list_five))}{adjust_printing(get_min(list_six))}')
    print(f'{"Maximum".ljust(OUTPUT_SPACING)}{adjust_printing(get_max(list_one))}{adjust_printing(get_max(list_two))}{adjust_printing(
        get_max(list_three))}{adjust_printing(get_max(list_four))}{adjust_printing(get_max(list_five))}{adjust_printing(get_max(list_six))}')
    print(f'{"Mean".ljust(OUTPUT_SPACING)}{adjust_printing(get_mean(list_one))}{adjust_printing(get_mean(list_two))}{adjust_printing(
        get_mean(list_three))}{adjust_printing(get_mean(list_four))}{adjust_printing(get_mean(list_five))}{adjust_printing(get_mean(list_six))}')
    print(f'{"StdDev".ljust(OUTPUT_SPACING)}{adjust_printing(get_stdDev(list_one))}{adjust_printing(get_stdDev(list_two))}{adjust_printing(
        get_stdDev(list_three))}{adjust_printing(get_stdDev(list_four))}{adjust_printing(get_stdDev(list_five))}{adjust_printing(get_stdDev(list_six))}')
    print(f'{"Count".ljust(OUTPUT_SPACING)}{adjust_printing(get_count(list_one))}{adjust_printing(get_count(list_two))}{adjust_printing(
        get_count(list_three))}{adjust_printing(get_count(list_four))}{adjust_printing(get_count(list_five))}{adjust_printing(get_count(list_six))}')
    print("-"*dash_line_length)


def area(file_number):
    if file := open_file(file_number):
        area_list = get_field_list(file, AREA_COULUMN)
        close_file(file)
        return area_list


def areachange(file_number: str) -> list:
    if file := open_file(file_number):
        areachange_list = get_field_list(file, AREACHANGE_COULUMN)
        close_file(file)
        return areachange_list


def elongation(file_number: str)-> list:
    if file := open_file(file_number):
        elongation_list = get_field_list(file, ELONGATION_COULUMN)
        close_file(file)
        return elongation_list


def distance(file_number: str)-> list:
    if file := open_file(file_number):
        distance_list = get_field_list(file, DISTANCE_COULUMN)
        close_file(file)
        return distance_list


def velocity(file_number: str)-> list:
    if file := open_file(file_number):
        velocity_list = get_field_list(file, VELOCITY_COULUMN)
        close_file(file)
        return velocity_list


if __name__ == "__main__":
    main()
