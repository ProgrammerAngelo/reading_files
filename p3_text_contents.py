#add a method that write multiple lines of text
#add a method that used mylife.txt for text
proceed = True
while proceed:
    line = input("Enter line: ")
    break_line = line + ("\n")
#add a method for looping text
    with open("my_life.txt") as my_life_output:
        my_life_output.write(break_line)
#add an input for lines
        while proceed:
            repeat = input("Are there any more lines y/n? \n")
#add a method that ask the user y or n
