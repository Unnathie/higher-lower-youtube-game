import random
import game_data
import art
print(art.logo)
print("Welcome to HIGHER or LOWER game")
exist=[]
score=0
b={}
game_start=True
while game_start:
    while True:
        first_option=random.choice(game_data.youtube_data)
        if first_option["name"] not in exist:
            break
    if len(b)==0:
        exist.append(first_option["name"])
    else:
        first_option=b
    print(f'Compare A: {first_option["name"]}, a {first_option["description"]}, from {first_option["country"]}.')

    print(art.vs)

    while True:
        second_option = random.choice(game_data.youtube_data)
        if second_option["name"] not in exist:
            break
    exist.append(second_option["name"])
    print(f'Compare B: {second_option["name"]}, a {second_option["description"]}, from {second_option["country"]}.')
    guess=input("Enter your guess 'A' or 'B' ").strip().lower()
    if guess=="a":
        if first_option["subscriber_count"]>second_option["subscriber_count"]:
            score +=1
            print(f"You're right! Your SCORE:{score}")
            b=second_option
        else:
            print(f"YOU WERE WRONG! your SCORE:{score}")
            if score < 4:
                print("That’s not a good score! The average score is 3.2.\nQuick, click Play Again and we will pretend we didn’t see that score!:)")
            elif score < 6:
                print("""Soooooo average!\nCome on... you can get a score of 6 can‘t you?\nKeep trying...""")
            play = input("Do you want to play again? Enter 'YES' or 'NO': ").lower()
            if play == "yes":
                score = 0
                b = {}
                exist=[]
                continue
            elif play == "no":
                print("okay bye!!!")
                game_start=False
    elif guess=="b":
        if first_option["subscriber_count"]<second_option["subscriber_count"]:
            score +=1
            print(f"You're right! Your SCORE:{score}")
            b=second_option
        else:
            print(f"YOU WERE WRONG! your SCORE:{score}")
            if score < 4:
                print(
                    "That’s not a good score! The average score is 3.2.\nQuick, click Play Again and we will pretend we didn’t see that score!:)")
            elif score < 6:
                print("""Soooooo average!\nCome on... you can get a score of 6 can‘t you?\nKeep trying...""")
            play=input("Do you want to play again? Enter 'YES' or 'NO': ").lower()
            if play=="yes":
                score=0
                exist=[]
                b={}
            elif play=="no":
                print("okay bye!!!")
                game_start=False
            else:
                print("WRONG INPUT!!!")
                break
    else:
        print("WRONG INPUT!")
        break

    if len(exist)==len(game_data.youtube_data):
        print(f"YOU WIN THE GAME YOUR SCORE:{score}")
        break
