# Author: <Andri Benedikt>
# Date: <28-02-2024>
# Project: <project_02>
# Acknowledgements: <
# https://docs.python.org/3/library/typing.html - fyrir type hints,
# autopep8 fyrir formatting,
# ChatGpt fyrir debugging,
# Github copilot fyrir endurtekningar
# og fékk vin í tölvunarfræði til að fara yfir kóðann fyrir python venjur og fasta>
import statistics
FOLDER = "project2/real/"
#FOLDER = "project2/"
#FOLDER = ""
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

#AREA_COULUMN = 4
AREACHANGE_COULUMN = 5
ELONGATION_COULUMN = 6
DISTANCE_COULUMN = 7
VELOCITY_COULUMN = 8

AREA_CHOICE = "1"
AREACHANGE_CHOICE = "2"
ELONGATION_CHOICE = "3"
DISTANCE_CHOICE = "4"
VELOCITY_CHOICE = "5"
QUIT_CHOICE = "6"


def main():
    if check_files():
        menu()


def check_files() -> bool:
    all_files_exist = True
    all_files = [FILE_ONE, FILE_TWO, FILE_THREE,
                 FILE_FOUR, FILE_FIVE, FILE_SIX]
    for a_file in all_files:
        try_file = open_file(a_file)
        if try_file is None:
            all_files_exist = False
        close_file(try_file)
    if all_files_exist is False:
        print("Check if you have the above files and try again")
    return all_files_exist


def menu():
    on = True
    while on:
        print("Zebra fish analysis:")
        print(f"{AREA_CHOICE}: Area")
        print(f"{AREACHANGE_CHOICE}: Areachange")
        print(f"{ELONGATION_CHOICE}: Elongation")
        print(f"{DISTANCE_CHOICE}: Distance moved")
        print(f"{VELOCITY_CHOICE}: Velocity")
        print(f"{QUIT_CHOICE}: Quit")
        choice = input("Selection: ")

        if choice == AREA_CHOICE:
            print_area_table()
        elif choice == AREACHANGE_CHOICE:
            print_areachange_table()
        elif choice == ELONGATION_CHOICE:
            print_elongation_table()
        elif choice == DISTANCE_CHOICE:
            print_distance_table()
        elif choice == VELOCITY_CHOICE:
            print_velocity_table()
        elif choice == QUIT_CHOICE:
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
    except FileNotFoundError:
        print(f"Can't open the file {file}")
        return None


def close_file(file: object) -> None:
    file.close()


def get_header_lines(file: object) -> int:
    line_count = 0
    for line in file:
        line_count += 1
        line = line.split(";")
        for y, x in enumerate(line):
            if "Number of header lines:" in x:
                header_lines = int(line[y+1].strip('"'))
                return header_lines


def get_column(column_name: str) -> int:
    file = open_file(FILE_ONE)
    line_count = 0
    new_line = []
    header_lines = get_header_lines(file)
    for line in file:
        line_count += 1
        if line_count == header_lines-2:
            new_line.append(line.split(";"))
    for column_number, column in enumerate(new_line[0]):
        if column.strip('"') == column_name:
            return column_number


def get_field_list(file: object, field_number: int) -> list:
    header_lines = get_header_lines(file)
    field_list = []
    line_count = 0
    for line in file:
        line_count += 1
        line = line.split(";")
        if line_count > header_lines:
            field_values = line[field_number].strip('"')

            if field_values != "-":
                field_list.append(float(field_values))
    return field_list


def adjust_printing(value: float) -> str:
    return str(round(value, ROUND_VALUE)).rjust(OUTPUT_SPACING)


def get_min(field_list: list) -> float:
    return min(field_list)


def get_max(field_list: list) -> float:
    return max(field_list)


def get_mean(field_list: list) -> float:
    return statistics.mean(field_list)


def get_stdDev(field_list: list) -> float:
    return statistics.stdev(field_list)


def get_count(field_list: list) -> int:
    return len(field_list)


def print_table(field: str, list_one: list, list_two: list, list_three: list, list_four: list, list_five: list, list_six: list) -> None:
    dash_line_length = OUTPUT_SPACING*(NUMBER_OF_FILES+1)
    all_files = [list_one, list_two, list_three,
                 list_four, list_five, list_six]
    min_list = [get_min(a_list) for a_list in all_files]
    max_list = [get_max(a_list) for a_list in all_files]
    mean_list = [get_mean(a_list) for a_list in all_files]
    stdDev_list = [get_stdDev(a_list) for a_list in all_files]
    count_list = [get_count(a_list) for a_list in all_files]
    header = f'{field.ljust(OUTPUT_SPACING)}'
    file1 = f'{FILE_ONE.rjust(OUTPUT_SPACING)}'
    file2 = f'{FILE_TWO.rjust(OUTPUT_SPACING)}'
    file3 = f'{FILE_THREE.rjust(OUTPUT_SPACING)}'
    file4 = f'{FILE_FOUR.rjust(OUTPUT_SPACING)}'
    file5 = f'{FILE_FIVE.rjust(OUTPUT_SPACING)}'
    file6 = f'{FILE_SIX.rjust(OUTPUT_SPACING)}'
    print("-"*dash_line_length)
    print(f'{header}{file1}{file2}{file3}{file4}{file5}{file6}')
    print("-"*dash_line_length)
    print(f'{"Minimum".ljust(OUTPUT_SPACING)}', end="")
    for a_list in min_list:
        print(adjust_printing(a_list), end="")
    print()
    print(f'{"Maximum".ljust(OUTPUT_SPACING)}', end="")
    for a_list in max_list:
        print(adjust_printing(a_list), end="")
    print()
    print(f'{"Mean".ljust(OUTPUT_SPACING)}', end="")
    for a_list in mean_list:
        print(adjust_printing(a_list), end="")
    print()
    print(f'{"StdDev".ljust(OUTPUT_SPACING)}', end="")
    for a_list in stdDev_list:
        print(adjust_printing(a_list), end="")
    print()
    print(f'{"Count".ljust(OUTPUT_SPACING)}', end="")
    for a_list in count_list:
        print(adjust_printing(a_list), end="")
    print()
    print("-"*dash_line_length)


def area(file_number: str) -> list | None:
    area_coulumn = get_column("Area")
    if file := open_file(file_number):
        area_list = get_field_list(file, area_coulumn)
        close_file(file)
        return area_list


def areachange(file_number: str) -> list | None:
    areachange_coulumn = get_column("Areachange")
    if file := open_file(file_number):
        areachange_list = get_field_list(file, areachange_coulumn)
        close_file(file)
        return areachange_list


def elongation(file_number: str) -> list | None:
    elongation_coulumn = get_column("Elongation")
    if file := open_file(file_number):
        elongation_list = get_field_list(file, elongation_coulumn)
        close_file(file)
        return elongation_list


def distance(file_number: str) -> list | None:
    distance_coulumn = get_column("Distance moved")
    if file := open_file(file_number):
        distance_list = get_field_list(file, distance_coulumn)
        close_file(file)
        return distance_list


def velocity(file_number: str) -> list | None:
    velocity_coulumn = get_column("Velocity")
    if file := open_file(file_number):
        velocity_list = get_field_list(file, velocity_coulumn)
        close_file(file)
        return velocity_list


if __name__ == "__main__":
    main()
