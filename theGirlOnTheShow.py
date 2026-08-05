# The Girl On The Late Night Show

def playGame():
    # Declare Variables

    userName = ""

    userAge = 0

    trustedFam = ""

    friendName = ""

    choice = ""

    conMessage = "\nThis action will have consequences...\n" # This action will have consequences...

    genderOfFam = ""

    # Define Functions

    conMessage = "\nThis action will have consequences...\n"

    def StoryContinue(choice, story, question, choice_1="", story_1="", choice_2="", story_2=""):
        print(conMessage)

        # Ask the question and save what they type into 'choice'
        choice = input(question)

        # Check which path they chose and print the matching story outcome
        if choice == choice_1:
            print(story_1)
        elif choice == choice_2:
            print(story_2)
        elif story:
            print(story)

        return choice

    # Ask for Information

    userName = input("What will be your Character's name?: ")

    userAge = int(input("How old are you?"))

    trustedFam = input("Which Family Member is your closest?\n\
 Mom (M)\n Father (F) \n Aunt (A)\n Uncle (U)\n Sister (S)\n Brother (B)\n Cousin (C)\n")
    if trustedFam == "M":
        trustedFam = "Mom"
        genderOfFam = "she"

    elif trustedFam == "F":
        trustedFam = "Father"
        genderOfFam = "he"

    elif trustedFam == "A":
        trustedFam = "Aunt"
        genderOfFam = "she"

    elif trustedFam == "U":
        trustedFam = "Uncle"
        genderOfFam = "he"

    elif trustedFam == "S":
        trustedFam = "Sister"
        genderOfFam = "she"

    elif trustedFam == "B":
        trustedFam = "Brother"
        genderOfFam = "he"

    elif trustedFam == "C":
        trustedFam = "Cousin"
        genderOfFam = "they"
    # start/introduce the story

    print("You're a host of a late-night call show. \
\nYou rarely get actual responses. \
\nMost of the time they are prank calls. \
\nElise a local girl in the city has been a usual caller for a week.\
\nThe gimmick of the day was: \"What is your strangest story\" \
\nElise called and started describing a very \
\nfamiliar murder story that had happened recently \
\nand that many details haven\'t been released...what do you do?")

    # Choice Making --- >

    print("You have 3 choices:\n\n Hang Up (\"H\")\n Trace the Call (\"T\")\n Just listen (\"J\")\n")
    choice = StoryContinue(choice, "", "What will you do?: ")
    # Chain of H
    if choice == "H" :
        # Hang Up

        print(conMessage)
        print("\nYou hang up immediately when you got nervous\
\nand play it off as if it were her \
fault. \nShe is annoyed.")
        choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Go to a restuarant to eat (R) \n\
Go home (H)\nEnter Here:... ")
        # Go to a restuarant to eat
        if choice == "R":
            print(conMessage)
            print("You go to the restaurant and eat your favorite food \n\
you think it tastes weird but you shake it \noff and deal with it. Now your thirsty \n\
so you ask your waiter for water but she \nsuggests a new drink that was now on the menu")
            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Just Water (W) \n\
Get a New Drink (N)\nEnter here:... ")
            # Just Water
            if choice == "W":
                print(conMessage)
                print("You get water and the next day the new drink reportedly got recalled \n\
                      because 129 people got sick 180 died and 42 survived but still fainted. ")
                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Take a walk (T) \n\
Go to Your Friend's House (F)\nEnter here:... ")
                # Take a walk
                if choice == "T":
                    print(conMessage)
                    print("You have a good rest of your day and you decide it's a good day to\n\
                    also take a good health walk in the city to appreciate nature ")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Go right (R) \n\
Go left (L)\nEnter here:... ")
                    # Go right
                    if choice == "R":
                        print(conMessage)
                        print("You continued walking in your route and you witnessed a car speeding like crazy \n\
                              and it hit a person and the person died instantly. You were traumatized.")
                    # Go left
                    elif choice == "L":
                        print(conMessage)
                        print("YWhile you were crossing the road a car was speeding and hit you all\n\
                              you saw was a woman trying to get him to stay alive.")
                        print("You died...")
                # Go to Your Friend's House
                elif choice == "F":
                    print(conMessage)
                    print("You go to your friend's house and you were told that he was killed ")
                    print("You suspect that it was Elise...")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Go Home and Cry (C) \n\
Get Revenge (R)\nEnter here:... ")
                    # Go Home and Cry
                    if choice == "C":
                        print(conMessage)
                        print("You go home and cry and you never figured out the mystery")
                        endingQ = StoryContinue(choice, "", "Game Ended -- Who Killed Your Friend?: Elise (E) Other (O) \n\
Enter here:... ")
                    # Get Revenge
                    elif choice == "R":
                        print(conMessage)
                        print("You decide to get revenge on Elise...After a few days of planning\
                              you find that she didnt kill him...? Apparently she is just a normal Youtuber\
                              that does horror pranks...but what about your friend? Who killed him?\
                              You find that he was killed from poisoning from that drink...")
                        print("")

            # Get a New Drink
            elif choice == "N":
                print(conMessage)
                print("You get the new drink but then you feel weird...\n\
                      the ice cubes in the drink are on the bottom you realize that the drink isnt safe \n\
                      you try driving to the hospital immediately but you get dizzy and\n\
                      you get into a bad car crash.  ")
                print("You died...")
                print("Now you are a ghost...your last wish was to find out who the killer was...")

        # Go Home
        elif choice == "H":
            print(conMessage)
            print("You go try going home in your car but you can see somebody following you...")
            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Ignore it (I) \n\
Tell them to Stop (T)\nEnter here:... ")
            # Ignore it
            if choice == "I":
                print(conMessage)
                print("You ignore it and when you get home a \n\
person with a hoodie starts chasing you\n")

                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Protect Yourself (P) \n\
Run (R)\nEnter here:... ")
                # Protect Yourself
                if choice == "P":
                    print(conMessage)
                    print("You try to fight the person.\
                           The person was frightened and ran away")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Let them Run Away (L) \n\
Follow Them and Try to Catch Them (F)\nEnter here:... ")
                    # Let them Run Away
                    if choice == "L":
                        print(conMessage)
                        print("You let them run away, you successfully protected youselfy and you never figured out the mystery")

                    # Follow Them and Try to Catch Them
                    elif choice == "F":
                        print(conMessage)
                        print("As you try to catch them the person turns you into the bad guy and reports you to the police and you get arrested and you never figured out the mystery")
                # Run
                if choice == "R":
                    print(conMessage)
                    print("You start running but the person grabs you but you fall face first onto the\n\
concret floor and when you wake up you find yourself in the hospital.")
                    input("Game Ended -- Who Killed Your Friend?: \nElise (E) \nAndrew (A) \nOther (O) \nEnter here:... ")
                    if choice == "E":
                        print("You chose Elise...but she was just a normal Youtuber that does horror pranks...\
                              So whose the murderer?...")
                        print("")
                    elif choice == "A":
                        print("You chose Andrew...Yes! ANDREW! Why and How was he the murderer? You ask?")

                        print("Andrew was Elise's bsf and he used that to his advantage and knew that\n\
he wouldn't be a suspect if he was included in her horror pranks. Andrew left those\n\
blood marks on the phone booth knowing that Elise would be the suspect...but close by to that photo booth there was an\n\
abandoned house and in there there was all of his plans and information...\n\
There it was...all of the information proved that he was the murderer.")


            # Tell them to Stop
            elif choice == "T":
                print(conMessage)
                print("You stop the car and the car just passes \n\
by as if it were never following you...")
                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Track Them Down (T) \n\
Tell Someone (S)\nEnter here:... ")
                # Tell Someone
                if choice == "S":
                    print(conMessage)
                    print("You tell", trustedFam, "about everything that happened but" ,genderOfFam , "\
didn't care")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Just Go On with Life (J) \n\
Tell Someone else (S)\nEnter here:... ")
                    # Just Go On with Life
                    if choice == "J":
                        print(conMessage)
                        print("Since your family didn't care you decided that you shouldn't either so you go on with life and you never figured out the mystery ")
                    # Tell Someone else
                    if choice == "S":
                        print(conMessage)
                        print("You tell your friend and they told you to report it to the police but you didn't want to because you were scared")
                        print("Since your family didn't care you decided that you shouldn't either so you go on with life and you never figured out the mystery ")

                # Track them Down
                elif choice == "T":
                    print("You memorize their license plate number and ask the police to\n\
                          track it down because of your situation but they tell you they cant do that... ")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Yell at The Police (P) \n\
Give Up (R)\nEnter here:... ")
                    if choice == "P":
                        print(conMessage)
                        print("You yell at the police and they tell you to calm down and \n\
                              that they will try to help you but they can't do much")
                        print("Later that night you get a call from the police saying they found nothing but a \n\
                              random note that said \"You should have listened to her\"")
                        print("After that the police say they can't find anything else and the have to close the case.\
                               You never figured out the mystery.")

                    elif choice == "R":
                        print(conMessage)
                        print("You give up and you never figured out the mystery...")

    # Chain of T
    elif choice == "T":

        # Trace the Call
        print(conMessage)
        print("You listen to her while you trace the call\
\nand you secretly call the police while finding \
\nthe phone booth she called from")

        choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Go Home (G) \n\
Take a Look in the Phone Booth (L)\nEnter here:... ")

        # Take a Look in the Phone Booth
        if choice == "L":
            print(conMessage)
            print("You take a look but nobody is there? You also try looking\n\
around and you see a woman with a hoodie over her head.")
            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Approach Her (A) \n\
Go Home (G)\nEnter here:... ")
            # Approach Her
            if choice == "A":
                print(conMessage)
                print("You approach her carefully but she notices you and takes off\n\
running into the crowd. You chase after her but lose her and you\n\
never figured out the mystery...")
            # Go Home (falls into the same "followed home" thread below)
            elif choice == "G":
                choice = "G"

        # Go Home
        if choice == "G":
            print(conMessage)
            print("You go try going home in your car but you can see somebody following you...")
            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Stay in the Car (S) \n\
Try Investigating by Yourself (I)\nEnter here:... ")
            # Stay in the Car
            if choice == "S":
                print(conMessage)
                print("The police come and they found that this phone booth hasn't\n\
been operating for a decade.")
                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Tell the Police to Keep Investigating (K) \n\
Tell Them not to Bother Investigating (N)\nEnter here:... ")
                # Tell the Police to Keep Investigating
                if choice == "K":
                    print(conMessage)
                    print("The police continue investigating and after a while the\n\
police officers get tired of looking and give up.")
                # Tell Them not to Bother Investigating
                elif choice == "N":
                    print(conMessage)
                    print("The police leave and you suddenly hear something in your car,\n\
you take a look and Elise left a note")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Ignore the Note, it's Nothing but an Empty Threat (I) \n\
Read the Note (R)\nEnter here:... ")
                    # Ignore the Note
                    if choice == "I":
                        print(conMessage)
                        print("You ignore the note and you find yourself bored and have\n\
nothing new to do. After a while you started to forget about\n\
Elise and you never figure out the mystery...")
                    # Read the Note
                    elif choice == "R":
                        print(conMessage)
                        print("The note says: \"You wont find me...I'll find you first\"")
                        choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Report this Note (R) \n\
Don't Report (D)\nEnter here:... ")
                        # Report this Note
                        if choice == "R":
                            print(conMessage)
                            print("You go to the police station and they investigate it but\n\
still nothing and they say they found nothing from this note.")
                        # Don't Report
                        elif choice == "D":
                            print(conMessage)
                            print("Day after day you keep getting more threatening notes and one\n\
day you see her in a hoodie while you were walking home from\n\
work. She starts following you but before you can call the\n\
police she already grabbed your hand...")
                            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Try to Let Go and Run (R) \n\
Try to Talk to Her (T)\nEnter here:... ")
                            # Try to Let Go and Run
                            if choice == "R":
                                print(conMessage)
                                print("You start running but the person grabs you but you fall face\n\
first onto the concret floor and when you wake up you find\n\
yourself in the hospital.")
                                input("Game Ended -- Who Killed Your Friend?: \nElise (E) \nAndrew (A) \nOther (O) \nEnter here:... ")
                                if choice == "E":
                                    print("You chose Elise...but she was just a normal Youtuber that does horror pranks...\
                                          So whose the murderer?...")
                                    print("")
                                elif choice == "A":
                                    print("You chose Andrew...Yes! ANDREW! Why and How was he the murderer? You ask?")
                                    print("Andrew was Elise's bsf and he used that to his advantage and knew that\n\
he wouldn't be a suspect if he was included in her horror pranks. Andrew left those\n\
blood marks on the phone booth knowing that Elise would be the suspect...but close by to that photo booth there was an\n\
abandoned house and in there there was all of his plans and information...\n\
There it was...all of the information proved that he was the murderer.")
                            # Try to Talk to Her
                            elif choice == "T":
                                print(conMessage)
                                print("You try talking to her and she's actually not a bad person.\n\
She reveals that she was a Youtuber that does scary pranks and\n\
she didnt mean for it to get this serious.")
                                print("You slip out of her grip and fall on the floor she helps you\n\
up and she tells you that she's not the murderer and she's just\n\
a Youtuber that does scary pranks and she didnt mean for it to\n\
get this serious.")
                                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Ask for Advice Online (A) \n\
Just Go Home (G)\nEnter here:... ")
                                # Ask for Advice Online
                                if choice == "A":
                                    print(conMessage)
                                    print("You gain thousands of followers and they tell you a variety\n\
of things to do but you shortened it to 2...")
                                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Explore the Phone Booth (E) \n\
Get Advice from Social Media Again (S)\nEnter here:... ")
                                    # Explore the Phone Booth
                                    if choice == "E":
                                        print(conMessage)
                                        print("You explore it for yourself but then you find that the phone\n\
booth has a new note on it. You read it and it says \"Behind you.\"")
                                        choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Look Behind You (L) \n\
Ignore it and Walk Away (I)\nEnter here:... ")
                                        # Look Behind You
                                        if choice == "L":
                                            print(conMessage)
                                            print("You look behind you and realize that a girl in a hoodie is\n\
there and she starts walking to you. You have no escape and you\n\
cant move in fear. She knocks you out and you die.")
                                        # Ignore it and Walk Away
                                        elif choice == "I":
                                            print(conMessage)
                                            print("You survived but you give up trying to figure the mystery of\n\
Elise because it brung you all this trouble.")
                                    # Get Advice from Social Media Again
                                    elif choice == "S":
                                        print(conMessage)
                                        print("People donate money to you and you go back to having a\n\
normal life.")
                                # Just Go Home
                                elif choice == "G":
                                    print(conMessage)
                                    print("You survived! You go home and try to move on with your\n\
life, but you never figured out the mystery...")
            # Try Investigating by Yourself
            elif choice == "I":
                print(conMessage)
                print("You try investigating by yourself and you find that the phone\n\
booth works occasionally but then you find that Elise is a\n\
Youtuber and she has a video about the exact same prank she did\n\
on you...")
                print("You find yourself bored and have nothing new to do. After a\n\
while you started to forget about Elise and you never figure out\n\
the mystery...")

    # Chain of J
    elif choice == "J":

        # Just Listen
        print(conMessage)
        print("She finishes and she thanks him for \n\
letting her on the show and hangs up")

        choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
You Go Home and Deal with guilt (G) \n\
Go to the Police Station (P)\nEnter here:... ")
        # Go Home and Deal with guilt
        if choice == "G":
            print(conMessage)
            print("You go home and you are bored...you keep thinking about that call.\n\
                  You are tempted to tell the police but you don't in fear.")
            print("You go to sleep and the next day you wake up\n\
                   become curios if she really was the murderer")
            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Do Nothing (N) \n\
Investigate Secretly (I)\nEnter here:... ")
            # Do Nothing
            if choice == "N":
                print(conMessage)
                print("You do nothing and at work people start talking\n\
                      about the mystery and you start to feel guilty \
                      for not doing anything about it")
                print("After a few days the whole city knows about it")
                print("You get a call from an Unknown Number")
                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Ignore the Phone Call (I) \n\
Answer the Phone Call (A)\nEnter here:... ")
                # Ingrore the Phone Call
                if choice == "I":
                    print(conMessage)
                    print("You ignore the phone call and you continue to live a normal life...but it never left your mind...")
                # Answer the Phone Call
                elif choice == "A":
                    print(conMessage)
                    print("You answer the call and a shaky voice whispers, \"You should\n\
have listened to her...\" before the line goes dead.")
                    print("Unsettled, you try to trace the number back but it comes back\n\
as disconnected. You never figured out the mystery...")
            # Investigate Secretly
            elif choice == "I":
                print(conMessage)
                print("You investigate secretly. Everyday after work\n\
you go to the phone booth Elise called from...you find blood on the phone booth")
                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Continue Investigating (C) \n\
Stop Investigating (S)\nEnter here:... ")
                # Continue Investigating
                if choice == "C":
                    print(conMessage)
                    print("You continue investigating and you find a note that says\n\
                          \"Come find me\"", userName)
                    print("You go home and you are scared and\n\
                          now youre even more motivated to find out who the murderer is")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Go to the neighboor hood that she called from... (G) \n\
Reasearch more (R)\nEnter here:... ")
                    # Go to the neighborhood
                    if choice == "G":
                        print(conMessage)
                        print("You go to the neighborhood and you find that there is an abandoned house")
                        choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Explore the House (E) \n\
Go Home and Forget About It (F)\nEnter here:... ")
                        # Explore the House
                        if choice == "E":
                            print(conMessage)
                            print("You explore the house and inside you find blueprints, notes,\n\
and photos - all of Andrew's plans laid out in detail. There it\n\
was...all of the information proved that Andrew was the murderer,\n\
using Elise's horror-prank persona as the perfect cover.")
                        # Go Home and Forget About It
                        elif choice == "F":
                            print(conMessage)
                            print("You go home and you find your house completly empty.\n\
Everything is gone... You also find that all your money is gone...")
                            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Become Homeless (B) \n\
Ask for Advice Online (A)\nEnter here:... ")
                            # Become Homeless
                            if choice == "B":
                                print(conMessage)
                                print("You become homeless and now you sit outside asking for\n\
money...you never figured out the mystery...")
                            # Ask for Advice Online
                            elif choice == "A":
                                print(conMessage)
                                print("You ask for advice online and thousands of people tell you\n\
what to do, but none of it brings your money or your answers\n\
back. You never figured out the mystery...")
                    # Research more
                    elif choice == "R":
                        print(conMessage)
                        print("You research more and you find that her best friend was the murderer.")
                        print("Andrew, her best friend, had used her horror-prank videos as\n\
the perfect cover the whole time.")
                # Stop Investigating
                elif choice == "S":
                    print(conMessage)
                    print("You stop investigating and you never figured out the mystery...The police never figured out either")
                    choice = StoryContinue(choice, "", "You Failed...Would you like to know who the murderer was? (Y/N)")
                    if choice == "Y":
                        print("The murderer was a guy named Andrew. Elise's best friend.")
                    elif choice == "N":
                        print("You chose not to know...Good Choice.")
            # Go to the Police Station
            elif choice == "P":
                print(conMessage)
                print("You go to the police station and report your findings.")
        # Go to the Police Station (from the top of the J chain)
        elif choice == "P":
            print(conMessage)
            print("You go to the police station and you report the girl. They\n\
ask for the recordings or any proof.")
            choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Give Them the Recordings (G) \n\
Tell Them You Don't Have Any (D)\nEnter here:... ")
            # Give Them the Recordings
            if choice == "G":
                print(conMessage)
                print("You give it to them but while looking for it in the system\n\
it suddenly goes missing?")
                choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Tell Them it's Gone (T) \n\
Keep Looking (K)\nEnter here:... ")
                # Tell Them it's Gone
                if choice == "T":
                    print(conMessage)
                    print("You tell them the recordings are gone and they say they can't\n\
do much without proof. They close the case and you never\n\
figured out the mystery...")
                # Keep Looking
                elif choice == "K":
                    print(conMessage)
                    print("You keep looking but you find nothing but a recording you\n\
didnt take but sounds like you. The recording was explaining\n\
the details of that murder but you never said that. The police\n\
find it and arrest you.")
                    choice = StoryContinue(choice, "", "Now you have 2 choices...\n\
Try to Tell Them it's Not Real (T) \n\
Give Up and Go to Jail (G)\nEnter here:... ")
                    # Try to Tell Them it's Not Real
                    if choice == "T":
                        print(conMessage)
                        print("They don't believe you but they look into it anyway. They\n\
find that it was Generated - a fake recording planted to frame\n\
you. You are released, but you never fully figure out who set\n\
you up...")
                    # Give Up and Go to Jail
                    elif choice == "G":
                        print(conMessage)
                        print("You go to prison for the rest of your life for a murder you never did.")
            # Tell Them You Don't Have Any
            elif choice == "D":
                print(conMessage)
                print("You tell them you don't have any proof and they say there's\n\
nothing they can do without it. They close the case and you\n\
never figured out the mystery...")


# Main Loop -- allows the player to replay the game

playAgain = "Y"
while playAgain == "Y":
    playGame()
    playAgain = input("\nYou Failed...Replay? Y/N: ").upper()

print("\nThanks for playing The Girl On The Late Night Show!")