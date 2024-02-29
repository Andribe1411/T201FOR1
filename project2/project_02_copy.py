# Author: <Andri Benedikt>
# Date: <28-02-2024>
# Project: <project_02>
# Acknowledgements: <>
import statistics
FOLDER = "project2/"
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

AREA_COULUMN = 4
AREACHANGE_COULUMN = 5
ELONGATION_COULUMN = 6
DISTANCE_COULUMN = 7
VELOCITY_COULUMN = 8

def main():
    menu()

def menu():
    on = True
    while on:
        print("Zebra fish analysis:")
        print("1: Area")
        print("2: Areachange")
        print("3: Elongation")
        print("4: Distance moved")
        print("5: Velocity")
        print("6: Quit")
        choice = input("Selection: ")
        if choice == "1":
            file_one_list = area(FILE_ONE)
            file_two_list= area(FILE_TWO)
            file_three_list = area(FILE_THREE)
            file_four_list = area(FILE_FOUR)
            file_five_list = area(FILE_FIVE)
            file_six_list = area(FILE_SIX)
            print_table("AREA",file_one_list, file_two_list, file_three_list, file_four_list, file_five_list, file_six_list)

                    
        elif choice == "2":
            file_one_list = areachange(FILE_ONE)
            file_two_list= areachange(FILE_TWO)
            file_three_list = areachange(FILE_THREE)
            file_four_list = areachange(FILE_FOUR)
            file_five_list = areachange(FILE_FIVE)
            file_six_list = areachange(FILE_SIX)
            print_table("AREACHANGE",file_one_list, file_two_list, file_three_list, file_four_list, file_five_list, file_six_list)
        elif choice == "3":
            file_one_list = elongation(FILE_ONE)
            file_two_list= elongation(FILE_TWO)
            file_three_list = elongation(FILE_THREE)
            file_four_list = elongation(FILE_FOUR)
            file_five_list = elongation(FILE_FIVE)
            file_six_list = elongation(FILE_SIX)
            print_table("ELONGATION",file_one_list, file_two_list, file_three_list, file_four_list, file_five_list, file_six_list)
        elif choice == "4":
            file_one_list = distance(FILE_ONE)
            file_two_list= distance(FILE_TWO)
            file_three_list = distance(FILE_THREE)
            file_four_list = distance(FILE_FOUR)
            file_five_list = distance(FILE_FIVE)
            file_six_list = distance(FILE_SIX)
            print_table("DISTANCE MOVED",file_one_list, file_two_list, file_three_list, file_four_list, file_five_list, file_six_list)
        elif choice == "5":
            file_one_list = velocity(FILE_ONE)
            file_two_list= velocity(FILE_TWO)
            file_three_list = velocity(FILE_THREE)
            file_four_list = velocity(FILE_FOUR)
            file_five_list = velocity(FILE_FIVE)
            file_six_list = velocity(FILE_SIX)
            print_table("VELOCITY",file_one_list, file_two_list, file_three_list, file_four_list, file_five_list, file_six_list)
        elif choice == "6":
            on = False
        else:
            print("Invalid choice")

def open_file(file):
    try:
        input_file = open(FOLDER+file+FILE_EXTENSION, 'r')
        return input_file
    except:
        print(f"Can't open the file {file}")
        return None
        
def get_field_list(file, field_number):
    field_list = []
    line_count = 0
    for line in file:
        line_count += 1
        line = line.split(";")
        if line_count == 1:
            header_lines = int(line[1].strip('"'))
        elif line_count > header_lines:
            field_values = line[field_number].strip('"')
            
            if field_values is not "-":
                field_list.append(float(field_values))
    
    return field_list
  

def adjust_printing(value):
    return str(round(value,3)).rjust(OUTPUT_SPACING)
def get_min(field_list):
    return min(field_list)
def get_max(field_list):
    return max(field_list)
def get_mean(field_list):
    return statistics.mean(field_list)
def get_stdDev(field_list):
    return statistics.stdev(field_list)
def get_count(field_list):
    return len(field_list)

def print_table(field,list_one, list_two, list_three, list_four, list_five, list_six):
    dash_line_length = OUTPUT_SPACING*(NUMBER_OF_FILES+1)
    print("-"*dash_line_length)
    print(f'{field.ljust(15)}{FILE_ONE.rjust(OUTPUT_SPACING)}{FILE_TWO.rjust(OUTPUT_SPACING)}{FILE_THREE.rjust(OUTPUT_SPACING)}{FILE_FOUR.rjust(OUTPUT_SPACING)}{FILE_FIVE.rjust(OUTPUT_SPACING)}{FILE_SIX.rjust(OUTPUT_SPACING)}')
    print("-"*dash_line_length)
    print(f'{"Minimum".ljust(OUTPUT_SPACING)}{adjust_printing(get_min(list_one))}{adjust_printing(get_min(list_two))}{adjust_printing(get_min(list_three))}{adjust_printing(get_min(list_four))}{adjust_printing(get_min(list_five))}{adjust_printing(get_min(list_six))}')
    print(f'{"Maximum".ljust(OUTPUT_SPACING)}{adjust_printing(get_max(list_one))}{adjust_printing(get_max(list_two))}{adjust_printing(get_max(list_three))}{adjust_printing(get_max(list_four))}{adjust_printing(get_max(list_five))}{adjust_printing(get_max(list_six))}')
    print(f'{"Mean".ljust(OUTPUT_SPACING)}{adjust_printing(get_mean(list_one))}{adjust_printing(get_mean(list_two))}{adjust_printing(get_mean(list_three))}{adjust_printing(get_mean(list_four))}{adjust_printing(get_mean(list_five))}{adjust_printing(get_mean(list_six))}')
    print(f'{"StdDev".ljust(OUTPUT_SPACING)}{adjust_printing(get_stdDev(list_one))}{adjust_printing(get_stdDev(list_two))}{adjust_printing(get_stdDev(list_three))}{adjust_printing(get_stdDev(list_four))}{adjust_printing(get_stdDev(list_five))}{adjust_printing(get_stdDev(list_six))}')
    print(f'{"Count".ljust(OUTPUT_SPACING)}{adjust_printing(get_count(list_one))}{adjust_printing(get_count(list_two))}{adjust_printing(get_count(list_three))}{adjust_printing(get_count(list_four))}{adjust_printing(get_count(list_five))}{adjust_printing(get_count(list_six))}')
    print("-"*dash_line_length)


def area(file_number):
    file = open_file(file_number)
    area_list = get_field_list(file,AREA_COULUMN)
    return area_list

def areachange(file_number):
    file = open_file(file_number)
    areachange_list = get_field_list(file,AREACHANGE_COULUMN)
    return areachange_list

def elongation(file_number):
    file = open_file(file_number)
    elongation_list = get_field_list(file,ELONGATION_COULUMN)
    return elongation_list

def distance(file_number):
    file = open_file(file_number)
    distance_list = get_field_list(file,DISTANCE_COULUMN)
    return distance_list

def velocity(file_number):
    file = open_file(file_number)
    velocity_list = get_field_list(file,VELOCITY_COULUMN)
    return velocity_list


if __name__ == "__main__":
   main()
    