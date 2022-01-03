"""
Hello Everyone
This a simple game where you have to guess the hidden number between 1 and 21.
"""
import random
print("Welcome to the game")
print("Lets guess the hidden number but !!!only 9 chances you would get :::")
while True:
    a1 = input("\nDo you want to continue yes or no : ") #taking user input
    if a1 == "yes":
        a = random.randrange(1, 21) #choosing random number 
        count = 1 #initialized the counter to count the number of steps taken
        while count<=9: 
            n = int(input("\nEnter the number to guess : "))
            if n > a:
                print("\nGuess a smaller number than this")
                print("Chances left ", 9 - count) #(9 is total chances) 9 - count tells the user how many chances left
                count=count+1 
            elif n<a:
                print("\nGuess number greater than this")
                print("Chances left ", 9 - count)
                count=count+1 

            elif n==a:
                print(f"\nHidden number is {a}")
                print("Congratulations!!! Your guess is correct you won ")
                print(f"You took {count} chances to win the game")
                break
        else:
            print("No chances left")
            print("\nGame Over!!!")
            print("Try next time :)")
    else:
        print("Ok! Thank You :)")
        break
