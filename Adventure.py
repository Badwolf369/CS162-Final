I_am_alive = True

while I_am_alive:

    print("you are walking down a trail.")
    print("you reach a fork in the road.")
    print("which way do you go?")
    Ans1 = input("left(1), right(2), or straight(3)?")

    # Path 1
    if Ans1 == 1:
        print("you turn left.")
        print("you are spotted by a head hunter.")
        print("what do you do?")
        Ans2 = input("do you hide(1), run(2), or attack(3)?")

        # Path 1 / 1 = End 1
        if Ans2 == 1:
            print("you do not hide fast enough and he finds you.")
            print("he then sells your head as a shrunken head.")
            I_am_alive = False

        # Path 1 / 2 = End 2
        elif Ans2 == 2:
            print("you out run him, but he calls for help.")
            print("you are completely surrounded.")
            print(
                "they then catch you and sell your head as a shrunken head."
            )
            I_am_alive = False

        # Path 1 / 3
        else:
            print(
                "you fight him and win but he calls reinforcements."
            )
            print("what do you do?")
            Ans3 = input(
                "do you dig a hole and hide(1), fight(2), or run(3)"
            )

            # Path 1 / 3 / 1 = End 3
            if Ans3 == 1:
                print(
                    "they trample the hole and you can not get out."
                )
                I_am_alive = False

            # Path 1 / 3 / 2 = End 4
            elif Ans3 == 2:
                print("there are to many of them.")
                print("you can not beat them.")
                print(
                    "they catch you and sell your head as a shrunken head."
                )
                I_am_alive = False

            # Path 1 / 3 / 3
            else:
                print("you are able to out run them.")
                print("you go on and continue the trail.")
                print("you see a rainbow.")
                print("what do you do?")
                Ans5 = input(
                    "do you follow it to get gold(1), or just keep walking(2)?"
                )

                # Path 1 / 3 / 3 / 1
                if Ans5 == 1:
                    print("you follow the rainbow.")
                    print("you reach the end of the rainbow")
                    print("you see a pot of gold.")
                    print("you go and get it.")
                    print("you see a unicorn with red eyes.")
                    Ans6 = input(
                        "do you run(1), or just keep going?(2)"
                    )

                # Path 1 / 3 / 3 / 1 / 1
                # if Ans6 == 1:
                # print("the unicorn is a carnivorous unicorn."
                # print("he is to fast for you."
                # print("he catches you and eats you."\
                # I_am_alive = False
                # else:
                # print("the unicorn is a carnivorous unicorn."
                # print("he eats you for trying to stael his gold."
                # I_am_alive = False

    # Path 2
    elif Ans1 == 2:
        print("you turn right")
        print("you see a gem on the ground.")
        print("what do you do?")
        Ans7 = input("do you pick it up(1), or leave it(2)")

        # Path 2 / 1 = End 6
        if Ans7 == 1:
            print("it is the tooth of a giant bronze serpent.")
            print("it was waiting for a good meal.")
            print("it swallows you whole")
            I_am_alive = False

        # Path 2 / 2
        else:
            print("you just keep walking.")
            print("you hear a rumble.")
            print(
                "you look back and find that the gem was the tooth of a giant bronze serpent."
            )
            print("you continue the path")
            print("you see a piece of gold.")
            Ans8 = input(
                "do you pick it up and leave(1), pick it up and look for more(2), or just leave."
            )

            # Path 2 / 2 / 1
            if Ans8 == 1:
                print("you pick it up and keep going.")
                print("you hear a growl.")
                print("you run.")
