# Author: <Andri Benedikt>
# Date: <09-04-2024>
# Project: <assignment_05_02>
# Acknowledgements: <>

class Distribution:
    def __init__(self,file="") -> None:
        self.file = file
        self.add_file_info()
        
    def add_file_info(self):
        new_set = []
        for x in self.file:
            new_set += x.strip().split()
        
        distribution_dict = {}
        for y in sorted(set(new_set)):
            distribution_dict[int(y)] = int(new_set.count(y))
        self.distribution = distribution_dict

        print(new_set)
        print(set(new_set))

    def set_distribution(self, input_dict):
        self.distribution = input_dict

    def average(self):
        summa = 0
        fjoldi = 0
        for x in self.distribution:
            fjoldi += self.distribution[x]
            summa += self.distribution[x]*x
        return summa/fjoldi
    
#The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). 
#In addition, the class should supply an __eq__() method.
    def __gt__(self, other):
        return self.average() > other.average()

    def __ge__(self, other):
        return self.average() >= other.average()

    def __lt__(self, other):
        return self.average() < other.average()

    def __le__(self, other):
        return self.average() <= other.average()


    
    def __str__(self):
        distribution_contents = ""
        for x in self.distribution:
            distribution_contents += str(x) +": "+ str(self.distribution[x]) +"\n"
        return distribution_contents
    
    def __add__(self, other):
        result_data = {}
        # Combine keys from both distributions
        all_keys = set(self.distribution.keys()) | set(other.distribution.keys())
        for key in all_keys:
            result_data[key] = self.distribution.get(key, 0) + other.distribution.get(key, 0)
        # Create a new Distribution object with the combined data
        new_distribution = Distribution()
        new_distribution.set_distribution(result_data)
        return new_distribution

            
    
'''
def open_file(filename):
    #Returns a file stream if filename found, otherwise None
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None


dist1 = Distribution()
dist1.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4})
print("Dist1: ")
print(dist1)
print(dist1.average())

filename = input("Enter filename: ")
file_stream = open_file(filename)

dist2 = Distribution(file_stream)
print("\nDist2: ")
print(dist2)
print(dist2.average())

if dist1 >= dist2:
    print("Dist1 >= Dist2")
else:
    print("Dist2 > Dist1")

dist3 = dist1 + dist2
print("\nDist3: ")
print(dist3)
print(dist3.average())
'''