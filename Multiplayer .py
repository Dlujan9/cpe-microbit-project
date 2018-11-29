# Add your Python code here. E.g.
from microbit import *
import random
import radio
import speech

count = 0
radio.on()
radio.config(channel=18)
radio.config(power=6)
messages = ["You lose", "Maybe Next Time!", "Sore Loser!", "Keep Trying!"]

rock = Image("00000:"
            "09990:"
            "09990:"
            "09990:"
            "00000")

paper = Image("99999:"
             "99999:"
             "99999:"
             "99999:"
             "99999")

scissors = Image("99009:"
                "99090:"
                "00900:"
                "99090:"
                "99009")

spock = Image("99099:"
             "99099:"
             "99099:"
             "09990:"
             "09990")

lizard = Image("00900:"
              "09990:"
              "00900:"
              "09990:"
              "00900")
              
speech.say("Ready Set Go", speed=120, pitch=100, throat=100, mouth=200)
while True:
   if accelerometer.was_gesture("shake"):
       display.clear()
       hand = random.randint(0, 4)
       if hand == 0:
           display.show(rock)

       elif hand == 1:
           display.show(paper)

       elif hand == 2:
           display.show(scissors)

       elif hand == 3:
           display.show(spock)

       else:
           display.show(lizard)

   incoming = radio.receive()
   if incoming is not None:
       display.scroll(incoming)

   if count == 5:
       radio.send("Game Over")
       message = random.choice(messages)
       radio.send(message)
       speech.say("I win", speed=120, pitch=100, throat=100, mouth=200)
       display.scroll("I win")
       sleep(100)
       reset()

   if button_a.is_pressed():
       count = count + 1
       display.scroll(str(count))
       
   if button_b.is_pressed():
       radio.send("I quit")
       speech.say("Thanks for playing")
       display.clear()
       break

