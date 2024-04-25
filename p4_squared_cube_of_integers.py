#make a txt file that named integers.txt, double.txt, triple.txt
#add a method thad read the source file
def squared_cube():
#for reading the integers.txt as number_source
    with open("integers.txt","r") as number_source:
        for line in number_source:
            line = int(line)
#add a method that reads the txt as number source
#add a method that finds the squared of the inetgers
#add a method that finds the cube of the inetgers