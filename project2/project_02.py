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
            print_table("Area")
        elif choice == AREACHANGE_CHOICE:
            print_table("Areachange")
        elif choice == ELONGATION_CHOICE:
            print_table("Elongation")
        elif choice == DISTANCE_CHOICE:
            print_table("Distance moved")
        elif choice == VELOCITY_CHOICE:
            print_table("Velocity")
        elif choice == QUIT_CHOICE:
            on = False
        else:
            print("Invalid choice")

# fall sem prentar út töflu með upplýsingum um dálk


def print_table(field: str):
    files = [FILE_ONE, FILE_TWO, FILE_THREE, FILE_FOUR, FILE_FIVE, FILE_SIX]
    stats_functions = [get_min, get_max, get_mean, get_stdDev, get_count]
    stats_names = ["Minimum", "Maximum", "Mean", "StdDev", "Count"]
    all_files_data = [get_column_list(file, field) for file in files]

    dash_line_length = OUTPUT_SPACING * (len(files) + 1)
    print("-" * dash_line_length)

    file_names_header = [field.upper().ljust(OUTPUT_SPACING)] + \
        [filename.rjust(OUTPUT_SPACING) for filename in files]
    print("".join(file_names_header))
    print("-" * dash_line_length)

    for i in range(len(stats_names)):
        stat_name = stats_names[i]
        stat_function = stats_functions[i]
        stats_values = [stat_function(all_files_data[j])
                        for j in range(len(files))]
        stats_line = [f"{stat_name.ljust(
            OUTPUT_SPACING)}"] + [adjust_printing(value) for value in stats_values]
        print("".join(stats_line))

    print("-" * dash_line_length)


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


# föll sem taka inn skráarnafn og skila lista með gildunum úr viðeigandi dálki


def get_column_list(file_number: str, chosen_coulumn) -> list | None:
    coulumn_number = get_column(chosen_coulumn)
    if file := open_file(file_number):
        coulumn_list = get_field_list(file, coulumn_number)
        close_file(file)
        return coulumn_list


# kalla á main fallið
if __name__ == "__main__":
    main()
