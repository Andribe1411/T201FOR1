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

# skilgreini fasta fyrir skráarnöfn, endingu, og aðra fasta
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

DELIMITTER = ";"
EMPTY_VALUE = "-"

AREA_CHOICE = "1"
AREACHANGE_CHOICE = "2"
ELONGATION_CHOICE = "3"
DISTANCE_CHOICE = "4"
VELOCITY_CHOICE = "5"
QUIT_CHOICE = "6"

# main fall sem kallar á check_files og menu


def main():
    if check_files():
        menu()

# fall sem athugar hvort allar skrárnar séu til


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

# fall sem prentar út valmynd og kallar á viðeigandi föll eftir vali


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

# fall sem prentar út töflu með upplýsingum um Area dálk


def print_area_table():
    area_list = [area(FILE_ONE), area(FILE_TWO), area(
        FILE_THREE), area(FILE_FOUR), area(FILE_FIVE), area(FILE_SIX)]
    print_table("AREA", area_list)

# fall sem prentar út töflu með upplýsingum um Areachange dálk


def print_areachange_table():
    areachange_list = [areachange(FILE_ONE), areachange(FILE_TWO), areachange(
        FILE_THREE), areachange(FILE_FOUR), areachange(FILE_FIVE), areachange(FILE_SIX)]
    print_table("AREACHANGE", areachange_list)

# fall sem prentar út töflu með upplýsingum um Elongation dálk


def print_elongation_table():
    elongation_list = [elongation(FILE_ONE), elongation(FILE_TWO), elongation(
        FILE_THREE), elongation(FILE_FOUR), elongation(FILE_FIVE), elongation(FILE_SIX)]
    print_table("ELONGATION", elongation_list)

# fall sem prentar út töflu með upplýsingum um Distance dálk


def print_distance_table():
    distance_list = [distance(FILE_ONE), distance(FILE_TWO), distance(
        FILE_THREE), distance(FILE_FOUR), distance(FILE_FIVE), distance(FILE_SIX)]
    print_table("DISTANCE MOVED", distance_list)

# fall sem prentar út töflu með upplýsingum um Velocity dálk


def print_velocity_table():
    velocity_list = [velocity(FILE_ONE), velocity(FILE_TWO), velocity(
        FILE_THREE), velocity(FILE_FOUR), velocity(FILE_FIVE), velocity(FILE_SIX)]
    print_table("VELOCITY", velocity_list)

# fall sem opnar skrá og skilar henni


def open_file(file: str) -> object:
    try:
        input_file = open(file+FILE_EXTENSION, 'r')
        return input_file
    except FileNotFoundError:
        print(f"Can't open the file {file}")
        return None

# fall sem lokar skrá


def close_file(file: object) -> None:
    file.close()

# fall sem tekur inn skrá og skilar fjölda línna sem eru header línur


def get_header_lines(file: object) -> int:
    line_count = 0
    for line in file:
        line_count += 1
        line = line.split(";")
        for y, x in enumerate(line):
            if "Number of header lines:" in x:
                header_lines = int(line[y+1].strip('"'))
                return header_lines

# fall sem tekur inn nafn á dálki og skilar númeri dálksins


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

# fall sem tekur inn skrá og númer af dálk og skilar lista með gildunum úr dálkinum


def get_field_list(file: object, field_number: int) -> list:
    header_lines = get_header_lines(file)
    field_list = []
    line_count = 0
    for line in file:
        line_count += 1
        line = line.split(DELIMITTER)
        if line_count > header_lines:
            field_values = line[field_number].strip('"')

            if field_values != EMPTY_VALUE:
                field_list.append(float(field_values))
    return field_list

# fall sem tekur inn float gildi og skilar því sem streng af námunduðu gildi sem er right justified


def adjust_printing(value: float) -> str:
    return str(round(value, ROUND_VALUE)).rjust(OUTPUT_SPACING)

# föll sem taka inn lista og skila minnsta/mesta/meðaltal/staðalfráviki/fjölda gildi/a í listanum


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

# fall sem prentar út töflu með upplýsingum úr öllum skránum


def print_table(field: str, all_files: list) -> None:
    dash_line_length = OUTPUT_SPACING*(NUMBER_OF_FILES+1)
    min_list = [get_min(a_list) for a_list in all_files]
    max_list = [get_max(a_list) for a_list in all_files]
    mean_list = [get_mean(a_list) for a_list in all_files]
    stdDev_list = [get_stdDev(a_list) for a_list in all_files]
    count_list = [get_count(a_list) for a_list in all_files]
    file_names = [f'{field.ljust(OUTPUT_SPACING)}', f'{FILE_ONE.rjust(OUTPUT_SPACING)}', f'{FILE_TWO.rjust(OUTPUT_SPACING)}',
                  f'{FILE_THREE.rjust(OUTPUT_SPACING)}', f'{FILE_FOUR.rjust(OUTPUT_SPACING)}', f'{FILE_FIVE.rjust(OUTPUT_SPACING)}', f'{FILE_SIX.rjust(OUTPUT_SPACING)}']
    print("-"*dash_line_length)
    [print(a_list, end="") for a_list in file_names]
    print()
    print("-"*dash_line_length)
    print(f'{"Minimum".ljust(OUTPUT_SPACING)}', end="")
    [print(adjust_printing(a_list), end="") for a_list in min_list]
    print()
    print(f'{"Maximum".ljust(OUTPUT_SPACING)}', end="")
    [print(adjust_printing(a_list), end="") for a_list in max_list]
    print()
    print(f'{"Mean".ljust(OUTPUT_SPACING)}', end="")
    [print(adjust_printing(a_list), end="") for a_list in mean_list]
    print()
    print(f'{"StdDev".ljust(OUTPUT_SPACING)}', end="")
    [print(adjust_printing(a_list), end="") for a_list in stdDev_list]
    print()
    print(f'{"Count".ljust(OUTPUT_SPACING)}', end="")
    [print(adjust_printing(a_list), end="") for a_list in count_list]
    print()
    print("-"*dash_line_length)

# föll sem taka inn skráarnafn og skila lista með gildunum úr viðeigandi dálki


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


# kalla á main fallið
if __name__ == "__main__":
    main()
