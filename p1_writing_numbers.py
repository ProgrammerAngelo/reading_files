#add a txt file used for number source
#add a method used for reading the number source
with open("numbers.txt","r") as number_source:#for reading the number txt as a number source
#add a method used for finding even numbers
    for line in number_source:
        if int(line) % 2 == 0:
            with open("even.txt","a") as even_output_files:
                even_output_files.write(line)
#add a method for finding odd numbers