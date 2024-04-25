#add a txt file used for number source
#add a method used for reading the number source
def read_write():
    with open("numbers.txt","r") as number_source:#for reading the number txt as a number source
#add a method used for finding even numbers
        for line in number_source:
            if int(line) % 2 == 0:
                with open("even.txt","a") as even_output_file:
                    even_output_file.write(line)
#add a method for finding odd numbers
            else:
                with open("odd.txt","a") as odd_output_file:
                    odd_output_file.write(line)
read_write()