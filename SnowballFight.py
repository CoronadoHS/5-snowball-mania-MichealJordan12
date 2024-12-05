''' 
    Name: Snowball-Mania
    Author: Thomas Buckmiller
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.12.2

'''
import random
import time
def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    print("Welcome to Snowball Mania!")
    name=input("What is your name?")
    print("Great to have you here," + name + "! Who do you want to play against?")
    opponent= input()
    print(name +" VS. "+ opponent)
    

    players=[]
    players.append(name)
    players.append(opponent)

    nextplayer=""

    while(nextplayer != "Done"):
        nextplayer=input("Are there any more opponents? If so, type them one at a time (or Done) and press 'Enter")
        players.append(nextplayer)
    players.remove("Done")
    choice=input("Do you want to choose who to throw the snowball at or play automatic mode)(yes or no please)")
    gameplay(name,players,choice)

    
    
    
def gameplay(name,players,manual):
    while (len(players) > 1):
        Thrower= random.choice(players)
        if (Thrower==name):
            if( manual== "yes"):
                target = input("Its your turn to throw who do you want to eliminate?")
            
            else: 
    
                target=random.choice(players)
                while(target==Thrower):
                    target=random.choice(players)
                #print(target)
        else:
            target=random.choice(players)
            while(target==Thrower):
                    target=random.choice(players)
                #print(target)
        print(Thrower + " is throwing a snowball at " + target + "!")
        time.sleep(2)
        #generate a random Number to use as the hit num
        hitnum=random.randint(1,5)
        success=hitResult(hitnum)
        if (success == True):
            print("its a hit!  "+target+ " is down" )
            if name== Thrower:
                name= input("What do you have to say after that shot? Hit enter if you dont")
          #  if name== Thrower and success== True:
               # Thrower= input("Talk some trash!!")
            players.remove(target)
        else:
            print(" unfortunately, "+ Thrower + " Sucks")
            if target == name and success==False:
                target= input(" Do you want to say anything? If not hit Enter")


    print(players[0] + " is the best snowballer!!")

def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if (hitNum==3):
        return True
    return False

main()
