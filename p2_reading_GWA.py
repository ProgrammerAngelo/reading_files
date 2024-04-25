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