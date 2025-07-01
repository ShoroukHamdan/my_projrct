print("Hello from the new feature branch!")
import random
rock_ascii= """
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
"""
paper_ascii=  """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)  
    """
scissors_ascii="""
      _____
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
    """
Input= input("press Enter to continue or press (Help) for the rules help: ").capitalize()
if Input == "Help":
    print ("""
       *******Rules*******    
       1)You choose and computer chooses
       2)Rock smashes Scissors -> Rock wins
       3)Scissors cut Paper -> Scissors wins
       4)Paper covers Rock -> Paper wins
           """)
user_choice =input("Enter your choice (rock,paper,scissors): ").lower()
if user_choice=="rock":
    print(f"your choice:\n{rock_ascii}")
elif user_choice=="paper":
  print(f"your choice:\n{paper_ascii}")

elif user_choice=="scissors":
    print(f"your choice:\n {scissors_ascii}")
else :
    print ("unvalid choice")
    
choices =["rock","paper","scissors"]
computer_choice=random.choice(choices)

if computer_choice=="rock":
    print(f"computer choice\n{rock_ascii}")
elif computer_choice=="paper":
  print(f"computer choice\n {paper_ascii}")

else:
    print(f"computer choice\n {scissors_ascii}")


if( ( user_choice=="paper" and computer_choice=="rock") 
    or
   ( user_choice=="rock" and computer_choice=="scissors") 
      or
  (user_choice=="scissors" and computer_choice=="paper")
   ):
      print(f"you win!{user_choice} beats {computer_choice}")
elif user_choice == computer_choice:
     print("it is a tie!")
else :
      print(f"You lose! {computer_choice} beats {user_choice}")
    