#make a txt file that named integers.txt, double.txt, triple.txt
#add a method thad read the source file
def squared_cube():
#for reading the integers.txt as number_source
    with open("integers.txt","r") as number_source:
        for line in number_source:
            line = int(line)
#add a method that finds the squared of the inetgers
            if line % 2 == 0:
                square = line **2
                with open("double.txt","a") as squared_output_file:
                    squared_output_file.write(str(square)+"\n")
#add a method that finds the cube of the inetgers
            else:
                cubed = line **3
                with open("triple.txt","a") as cubed_output_file:
                    cubed_output_file.write(str(cubed)+"\n")
squared_cube()