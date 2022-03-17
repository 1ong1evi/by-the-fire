

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
        return "You sleep through the cold night, to live another day.\nSafe travels, traveler."


main()
