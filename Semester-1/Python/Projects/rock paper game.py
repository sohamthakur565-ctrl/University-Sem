import random
import sys
game=("Rock","Paper","Scissor")

def best():
    best0=input("Do you want to do Best of 3 or 5 ? (Y/N) :")
    print("------------------------------------------------------------")
    if best0=='Y' or best0=='y':
        best1=int(input("Enter 3 or 5 for best of 3/5 :"))
        print("------------------------------------------------------------")
        if best1==3:
            a=0
            while a<3:
                a+=1
                print("This is the",a,"th round")
                main2()
                if a==3:
                    if wins_player>wins_bot:
                        print("YOU WINs")
                        print("SCORE-: You:",wins_player,"Bot:",wins_bot,"Tie:",wins_tie)
                        print("THANKS FOR PLAYING")
                        sys.exit()
                    if wins_bot>wins_player:
                        print("BOT WINs")
                        print("SCORE-: You:",wins_player,"Bot:",wins_bot,"Tie:",wins_tie)
                        print("THANKS FOR PLAYING")
                        sys.exit()
                    if wins_tie>wins_player and wins_bot:
                        print("It's a TIE")
                        print("SCORE-: You:",wins_player,"Bot:",wins_bot,"Tie:",wins_tie)
                        print("THANKS FOR PLAYING")
                        sys.exit()
                    
        if best1==5:
            a=0
            while a<5:
                print("This is the",a,"th","round")
                main2()
                if a==5:
                    if wins_player>wins_bot:
                        print("YOU WINs, Score -",wins_player,"::",wins_bot)
                        print("THANKS FOR PLAYING")
                        sys.exit()
                    if wins_bot>wins_player:
                        print("BOT WINs, Score -",wins_bot,"::",wins_player)
                        print("THANKS FOR PLAYING")
                        sys.exit()
        else:
            print("You have to type (3/5)")
            print("------------------------------------------------------------")
            best()
    if best0=='n' or best0=='N':
        print("------------------------------------------------------------")
        print("Okay!!, let's begin the game then")
        print("------------------------------------------------------------")
        main2()
    else:
        again=input("You have to type (Y/N), Do you want to try again? (Y/N) :")
        print("------------------------------------------------------------")
        if again=='yes' or again=='Y' or again=='Yes' or again=='y':
            best()
        else:
            print("Thanks for playing")
            sys.exit()

def main1():
    choose_player=input("Choose Rock...Paper....Scissor: ")
    if choose_player=="rock" or choose_player=="ROCK" or choose_player=="Rock" or choose_player=="paper" or choose_player=="Paper" or choose_player=="PAPER" or choose_player=="scissor" or choose_player=="SCISSOR" or choose_player=="Scissor":
        print("------------------------------------------------------------")
        choose_bot=random.choice(game)
        if choose_player.lower()==choose_bot.lower():   
            print("It's",choose_player,"and",choose_bot,"So, It's a tie")
            print("------------------------------------------------------------")
            print("It's a Tie so no one gets a point")
            wins_tie+=1
            print("YOU :",wins_player,"BOT :",wins_bot,"TIE :",wins_tie)
            print("------------------------------------------------------------")
        if choose_player.lower()=='rock'and choose_bot.lower()=='paper':
            print("You choose:",choose_player, "and Bot choose:",choose_bot,"So, BOT WINS!!")
            print("------------------------------------------------------------")
            wins_bot+=1
            print("YOU :",wins_player,"BOT :",wins_bot,"TIE :",wins_tie)
            print("------------------------------------------------------------")
        if choose_player.lower()=='paper' and choose_bot.lower()=='scissor':
            print("You choose:",choose_player, "and Bot choose:",choose_bot,"So, BOT WINS!!")
            print("------------------------------------------------------------")
            wins_bot+=1
            print("YOU :",wins_player,"BOT :",wins_bot,"TIE :",wins_tie)
            print("------------------------------------------------------------")
        if choose_player.lower()=='scissor' and choose_bot.lower()=='rock':
            print("You choose:",choose_player, "and Bot choose:",choose_bot,"So, BOT WINS!!")
            print("------------------------------------------------------------")
            wins_bot+=1
            print("YOU :",wins_player,"BOT :",wins_bot,"TIE :",wins_tie)
            print("------------------------------------------------------------")
        if choose_bot.lower()=='rock' and choose_player.lower()=='paper':
            print("Bot choose:",choose_bot, "and You choose:",choose_player,"So, YOU WINS!!")
            print("------------------------------------------------------------")
            wins_player+=1
            print("YOU :",wins_player,"BOT :",wins_bot,"TIE :",wins_tie)
            print("------------------------------------------------------------")
        if choose_bot.lower()=='paper' and choose_player.lower()=='scissor':
            print("Bot choose:",choose_bot, "and You choose:",choose_player,"So, YOU WINS!!")
            print("------------------------------------------------------------")
            wins_player+=1
            print("YOU :",wins_player,"BOT :",wins_bot,"TIE :",wins_tie)
            print("------------------------------------------------------------")
        if choose_bot.lower()=='scissor' and choose_player.lower()=='rock':
            print("Bot choose:",choose_bot, "and You choose:",choose_bot,"So, YOU WINS!!")
            print("------------------------------------------------------------")
            wins_player+=1
            print("YOU :",wins_player,"BOT :",wins_bot,"TIE :",wins_tie)
            print("------------------------------------------------------------")
    else:
        again3=("You might have spelt the word wrong, Try again (Y/N): ")
        if again3== 'yes' or again3=='Yes' or again3== 'YES':
            best()
        if again3== 'no' or again3=='No' or again3== 'NO':
            sys.exit("Thanks for playing")
def main2():
    choose_player=input("Choose Rock...Paper....Scissor: ")
    if choose_player=="rock" or choose_player=="ROCK" or choose_player=="Rock" or choose_player=="paper" or choose_player=="Paper" or choose_player=="PAPER" or choose_player=="scissor" or choose_player=="SCISSOR" or choose_player=="Scissor":
        print("------------------------------------------------------------")
        choose_bot=random.choice(game)
        if choose_player.lower()==choose_bot.lower():   
            print("It's",choose_player,"and",choose_bot)
            print("------------------------------------------------------------")
            print("TIE")
            print("------------------------------------------------------------")
        if choose_player.lower()=='rock'and choose_bot.lower()=='paper':
            print("You choose:,choose_player, "and "Bot choose:",choose_bot)
            print("------------------------------------------------------------")
            print("BOT WINS")
            print("------------------------------------------------------------")
        if choose_player.lower()=='paper' and choose_bot.lower()=='scissor':
            print("You choose:",choose_player, "and Bot choose:",choose_bot)
            print("------------------------------------------------------------")
            print("BOT WINS")
            print("------------------------------------------------------------")
        if choose_player.lower()=='scissor' and choose_bot.lower()=='rock':
            print("You choose:",choose_player, "and Bot choose:",choose_bot)
            print("------------------------------------------------------------")
            print("BOT WINS")
            print("------------------------------------------------------------")
        if choose_bot.lower()=='rock' and choose_player.lower()=='paper':
            print("Bot choose:",choose_bot, "and You choose:",choose_player)
            print("------------------------------------------------------------")
            print("YOU WON")
            print("------------------------------------------------------------")
        if choose_bot.lower()=='paper' and choose_player.lower()=='scissor':
            print("Bot choose:",choose_bot, "and You choose:",choose_player)
            print("------------------------------------------------------------")
            print("YOU WON")
            print("------------------------------------------------------------")
        if choose_bot.lower()=='scissor' and choose_player.lower()=='rock':
            print("Bot choose:",choose_bot, "and You choose:",choose_bot)
            print("------------------------------------------------------------")
            print("YOU WON")
            print("------------------------------------------------------------")
    else:
        again3=("You might have spelt the word wrong, Try again (Y/N): ")
        if again3== 'yes' or again3=='Yes' or again3== 'YES':
            best()
        if again3== 'no' or again3=='No' or again3== 'NO':
            sys.exit("Thanks for playing")
            
        
print("HELLO, Welcome to Rock, Paper & Scissor game")
print("------------------------------------------------------------")
name=input("What's your name? :")
print("------------------------------------------------------------")
print("Let's start the game")
print("------------------------------------------------------------")
best()
