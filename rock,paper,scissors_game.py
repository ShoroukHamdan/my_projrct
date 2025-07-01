import random
print ("Welcom to the Rock,Paper,Scissors Game:")
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
    print("""
you choose 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)       
          """)
elif user_choice=="paper":
    print("""
    you choose
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)      
          """)
elif user_choice=="scissors":
    print("""
     you choose 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)     
          """)
    
else :
    print("unvalid choice")
    
choices =["rock","paper","scissors"]

index=random.randint(0,2)
computer_choice=choices[index]

if computer_choice=="rock":
    print("""
computer choose 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)       
          """)
elif computer_choice=="paper":
    print("""
    computer choose
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)      
          """)
elif computer_choice=="scissors":
    print("""
     computer choose 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)     
          """)
    
else :
    print("unvalid choice")
    
if user_choice!=computer_choice:
    if user_choice=="paper" and computer_choice=="rock":
        print ("you win! paper cover the rock")
     
    if user_choice=="rock" and computer_choice=="scissors":
        print ("you win! rock smashe the scissors")
      
    if user_choice=="scissors" and computer_choice=="paper":
        print("you win! scissors beats the paper ")    
        
        
       
    if user_choice=="paper" and computer_choice=="scissors":
          print("you lose! scissors beats the paper")
        
    if user_choice=="rock" and computer_choice=="paper":
         print("you lose! paper beats the rock")
         
    if user_choice=="scissors" and computer_choice=="rock":     
         print("you lose! rock smashe the scissors ")
        
else :
    print("you are equal to the computer")
        
    


