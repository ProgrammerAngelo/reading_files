#add a method for reading the students name and GWA
path = (r"students_names_GWA.txt")
def find_highest_GWA(path):
#add a method used for reading the students txt as student source file
    with open(path,"r") as source_file:
#add a method for printing names
        data = source_file.read()
        txt_data = eval(data)
        highest_GWA = None
        students_highest_GWA = None
#add a method for printing highest GWA
        for key, value in txt_data.items():
            decimal_value = float(value)
            if highest_GWA is None or decimal_value > float(highest_GWA):
                students_highest_GWA = key
                highest_GWA = value
        return students_highest_GWA, highest_GWA

key, value = find_highest_GWA(path)
print(f"{key}Has a Highest GWA with the value of{value}")