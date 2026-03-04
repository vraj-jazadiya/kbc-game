from trivia_api import get_ques
import random
from rich import print

money_ladder = [0, 1000, 2000, 3000, 5000, 10000, 20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,100000000,700000000 ]
level = 0 

isSkipAvailable = True
isFiftyAvailable = True

player_name = input("Enter your name: ")

print("Welcome to [bold yellow] Kaun Banega Crorepati[/bold yellow] \n")

print("Select Difficulty Level")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    difficulty = "easy"
elif choice == "2":
    difficulty = "medium"
elif choice == "3":
    difficulty = "hard"
else:
    difficulty = "easy"

limit = int(input("How many questions do you want? (max 17): "))

#function call for questions
questions = get_ques(limit, difficulty)

if not questions:
    print("No questions available. Exiting the game.")
    exit()

for i , q in enumerate(questions):
    que = q["question"]["text"]
    corrAns = q["correctAnswer"]  
    inCorrAns = q["incorrectAnswers"]  
    
    options = inCorrAns + [corrAns]
    random.shuffle(options)
    
    print("\n==============================")
    print(f"Qes.{i+1} for ₹{money_ladder[level+1]}")
    print("==============================")
    print(f"\n{que}")
    for j , optn in enumerate(options):
            print(f"{chr(65+j)}. {optn}")
    
    while True:
        ans = input("\nLock your answer (A/B/C/D | skip | quit | 5050): ").upper()
        
        if ans == "QUIT":
            print(f"\nYou quit the game.\nYou won: ₹{money_ladder[level]}")
            break
        
        if ans == "SKIP":
            if isSkipAvailable:
                print("Question skipped! --> NOTE: Now you can't skip it again ")
                isSkipAvailable = False
                break
            else:
                print("Bruuuh... You already used your skip lifeline")
                continue
            
        if ans == "5050":
            
            if not isFiftyAvailable:
                print("50-50 already used")
                continue
            
            print("\n50-50 Lifeline Activated!\n")
            isFiftyAvailable = False
            remaining = [corrAns]
            remaining.append(random.choice(inCorrAns))
            random.shuffle(remaining)
            
            for k , optn in enumerate(remaining):
                print(f"{chr(65+k)}. {optn}")
                
            while True:
                ans = input("\nLock your answer (A/B | SKIP | quit ): ").upper()
                
                if ans == "QUIT":
                    print(f"\nYou quit the game.\nYou won: ₹{money_ladder[level]}")
                    break
            
                if ans == "SKIP":
                    if isSkipAvailable:
                        print("Question skipped! --> NOTE: Now you can't skip it again ")
                        isSkipAvailable = False
                        break
                    else:
                        print("Bruuuh... You already used your skip lifeline")
                        continue
        
                if corrAns == remaining[ord(ans)-65]:
                    print("[bold green]Correct answer! [/bold green]\n")
                    level += 1
                else:
                    print("[bold red]Wrong Answer [/bold red]")
                    print(f"You won: ₹{money_ladder[level]}")
                    exit()
                break
            break
            

        if ans not in ["A", "B", "C", "D"]:
            print("Invalid option. Try again.")
            continue

        if corrAns == options[ord(ans)-65]:
            # print("correct answer!\n")
            print("[bold green]Correct answer! [/bold green]\n")  
            level += 1
        else:
            print("[bold red]Wrong Answer [/bold red]")
            print(f"You won: ₹{money_ladder[level]}")
            exit()
        break
    

print("\n==============================")
print(f"You reached Level {level}")
print(f"You won ₹{money_ladder[level]}")
print("==============================")
    