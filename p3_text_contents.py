#add a method that write multiple lines of text
#add a method that used mylife.txt for text
proceed = True
while proceed:
    line = input("Enter line: ")
    break_line = line+("\n")
#add a method for looping text
    with open("my_life.txt", "a") as my_life_output:
        my_life_output.write(break_line)
#add an input for lines
        while proceed:
#add a method that ask the user y or n
            repeat = input("Are there any more lines yes/no? \n")
            if repeat.lower() == "yes":
                break
            elif repeat.lower() == "no":
                proceed = False
            else:
                print("Invalid, type yes/no only bro!")
                continue