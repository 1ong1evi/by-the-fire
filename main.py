import random
# intro
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
# Intro to the story & first question
investigate = input("Do you go checkout the noise? (y/n) ")
if investigate == "n":
    # no responds with safe travels
    print("\nYou sleep through the cold night, to live another day.\nSafe travels, traveler.")
    # sneak question rush in y/n
sneak = input("\nYou are approaching the sound. Do you rush in? (y/n) ")
if sneak == "n":
    # first sight of strange figure
    strange_figure = input(
        "\nYou see a strange animal. Tall and standing on its hind legs.\n Do you continue to sneak to get a better look? (y/n) ")
    if strange_figure == "n":
        # logic if you said no to the get a better look "safe travels"
        print("\nWeary of your travels you decide to head back to camp.\nYou sleep through the cold night, to live another day.\nSafe travels, traveler.")
    elif strange_figure == "y":
        # sneak attack has a 50% chance to hit text to the user
        sneak_attack = input("""
You see a deformed animal with orange-red eyes. Remembering of past conversations of the previous
the village you know this a skinwalker. Due to you sneaking you have a chance to kill it. 
You have a 50% chance do you take it? (y/n) """)
        if sneak_attack == "n":
            # "no" continues with the safe travels text
            print("\nUneasy about your chances you decide to sneak back to camp.\nYou sleep through the cold night, to live another day.\nSafe travels, traveler.")
        elif sneak_attack == "y":
            # attack sequence
            # death sequence
            one = "\nThe closer you get the more you second guess yourself.\nYou get one step away when you step on a leaf. The skinwalker turns around\nand gives out a loud screech, you try to swing at it with your sword but you miss. It slashes at your throat.\nYou try to stay upright but you fall to your knees. Then to the floor of \nthe forest. You try to scream but it was only a thought"
            # kill the skin walker sequence
            two = "\nThe closer you get the more you second guess yourself.\nYou pull out your knife that was dipped in white ash. You smell the stench\nof death the skinwalker reeks of. In an instances you slit the skinwalker's throat. It drops to its knees without\na peep. You drag the it back to your camp."
            seq = [two, one]
            # chooses between two endings
            print(random.choice(seq))
elif sneak == "y":
    # logic for death
    print("""\nYou rush in to only be met by a deformed animal with orange-red eyes.
You turn your back to it while running back to your camp.
That's when you feel its sharp claws puncturing into both of your shoulders.
You try to stay upright but you fall to your knees. Then to the floor of
the forest. You try to scream but it was only a thought. 
""")
# might make shorter
