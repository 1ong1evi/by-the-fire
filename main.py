import random


def main():
    print("""
  ____          _   _            ______ _          
 |  _ \        | | | |          |  ____(_)         
 | |_) |_   _  | |_| |__   ___  | |__   _ _ __ ___ 
 |  _ <| | | | | __| '_ \ / _ \ |  __| | | '__/ _ |
 | |_) | |_| | | |_| | | |  __/ | |    | | | |  __/
 |____/ \__, |  \__|_| |_|\___| |_|    |_|_|  \___|
         __/ |                                     
        |___/                                      
    """)
    print("---------------------------------------------------")
    print("Welcome Adventurer!")
    print("---------------------------------------------------")
    print("""You have been traveling for hours on end. 
Getting late, you decide to set up camp. Before falling asleep, 
you made a fire to cook up some dried meat you packed. 
Then all of sudden halfway through cooking it, you hear a noise in the woods. 
    """)

    investigate = input("Do you go checkout the noise? (y/n) ")
    if investigate == "n":
        print("\nYou sleep through the cold night, to live another day.\nSafe travels, traveler.")
    sneak = input("\nYou are approaching the sound. Do you rush in? (y/n) ")
    if sneak == "n":
        strange_figure = input(
            "You see a strange animal. Tall and standing on its hind legs.\n Do you continue to sneak to get a better look? (y/n)")
    print("""\nYou rush in to only be met by a deformed animal with orange-red eyes.
You turn your back to it while running back to your camp.
That's when you feel sharp claws puncturing into both your shoulders.
You try to stay upright but you fall to your knees. Then to the floor of
the forest. You try to scream but it was only a thought. 
""")


main()
