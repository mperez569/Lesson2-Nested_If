#1. Nested Decisions: The Adventure Game
#Task 1: Code Correction
place = input("Choose a place: forest or cave?: ")

if place == "forest":
  action = input("climb a tree or cross a river?: ")
  if action == "climb a tree":
    print("You found a bird's nest!")
  elif action == "cross a river":
    print("You found a boat!")
  #task 3
  else:
      pass
    
elif place == "cave":
    #print("You find a hidden treasure!")
  #Task 2: Setting the Scene
  action = input("light a torch or proceed in the dark?: ")
  if action == "light a torch":
    print("you woke up a monster!")
  elif action == "proceed in the dark":
    print("you are lost!")
  #task 3
  else:
      pass
#task 3
else:
    pass

#2. Quick Decisions: The Event Planner 🎉
#Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"

#Task 2: Venue Selection
projector = "You need a projector" if attendees > 50 else "no need for a projector"
audio_system = "large speakers" if attendees > 30 else "small speakers"

#Task 3: Catering Choices
catering = input("Would you like vegetarian food?: ")
food = "We reccomend Veggie Delight Caterers" if catering == "yes" else "We recommend Gourmet Meals Caterers"
print("venue: " + venue + "\nprojector: " + projector + "\naudio system: " + audio_system + "\n" + food)
