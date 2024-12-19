#Personal Program  - Creating Dice Roll 

#Importing random library
import random
#Importing time
import time
#Creating an empty list
Dice_output = []
# Dictionary mapping for die types to sides
dice_sides = {
    'D4': 4,
    'd4': 4,
    'D6': 6,
    'd6': 6,
    'D8': 8,
    'd8': 8,
    'D10': 10,
    'd10': 10,
    'D12': 12,
    'd12': 12,
    'D20': 20,
    'd20': 20,
    'D100': 100,
    'd100': 100}
#Creating subprogram for the random sides
def number_gen(dice_num):
    return random.randint(1, dice_num)
#Creating Sunprogram to print un-interactive menu
def menu():
    print("*******DICE TO BE USED*******\nTraditional Dice (D6)\nTetrahedron Dice (D4)\nOctahedron Dice (D8)\nDecahedron Dice (D10)\nDodecahedron Dice (D12) \nIcosahendron Dice (D20)\nA hundred (D100)\n")
#Creating subprogram to pause
def pause():
    time.sleep(1.2)#Seconds

#Creating Subprogram for the dice role
def dice_roll():
    input_role = input("Please enter a Dice to use, with the D-code: ")
    
    if input_role in dice_sides:
        role_amount = int(input("How many times you would like to role " + input_role + ": "))
        
        for num in range (role_amount):
            roll_result = number_gen(dice_sides[input_role])
            Dice_output.append(roll_result)
        
        print("Rolling...")
        pause()
        print(f"You rolled: {', '.join(map(str, Dice_output))}!")
    else:
        print("Please enter a valid dice code!")
        dice_roll()
        
#Creating subprogram to add the dice roll
def add_dice_roll():
    pos = 0
    for num in (Dice_output):
        pos+=num
    print("Adding...")
    pause()
    print("The sum of your roll is: ", pos, "!")

#Creating the average of the roll
def avg_dice_roll():
    position = 0
    for number in (Dice_output):
        position+=number / len(Dice_output)
        x = round(position, 2)
    print("Averaging...")
    pause()
    print("The average of your roll is: ",x, "!")
    
#Creating subprogram to ask if the user wants the sum of their roll
def dice_sum():
    add_roll = input("Would you like the sum of your roll? Y/N: ")
    add_roll = add_roll.upper()
    
    if add_roll == "Y":
        add_dice_roll()
    elif add_roll == "N":
        print("Thank you for rolling!")
        pause()
        print("Restarting...")
        main_program()
    else:
        print("Invalid input. Please enter either Y or N: ")
        dice_sum()
        
#Creating subprogram to calculate the average    
def dice_avg():
    avg_roll = input("Would you like the average of your roll? Y/N: ")
    avg_roll = avg_roll.upper()
    
    if avg_roll == "Y":
        avg_dice_roll()
    elif avg_roll == "N":
        print("Thank you for rolling!")
        pause()
        print("Restarting...")
        main_program()
    else:
        print("Invalid input. Please enter either Y or N: ")
        dice_avg()
    
        
#Creating subprogram for the main program
def main_program():
    menu()
    dice_roll()
    dice_sum()
    dice_avg()
    
#Calling the main program
main_program()
