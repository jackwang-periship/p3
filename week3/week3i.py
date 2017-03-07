'''
Created on Feb 28, 2017

@author: jackwang
'''
from sys import exit


def gold_room():
    print "This room is full of gold. How much do you take?"
    next_move = raw_input("> ")
    if "0" in next_move or "1" in next_move:
        how_much = int(next_move)
    else:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    while True:
        next_move = raw_input("> ")
        if next_move == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next_move == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next_move == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next_move == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next_move = raw_input("> ")

    if "flee" in next_move:
        start()
    elif "head" in next_move:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    next_move = raw_input("> ")
    if next_move == "left":
        bear_room()
    elif next_move == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()

