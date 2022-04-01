import time
import random
import words
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a wide open field "
                "surrounded by mountains. ")
    print_pause("On your right is what appears to be a dark cave. ")
    print_pause("And on your left is a beautiful cottage. ")
    print_pause("In your hand you hold your old, but rather blunt, dagger. ")
    print_pause("A farmer walks along and tells you to be careful "
                "of the cottage for a fearsome beast dwells inside it.")
    print_pause("You thank the farmer for his warning and make a decision.\n")


def cave(items):
    print_pause("You walk to the gaping mouth of the cave. ")
    print_pause("And timidly peer inside the darkness. ")
    print_pause("You strike a match and look around. ")

    if "Sword of Oogaroth" in items:
        print_pause("There was nothing of interest. "
                    "It seems you have what you were looking for.")
    else:
        print_pause("There it was! The mystical Sword of Oogaroth! "
                    "You quickly sheath your old dagger and take the sword.")
        items.append("Sword of Oogaroth")
    print_pause("You leave the cave and go back to the field.\n")
    choice(items)


def cottage(items):
    print_pause("You cautiously approach the cottage and knock on the door.")
    print_pause(game_boss(words.nouns, words.templates))

    if "Sword of Oogaroth" in items:
        print_pause("Since you got the sword, you are feeling brave. "
                    "You are willing to risk your life to save the people.")
    else:
        print_pause("You feel a little underprepared since all you have "
                    "is a tiny dagger. ")

    while True:
        response = input("Would you like to (1) fight or (2) run away?\n")
        if response == "1":
            print_pause("You ready yourself for the fight of a lifetime.")

            if "Sword of Oogaroth" in items:
                print_pause("You fight bravely and slay the beast!")
                print_pause("The people thank you and throw a feast "
                            "in your honour.")
                items.append("winner")
            else:
                print_pause("You fought bravely, but alas, "
                            "you were no match for the beast.")
                items.append("slain")
            ending(items)
            break
        if response == "2":
            print_pause("you run away as fast as you can back to the field.")
            print_pause("Luckily, the beast does not seem to have "
                        "followed after you.\n")
            choice(items)
            break


def choice(items):
    print_pause("Enter 1 to go to the cave. ")
    print_pause("Enter 2 to go to the cottage. ")
    print_pause("Where would you like to go?")

    while True:
        choice = input('(Please enter 1 or 2)\n')
        if choice == "1":
            cave(items)
            break
        if choice == "2":
            cottage(items)
            break


def ending(items):
    if "slain" in items:
        print_pause("GAME OVER")
    if "winner" in items:
        print_pause("YOU WON")

    while True:
        response = input("Would you like to play again? (y/n)\n")
        if response == "y".lower():
            play()
        if response == "n".lower():
            print_pause("Thank you for playing, please come by again!")
            break


def game_boss(nouns, templates):
    template = random.choice(templates)
    nouns = random.choice(nouns)

    output = []

    index = 0

    while index < len(template):
        if template[index:index+8] == '{{noun}}':
            output.append(nouns)
            index += 8
        else:
            output.append(template[index])
            index += 1
    output = ''.join(output)
    return output


def play():
    items = []
    intro()
    choice(items)


play()
