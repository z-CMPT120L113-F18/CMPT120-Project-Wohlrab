#CMPT 120L
#Project Version .1
#Ashley Wohlrab
# 17 September 2018

print("\ESCAPE FROM THE DEATH STAR: A STAR WARS GAME"
      "\n========\n")

# show game introduction
#for reference, this game takes place between Episodes 3 and 4
print("A long time ago in a galaxy far, far away..."

      "You are a rebel spy who has snuck aboard the Death Star in search of "
      "intel on Darth Vader's next attack. You are sure that you'll be able "
      "to take this information back to the Rebel Alliance and help destroy "
      "the Sith, who are rising to power in their creation of the Galactic Empire."
      "As you're sneaking through the corridors of the massive space-station, the "
      "alarm sounds. You duck into a dark corner just outside the control room as dozens of "
      "storm-troopers run toward the main entrance of the ship. Now is your chance! You take this "
      "opportunity to race into the empty control room, and gather the intel you need."
      "The Death Star is under attack, and now that you have what you came for, it's "
      "time to find a strategic escape!")

scoreMessage = "Your score is "
inputMessage = "\n<Press Enter to Continue...>\n"
score = 0;

# this function shows the current score
def printScore():
	print(scoreMessage + str(score))

# prompt the user
input(inputMessage)

# show the current location
print("You are standing in the empty control room."
          "You hear the footsteps of stormtroopers outside the door. "
          "There is an air duct on the wall, a back door to the room, and strange looking tool laying on the desk.")

# show the current score
printScore()

# prompt the user
input(inputMessage)

# show the current location
print("You pick up the tool and walk to the air duct. "
      "Using the tool, you pry the vent from the duct."
      "It's dark inside, but you can just make out the path in front of you.")

# update the score
score = score + 5
print(scoreMessage + str(score))

# same as above
input(inputMessage)

# same as above
print("You take a right turn, and then a left."
      "You come across another vent, leading into what looks like a small, empty room."
      "You use the tool to pry open the vent, then drop down into a storage closet")

# same as above
score = score + 5
print(scoreMessage + str(score))

# again...
input(inputMessage)

# again...
print("Inside you find storm-trooper uniforms!"
      "You grab a uniform and throw it on, opening the door and blending into the crowd "
      "of stormtroopers outside.")

# again...
score = score + 5
print(scoreMessage + str(score))

# yet again...
input(inputMessage)

# yet again...
print("You take a left turn, then a right and find your way to the ship's vehicle storage."
      "There are Rebels and Storm-troopers fighting closeby, but you jump into a nearby tie fighter.")

# yet again...
score = score + 5
print(scoreMessage + str(score))

# one last time...
input(inputMessage)

# show game ending
print("You turn the key and start the engine, flying away from the vessel."
      "You look out into space and feel hopeful for the future of the galaxy. Game over!")

# show credits
print("\nCopyright (c) 2018 Ashley Wohlrab, Ashley.Wohlrab1@marist.edu")
