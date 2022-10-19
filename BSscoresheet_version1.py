print("Recorded victories in last 20 games of Bullshit \n \n")
name_list = ["Dell", "Paige", "Austin", "Destiny"]
score_list = ["6", "3", "6", "5"]

while(True):
    for names in name_list:
        print(names, end = "   ")
    print("\n")
    for scores in score_list:
        print(scores, end = "        ")
    print("\n \n")
    user_input =input("Would you like to add a new name to the list?  ")
    if(user_input == "yes" or user_input == "Yes"):
        new_name = input("Enter the new name:  ")
        name_list.append(new_name)
        new_score = input("How many wins has this new player had?  ")
        score_list.append(new_score)
    user_input = input("Would you like to remove anyone from the scoresheet?  ")   
    if(user_input == "yes" or user_input == "Yes"):
        delete_name = input("Who do you no longer play games with?  ")
        name_list.remove(delete_name)
        delete_number = int(input("Where are they in the list?"))
        score_list.remove(score_list[delete_number])
    user_input = input("Are you done updating the scoresheet?  ")
    if(user_input != "no" and user_input != "No"):
        break
for names in name_list:
    print(names, end = "   ")
print("\n")
for scores in score_list:
    print(scores, end = "        ")