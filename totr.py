#Reference Files
#https://lotr.fandom.com/wiki/Quest_of_the_Ring
#https://www.asciiart.eu/books/lord-of-the-rings

import random
import time

#Title page/main menu
def main():
    print(" _____         _ _          __   _   _           ______ _")
    print("|_   _|       (_) |        / _| | | | |          | ___ (_)")
    print("  | |_ __ __ _ _| |   ___ | |_  | |_| |__   ___  | |_/ /_ _ __   __ _ ___ ")
    print("  | | '__/ _` | | |  / _ \|  _| | __| '_ \ / _ \ |    /| | '_ \ / _` / __|")
    print("  | | | | (_| | | | | (_) | |   | |_| | | |  __/ | |\ \| | | | | (_| \__ \ ")
    print("  \_/_|  \__,_|_|_|  \___/|_|    \__|_| |_|\___| \_| \_|_|_| |_|\__, |___/")
    print("                                                                 __/ |    ")
    print("                                                                |___/")
    print("\n")
    print("Welcome to the Hobbiton Trail")
    print("Travel from the Shire to Mordor to deliver the one ring!")
    print("1.) Start")
    print("2.) Exit")
    option = input("-->")
    if option == "1" or option == "start" or option == "Start":
        start()
    elif option == "2" or option == "Exit" or option == "exit":
        quit()
    else:
        main()
                
#asking name of main player "Ring-bearer"
def start():
    print("\n")
    global player_name
    player_name = input("What is your name, young hobbit?: ")
    while len(player_name)>0:
        if len(player_name)>1:
            print(str(player_name)+"? A fine hobbit name.")
            companion()
        elif len(player_name)==1:
            player_name_choice = input(str(player_name)+"? Truly? Only one letter? Must be Dwarvish. Are you certain that's your name? (y/n):")
            if player_name_choice == "y" or player_name_choice == "Y":
                print("\n")
                print("Very well..."+(str(player_name))+"... *grumble*... I'm still going to treat you like any other hobbit!")
                companion()
            elif player_name_choice == "n" or player_name_choice == "N":
                player_name = input("What is your name: ")
                companion()
        else:
            print("Did you write anything? My eyes must be going. Could you write that again for me?")
            player_name = input("What is your name: ")
            companion()
     
#asking name of companion "gardener"
def companion():
    print("\n")
    global companion_name
    companion_name = input("This is a dangerous journey to undertake alone, who will be joining you?: ")
    while len(companion_name)>0:
        if len(companion_name)>1:
            print (str(companion_name)+"? A worthy companion.")
            f.companions.append(companion_name)
            mode()
        elif len(companion_name)==1:
            companion_name_choice = input(str(companion_name)+"? *sigh* Another dwarf? There's sure to be too much singing on this journey. Are you sure that's who you wish to travel with? (y/n):")
            if companion_name_choice == "y" or player_name_choice =="Y":
                print("Very well..."+(str(companion_name))+"... *sigh* ... Save me from the stubbornness of Dwarves.")
                f.companions.append(companion_name)
                mode()
            elif companion_name_choice == "n" or player_name_choice == "N":
                companion_name = input("Who will be joining you?: ")
                f.companions.append(companion_name)
                mode()
        

 #starting variables to refer back to/modify   
class party():
    def fellowship(object):
        disbanded = False
        def ofthering(self):
            if self.disbanded:
                continue_choice = input("the fellowship is disbanded, but not yet broken. Try again? (y/n): ")
                if continue_choice == "y" or continue_choice =="Y":
                    start()
                else:
                    main()
                
f = party()
f.companions = []
f.weapons = 2
f.water = 0
f.ponies = 2
f.miles = 1535
f.day = 0
f.food = 0


def party():
    disbanded == False
    if disbanded == True:
        continue_choice = input("The fellowship is broken, but not yet disbanded. Try again? (y/n): ")
        if continue_choice == "y" or continue_choice == "Y":
            start()
        elif continue_choice == "n" or continue_choice == "N":
            main()
 
#main and starting stats for main player. Death statement. 
def ringbearer():
    r.alive == True
    r.fleshwound = False
    r.RingMad = False
    r.LazyHobbit = False
    if r.alive ==  False:
        print("\n")
        continue_choice = input("The ring-bearer has fallen. But not all hope is yet lost. Try again? (y/n?): ")
        if continue_choice == "y" or continue_choice == "Y":
            start()
        elif continue_choice == "n" or continue_choice == "N":
            main()

#main and starting stats for companion character. Death statement.
def gardener():
    g.alive == True
    g.fleshwound = False
    g.LazyHobbit = False
    if g.alive == False:
        print("\n")
        print("Your companion has fallen... their final words are whispered out.")
        time.sleep(3)
        print("\n")
        print("'I made a promise, player_name. A promise.")
        time.sleep(1)
        print("Don't you leave them, companion_name.")
        time.sleep(1)
        print("And I don't mean to.")
        time.sleep(2)
        print("I don't mean to.'")
        time.sleep(3)
        continue_choice = input ("The journey cannot continue without your dearest friend. Do you attempt the journey again? (y/n?): ")
        if continue_choice == "y" or continue_choice == "Y":
            start()
        elif continue_choice == "n" or continue_choice == "N":
            main()
            
            
#choose difficulty level
def mode():
    print("\n")
    print("The road ahead is long and arduous, though perhaps I can ease your way.")
    mode_choice = input("How difficult of a journey would you like to undertake? (easy, normal, hard, impossible): ")
    if mode_choice == "easy":
        f.food = 1000
        f.water = 1000
        intro()
    elif mode_choice == "normal":
        f.food = 500
        f.water = 500
        intro()
    elif mode_choice == "hard":
        f.food = 300
        f.water = 300
        intro()
    elif mode_choice == "impossible":
        f.food = 100
        f.water = 100
        intro()
    else:
        print("please check your spelling and try again")
        mode()
        
#Intro text
def intro():
    print("\n")
    print("You have a difficult road ahead of you my young hobbit.")
    time.sleep(1)
    print("You carry with you one of the great rings of power.")
    time.sleep(1)
    print("THE great ring of power.")
    time.sleep(1)
    print("                                             _______________________")
    print("   _______________________-------------------                       `|")
    print(" /:--__                                                              |")
    print("||< > |                                   ___________________________/")
    print("| \__/_________________-------------------                         |")
    print("|                                                                  |")
    print(" |                       THE LORD OF THE RINGS                      |")
    print(" |                                                                  |")
    print(" |       Three Rings for the Elven-kings under the sky,             |")
    print("  |        Seven for the Dwarf-lords in their halls of stone,        |")
    print("  |      Nine for Mortal Men doomed to die,                          |")
    print("  |        One for the Dark Lord on his dark throne                  |")
    print("  |      In the Land of Mordor where the Shadows lie.                 |")
    print("   |       One Ring to rule them all, One Ring to find them,          |")
    print("   |       One Ring to bring them all and in the darkness bind them   |")
    print("   |     In the Land of Mordor where the Shadows lie.                |")
    print("   |                                              ____________________|_")
    print("  |  ___________________-------------------------                      `|")
    print("  |/`--_                                                                 |")
    print("  ||[ ]||                                            ___________________/")
    print("   \===/___________________--------------------------")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    time.sleep(2)
    proceed = input("To proceed on your journey, select any key and hit enter: ")
    if proceed !=" ":
        chp1()
    else: #easter egg because I'm a dork
        print("\n")
        print("Any key except that one! Fool of a Took! Hold on, I'll fix this.")
        time.sleep(2)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("*grunt*")
        time.sleep(1)
        print("...")
        time.sleep(.5)
        print("Ahh, there we go.")
        time.sleep(2)
        chp1()

#Chapter 1 text
def chp1():
    print("\n")
    print("It's a dangerous business, "+str(player_name)+", going out your door.")
    time.sleep(1)
    print("You step onto the road, and if you don't keep your feet,")
    time.sleep(1)
    print("there's no knowing where you might be swept off to")
    time.sleep(1)
    print("\n")
    print("                    . .:.:.:.:. .:\     /:. .:.:.:.:. ,")
    print("               .-._  `..:.:. . .:.:`- -':.:. . .:.:.,'  _.-.")
    print("              .:.:.`-._`-._..-''_...---..._``-.._.-'_.-'.:.:.")
    print("           .:.:. . .:_.`' _..-''._________,``-.._ `.._:. . .:.:.")
    print("        .:.:. . . ,-'_.-''      ||_-(O)-_||      ``-._`-. . . .:.:.")
    print("       .:. . . .,'_.'           '---------'           `._`.. . . .:.:")
    print("     :.:. . . ,','               _________               `.`. . . .:.:")
    print("    `.:.:. .,','            _.-''_________``-._            `._.     _.':")
    print("  -._  `._./ /            ,'_.-'' ,       ``-._`.          ,' '`:..'  _.-:")
    print(" .:.:`-.._' /           ,','                   `.`.       /'  '  \\.-':.:.:")
    print(" :.:. . ./ /          ,','               ,       `.`.    / '  '  '\\. .:.::")
    print(":.:. . ./ /          / /    ,                      \ \  :  '  '  ' \\. .:.:")
    print(".:. . ./ /          / /            ,          ,     \ \ :  '  '  ' '::. .:.")
    print(":. . .: :    o     / /                               \ ;'  '  '  ' ':: . .:")
    print(".:. . | |   /_\   : :     ,                      ,    : '  '  '  ' ' :: .:.")
    print(":. . .| |  ((<))  | |,          ,       ,             |\'__',-._.' ' ||. .:")
    print(".:.:. | |   `-'   | |---....____                      | ,---\/--/  ' ||:.:.")
    print("------| |         : :    ,.     ```--..._   ,         |''  '  '  ' ' ||----")
    print("_...--. |  ,       \ \             ,.    `-._     ,  /: '  '  '  ' ' ;;..._")
    print(":.:. .| | -O-       \ \    ,.                `._    / /:'  '  '  ' ':: .:.:")
    print(".:. . | |_(`__       \ \                        `. / / :'  '  '  ' ';;. .:.")
    print(":. . .<' (_)  `>      `.`.          ,.    ,.     ,','   \  '  '  ' ;;. . .:")
    print(".:. . |):-.--'(         `.`-._  ,.           _,-','      \ '  '  '//| . .:.")
    print(":. . .;)()(__)(___________`-._`-.._______..-'_.-'_________\'  '  //_:. . .:")
    print(".:.:,' \/\/--\/--------------------------------------------`._',;'`. `.:.::")
    print(":.,' ,' ,'  ,'  /   /   /   ,-------------------.   \   \   \  `. `.`. `..:")
    print(",' ,'  '   /   /   /   /   //                   \\   \   \   \   \  ` `...:")
    print("\n")
    time.sleep(1)
    print("And so "+(str(player_name))+" set forth on their journey,")
    print("accompanied by their loyal friend and gardener "+(str(companion_name))+",")
    print("to the city of Bree, to meet with Gandalf.")
    print("\n")
    time.sleep(2)
    trav1()


#stats to display during travel/in future GUI
def init_stat():
    print("CURRENT STATUS")
    print("Days on the road: "+(str(f.day)))
    print("Miles to Mordor: "+(str(f.miles)))
    print("Companions: "+ ", ".join(f.companions))
    print("Food remaining: "+(str(f.food)))
    print("Water remaining: "+(str(f.water)))
    print("Ponies: "+(str(f.ponies)))
    print("Weapons: "+(str(f.weapons)))
    print("\n")

#Actions that players can potentially take
def progress():
    travelevents()
    deathcheck()
    miles_traveled = random.randint(30,60)
    f.day +=1
    f.miles = f.miles - miles_traveled + f.ponies*5
    f.food = f.food - 1 - len(f.companions) - f.ponies
    f.water = f.water - 1 - len(f.companions) - f.ponies
 
##random travel events that can occur during progress 
def travelevents():
    event = random.randint(1,20)
    if event == 1:
        print("\n")
        print("The Nazgul are on your trail. You must hide to avoid them, this costs you one day of travel and supplies.")
        f.day +=1
        f.food = f.food - 1 - len(f.companions) - f.ponies
        f.water = f.water - 1 - len(f.companions) - f.ponies
    elif event == 2:
        print("\n")
        print("An Uruk-Hai war party is traveling nearby. You run for cover, dropping some food.")
        f.food = f.food - 10
    elif event == 3:
        print("\n")
        print("The eye of Sauron has noticed you. Lie low for a while until his gaze passes. This costs you one day of travel and supplies.")
        f.day +=1
        f.food = f.food - 1 - len(f.companions) - f.ponies
        f.water = f.water - 1 - len(f.companions) - f.ponies
    elif event ==4:
        print("\n")
        print("A member of your party has been bitten by a gigantic spider. You use water to cleanse the wound.")
        f.water = f.water - 10
    elif event ==5:
        print("\n")
        print("The Nazgul have spotted you! Do you fight or do you run?")
        fight_flight = input("(fight/run): ")
        if fight_flight == "fight":
            while f.weapons <= 0:
                print("You have no weapons! The Nazgul overpower you and kill the party in their quest for the ring.")
                r.alive == False
            while weapons >0:
                brawl = random.randint(1,3)
                if brawl ==1:
                    print("\n")
                    print("You successfully fight off the Nazgul")
                if brawl ==2:
                    print("\n")
                    print("You succsessfully fend off the Nazgul for now, but one of your weapons is broken in the fight")
                    f.weapons -= 1
                else:
                    print("\n")
                    print("One of the Nazgul has managed to stab you. "+(str(player_name))+" has an injury.")
                    r.fleshwound = True
                    ringbearer()
        else:
            runchance = random.randint(1,3)
            if runchance ==1:
                print("\n")
                print("You drop some of your food and water in your escape.")
                f.food -= 15
                f.water -= 15
            else:
                print("\n")
                print("You got away safely.")

def forage():
    print("\n")
    f.day += 1
    eventf = random.randint(1,5)
    foraged = random.randint(10,21)
    if eventf == 1:
        print("You've found mushrooms!")
        f.food = f.food + foraged
        f.water = f.water + foraged
    elif eventf == 2:
        print("You've found potatoes!")
        f.food = f.food + foraged
        f.water = f.water + foraged
    elif eventf == 3:
        print("You've found... something. It appears to be edible.")
        f.food = f.food + foraged - 5
        f.water = f.water + foraged
    elif eventf ==4:
        print("The land here appears barren, there's no food to be found.")
    else:
        print("You've found mushrooms! In your haste you eat them before identifying them and realize they are poisoned. You waste 5 water rinsing your mouth.")
        f.water = f.water - 5
            
def hunt():
    print("\n")
    f.day +=1
    eventh = random.randint(1,6)
    caught = random.randint(20,40)
    if eventh ==1:
        print("You've caught a deer!")
        f.food = f.food + caught
    if eventh ==2:
        print("You've caught some rabbits!")
        f.food = f.food + caught
    if eventh ==3:
        print("You caught a troll... better him than us... and better than starving... I guess.")
        f.food = f.food + caught
    if eventh ==4:
        print("The Uruk-Hai marched through here recently. There is no game to be found.")
    if eventh ==5:
        injury = random.randint(1,3)
        if injury ==1:
            print("You were injured trying to bring down an animal! You now have a fleshwound!")
            r.fleshwound = True
            ringbearer()
        else:
            print("Your companion, "+(str(companion_name))+", was injured trying to bring down an animal! They now have a fleshwound!")
            g.fleshwound = True
            gardener()
            
def rest():
    print("\n")
    f.day +=1
    f.food = f.food - 1 - len(f.companions) - f.ponies
    f.water = f.water - 1 - len(f.companions) - f.ponies
    eventr = random.randint(1,3)
    if eventr ==1 or eventr ==2:
        if r.fleshwound == True or g.fleshwound == True:
            print("You've rested and tended to your injuries. None of your party have fleshwounds.")
            r.fleshwound = False
            g.fleshwound = False
            if r.RingMad == True :
                print("During your rest, your companions were able to talk some sense into you. The corruption of the ring seems to have passed for now.")
                r.RingMad = False
            if r.LazyHobbit == True or g.LazyHobbit == True:
                print("Given a day to laze around, the hobbits appear to be cured of their laziness.")
                r.LazyHobbit = False
                g.LazyHobbit = False
            else:
                print("Your party is fully rested")
    else:
            print("Your party takes the day to rest, but the elements prevent you from feeling re-energized.")
            
def helpchoices():
    print("\n")
    print("Travel: make progress on your journey. Consuming food and water based on the size of your party. Ponies can help you travel faster.")
    print("Forage: gather food and water to sustain your party.")
    print("Hunt: hunt nearby creatures for increased food. Provides more food than foraging, but does not provide water.")
    print("Rest: take one day to rest your party, with the potential to heal injuries and detrimental status effects.")
    print("\n")
    
def quit_check():
    check = input("are you sure you want to quit? (y/n): ")
    if check =="y" or check =="Y":
        print("...One does not simply walk into Mordor...")
        quit()
    else:
        print("And so we continue on our journey.")
        
        
def deathcheck():
    if f.food == 0 or f.water == 0:
        print("You have run out of resources. You cannot possibly go on.")
        r.alive == False
        ringbearer()

#Travel marker for chapter 1
def trav1():
    print("\n")
    print("The Shire ---------> Bree")
    init_stat()
    while  1415 < f.miles <=1535:
        options1()
    else:
        chap2()

#Travel options for chapter 1
def options1():
    print("what would you like to do?")
    select = input("travel, forage, hunt, rest, help, quit: ")
    if select == "travel":
        progress()
        trav1()
    elif select == "forage":
        forage()
        trav1()
    elif select == "hunt":
        hunt()
        trav1()
    elif select == "rest":
        print("\n")
        print("Lazy hobbits, we've barely gotten started!")
        rest()
        trav1()
    elif select =="help":
        helpchoices()
    elif select=="quit":
        quit_check()
    else:
        print("Please check your spelling and try again.")
        select = input("travel, forage, hunt, rest, help, quit: ")
            
#Chapter 2 text/story
def chap2():
    print("\n")
    print("On the road to Bree you find your friends Pippin and Merry stealing vegetables from Farmer Maggot's fields.")
    time.sleep(1)
    print("They join you on your journey to Bree, bringing the vegetables they have found with them.")
    f.food += 50
    f.companions.append("Pippin")
    f.companions.append("Merry")
    time.sleep(2)
    print("\n")
    print("Pippin and Merry and joined the party.")
    print("\n")
    init_stat()
    print("\n")
    time.sleep(2)
    print("As you continue toward Bree your party is pursued by mysterious black riders.")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("Fortunately you are able to hide from these dangerous riders and make it to the Inn of the Prancing Pony to meet Gandalf.")
    time.sleep(5)
    print("\n")
    print("\n")
    print("   _____,,;;;`;   The Inn     ;';;;,,_____")
    print(",~(  )  , )~~\|    of the     |/~~( ,  (  )~;")
    print("' / / --`--,      Prancing       .--'-- \ \ `")
    print(" /  \    | '        Pony         ` |    /  |")
    print("\n")
    time.sleep(3)
    print("Unfortunately, Gandalf is unable to meet you in Bree,")
    print("however, you do encounter a ranger by the name of Strider.")
    print("Your part leaves with Strider to make their way to Rivendell")
    print("\n")
    print("Strider joins the party. Bringing his own weapons and rations.")
    f.companions.append("Strider")
    f.food += 30
    f.weapons += 3
    f.ponies += 1
    trav2()

#travel for chapter 2
def trav2():
    print("\n")
    print("Bree ----------> Rivendell")
    init_stat()
    while 1320 < f.miles <=1535:
        options2()
    else:
        chap3()
        
    #Slightly modified text and options for chapter 2    
def options2():
    print("\n")
    print("what would you like to do?")
    select = input("travel, forage, hunt, rest, help, quit: ")
    if select == "travel":
        progress()
        trav2()
    if select == "forage":
        forage()
        trav2()
    if select == "hunt":
        print("\n")
        print("Strider grabs his bow and leaves the camp to hunt.")
        hunt()
        trav2()
    if select == "rest":
        print("\n")
        print("As the hobbits sit down to second breakfast, Strider stairs at you in disbelief.")
        print("'What are you doing??'")
        print("\n")
        time.sleep(2)
        print("We'd better get back on the road.")
        rest()
        trav2()
    if select=="help":
        helpchoices()
    if select =="quit":
        quit_check()        
        
        
#Chapter 3 text/story
def chap3():
    print("\n")
    print("As you make your journey to Rivendell, you are waylayed by the Nazgul.")
    time.sleep(1)
    print("\n")
    print("Oh no! "+(str(player_name))+" is stabbed by their leader.")
    print("\n")
    print("       .---.")
    print("       |---|")
    print("       |---|")
    print("       |---|")
    print("   .---^ - ^---.")
    print("   :___________:")
    print("      |  |//")
    print("      |  |//|")
    print("      |  |//|")
    print("      |  |//|")
    print("      |  |//|")
    print("      |  |//|")
    print("      |  |.-|")
    print("      |.-'**|")
    print("       \***/")
    print("        \*/")
    print("         V")
    print("\n")
    time.sleep(1)
    print("The elf, Arwen, appears. She offers aid, and hurries the party on to Rivendell.")
    print("\n")
    print("Arwen has joined your party. She brings her horse, weapons, and supplies.")
    f.companions.append("Arwen")
    f.food += 30
    f.water += 30
    f.ponies += 1
    trav3()

def trav3():
    print("\n")
    print("Weathertop ----------> Rivendell")
    init_stat()
    while 1067 < f.miles <=1320:
        options3()
    else:
        chap4()

def options3():
    print("PLACEHOLDER")
    quit()


main()
