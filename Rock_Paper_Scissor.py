import random

user_wins = 0
computer_wins = 0
choice = ['Rock','Paper', 'Scissor']

playgame = input("\n\nROCK PAPER SCISSOR GAME\nIf you want to quit press q now or any key to continue ... ").lower()

name = input("Lets play now!!!!\n\n\nWhat's your name?:  ")
while True:
    if playgame == 'q':
        break

    
    user_input = input("\n\nHello " + name + " Welcome to the game!\n\n Rock, paper or scissor?? :  ") 

    if user_input not in choice:
        continue


    random_num = random.randint(0,2)
    computer_pick = choice[random_num]

    print ("Your Choice : " + user_input + "\nComputer's choice :" + computer_pick)

    if user_input == choice[0] and computer_pick == choice[2]:
        print("You Won!!! ")
        user_wins +=1

    elif user_input == choice[1] and computer_pick == choice[0]:
        print("You Won!!! ")
        user_wins +=1


    elif user_input == choice[2] and computer_pick == choice[1]:
        print("You Won!!! ")
        user_wins +=1
        continue

    else:   
        print("You Lost!!!")
        computer_wins +=1 
    
    print("\n\nHere are the current stats \n\n -- ----- -----  --- \n\n " + name + " : " + str(user_wins) + "\n Computer : " + str(computer_wins) + "\n\n" )
    x = input("\n\nPrint c to conntinue game or any other key to quit ! ")

    if x =='c':
        continue
    else:
        break


print("Goodbye!")
