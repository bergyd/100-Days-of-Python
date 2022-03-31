import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("Which do you think will beat the computer? Rock, Paper or Scissors?\
\nChoose 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
	print("You typed an invalid number. You lose.")
else:
	comp_choice = random.randint(0, 2)


	if choice == 0:
		print(f"\nYou choose Rock:{Rock}")
		
	if choice == 1:
		print(f"\nYou choose Paper:{Paper}")
		
	if choice == 2:
		print(f"\nYou choose Scissors:{Scissors}")
		
	print("-------------------------------")

	if comp_choice == 0:
		print(f"\nThe Computer choose Rock:{Rock}")
		
	if comp_choice == 1:
		print(f"\nThe Computer choose Paper:{Paper}")
		
	if comp_choice == 2:
		print(f"\nThe Computer choose Scissors:{Scissors}")
		

	if choice == 0 and comp_choice == 2:
		print("You have defeated the computer!")
	elif comp_choice == 0 and choice == 2:
		print("Sorry, the Computer is the winner. You lose.")
	elif choice > comp_choice:
		print("You have defeated the computer!")
	elif comp_choice > choice:
		print("Sorry, the Computer is the winner. You lose.")
	elif choice == comp_choice:
		print("You have tied. It is a draw.")





