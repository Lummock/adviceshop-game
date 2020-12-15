import os
import time
from random import choice, randint
from colored import *


logo = fg(7) + """                                           ____________________________________________________
                                          |    _   _____   _____ ___ ___   ___ _  _  ___  ___  |
                                          |   /_\ |   \ \ / /_ _/ __| __| / __| || |/ _ \| _ \ |
                                          |  / _ \| |) \ V / | | (__| _|  \__ \ __ | (_) |  _/ |
                                          | /_/ \_\___/ \_/ |___\___|___| |___/_||_|\___/|_|   |
                                          |____________________________________________________|"""

personage1 = fg(7) + """
                                                                    ______
                                                                   /      \ 
                                                                  /        \ 
                                                                 |          |
                                                                 |          |
                                                                  \        /
                                                                   \      /
                                                                    |    |
                                                                    |    |
                                                                   /      \ 
                                                                  /        \ """

personage2 = fg(7) + """
                                                                   _________
                                                                  /         \ 
                                                                 /           \ 
                                                                |             |
                                                                |             |
                                                                 \           /
                                                                  \         /
                                                                   |       |
                                                                   |       |
                                                                  /         \ 
                                                                 /           \ """

personage3 = fg(7) + """
                                                                      ___
                                                                     /   \ 
                                                                    /     \ 
                                                                   |       |
                                                                   |       |
                                                                    \     /
                                                                     \   /
                                                                      | |
                                                                      | |
                                                                     /   \ 
                                                                    /     \ """

personage4 = fg(7) + """
                                                                     /__\/\ 
                                                                    /      \ 
                                                                   /       / 
                                                                  |        \ 
                                                                  |       _|
                                                                   \     /
                                                                    \   /
                                                                     \ \ 
                                                                      \ \ 
                                                                     /   \ 
                                                                    /     \ """

personage5 = fg(7) + """
                                                                      _____|
                                                                     /      | 
                                                                    /       | 
                                                                   |        | 
                                                                   |       |
                                                                    \     /
                                                                     \   /
                                                                      / /
                                                                      \ \ 
                                                                     /   \ 
                                                                    /     \ """

line = """ ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"""

kek = [personage1, personage2, personage3, personage4, personage5]

line1 = "Should I get a dog?"
line2 = "Should I go to the playground?"
line3 = "Must I get Ice Cream?"
line4 = "Ought I buy vodka?"
line5 = "Should I blow up the preschool?"
line6 = "Should I put down my dog?"
line7 = "Im getting arrested. Should I call my friend?"
line8 = "Should I kill myself?"
line9 = "Do I need my medications?"
line10 = "Do I need to buy nachos?"
line11 = "Should I ask rhetorical questions?"
line12 = "Kill. Kill. Kill."
line13 = "Yes or No: Killing babies."
line14 = "Should I get weed?"
line15 = "Should I buy a gravel plot?"
line16 = "Must I buy a gun?"
line17 = "Pawefchesy, eifhHfe8?"
line18 = "Please, should I sell my farm?"
line19 = "Should I plug the hole?"

def randvoice():
    c = randint(1, 253)
    print(fg(c))
    r = randint(1, 19)
    if r == 1:
        print(line1)
        liney = "True, I deserve food."
        linen = "Yeah... I deserve to be alone."
    elif r == 2:
        print(line2)
        liney = "Yeah, the basement kids have had enough free time."
        linen = "Yeah, 4 is old enough to go out on your own."
    elif r == 3:
        print(line3)
        liney = "Ol' Cannibal Cream IS very good... wonder what's in it."
        linen = "I don't deserve to be happy."
    elif r == 4:
        print(line4)
        liney = "My kid's birthday needs a party drink."
        linen = "I should buy meth instead."
    elif r == 5:
        print(line5)
        liney = "Kaboom? Yes, KABOOM! " + '\033[1m' + "KABOOOOOOOOOOM!" + '\033[0m'
        linen = "I should let off mustard gas instead."
    elif r == 6:
        print(line6)
        liney = "Ol' rusty should know not to chew socks by now!"
        linen = "Im sure eldritch tentacles are normal. Unrelated, but have you seen my kids?"
    elif r == 7:
        print(line7)
        liney = "Yeah, Ted Bundy should know what to do!"
        linen = "Fake moustaches are a sign of real police, right?"
    elif r == 8:
        print(line8)
        liney = "I don't matter."
        linen = "Myself Rogers may be a child murderer, but we have a strict no-kill policy."
    elif r == 9:
        print(line9)
        liney = "CYANIDE sounds sciency."
        linen = "I need to listen to the voice in my head. And the other one."
    elif r == 10:
        print(line10)
        liney = "Im 9746 pounds, but im gonna add 1 more!"
        linen = "My kid, Nachos, should vibe with their kidnapper anyway."
    elif r == 11:
        print(line11)
        liney = "That was rhetorical."
        linen = "That was rhetorical."
    elif r == 12:
        print(line12)
        liney = "KILL. KILL. KILL. KILL."
        linen = "Ok."
    elif r == 13:
        print(line13)
        liney = "Whee! Time to go to the children's hospital!"
        linen = "A dog AND a baby with tentacles isnt.. weird.."
    elif r == 14:
        print(line14)
        liney = "I'll plant it at my bosses place."
        linen = "My medical condition should be ok."
    elif r == 15:
        print(line15)
        liney = "Only 4 bil for 9 acres? What a steal!"
        linen = "I'm sure the family gravel heirloom isn't important."
    elif r == 16:
        print(line16)
        liney = "Im gonna reenact DOOM at the children's hospital!"
        linen = "Shooting that guy who is burning our city is unethical!"
    elif r == 17:
        print(line17)
        liney = "yeugfyjk DBALDhwaIOd?"
        linen = "GDYWUKD dagDADKhGYkud !"
    elif r == 18:
        print(line18)
        liney = "Goodbye, kids!"
        linen = "Nightmare chickens are fine. Anyway, have you seen my kids?"
    elif r == 19:
        print(line19)
        liney = "I'll fuckin plug my mouth with bullets!"
        linen = "The dam can wait, I want Ice Cream!"
    i = input("(Y/N): ")
    if i.lower() in ("y", "yes"):
        print(liney)
    elif i.lower() in ("n", "no"):
        print(linen)
while True:
    while True:
        os.system('clear')
        print(logo)
        print(choice(kek))
        print(line)
        randvoice()
        input("")
