keep_going = 0
print("Recorded victories in last 20 games of Bullshit \n \n")
name_list = ["Dell", "Paige", "Austin", "Destiny"]
score_list = ["6", "3", "6", "5"]
zipped = zip(name_list, score_list)
while(keep_going == 0):
    user_input = input("Type 'Add' to add names and values to the list \n type 'Remove' to delete vaues from the list \n type 'Quit' to end the list ")
    if(user_input == "Add"):
        new_name= input("What is the name of the person you wish to add? ")
        new_score= input("What score corresponds to the newly entered person? ")
        name_list.append(new_name)
        score_list.append(new_score)
    elif(user_input == "Remove"):
         new_name= input("What is the name of the person you wish to remove? ")
         new_score= input("which person were they in the list? ")
         name_list.remove(new_name)
         score_list.remove(new_score)
    else:
        keep_going = keep_going + 1
    print([i for i in zip(name_list, score_list)])
print("Goodbye")

