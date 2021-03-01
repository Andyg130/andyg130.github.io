print ("Hello traveler")
answer = input(" would you like to play a game? (yes/no) ")

if answer.lower().strip() == "yes":

    answer = input("What animal is superior, cats or dogs? ").lower().strip()
    if answer == "dogs":
            print (" Congratulations you won! ")
    elif answer == "cats":
            print (" Wrong answer, you lose! ")
    else: 
        print(" invalid choice, you lost! ")

else: 
    print("Sucks to suck nerd")
