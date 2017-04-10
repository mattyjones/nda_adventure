#! /usr/bin/env python

# greet the player
#
# ask if they would like to continue a previous game
# if the answer is yes then provide a list of saved games
# if the answer is no then start a new game
#
# set the starting location (area of the cave)
# describe the starting room
# sample list of commands for the player to type (north, east, south, west, look)

# action = ''
# common_actions = 'north, south, east, west, look, pickup, quit'
# local_actions = 'no-op'

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

matt_r1_map = {'south': 'r2', 'east': 'r3', 'west': 'r4'}
matt_r2_map = {'north': 'r1', 'east': 'r5', 'west': 'r6'}
matt_r1_description = """

Welcome to Matt's area. Be prepared for anything, you never know what is around the next corner or the next room.

You are in a wide empty room with doors to the south, east, and west. There is a chair in the middle of the room and an empty table.
"""

def help() :
    if local_actions == '':
      print('\ncommon actions: ' + common_actions + '\n')
    else:
      print('\ncommon actions: ' + common_actions + ', ' + local_actions + '\n')
    
    print('The simplest thing to do is look around\n')

def look_around(room):
    print room

def move(direction, location):
    # m = location + '_map'
    print [direction]


def leave_game():
    print('Good Bye!')
    exit(0)

## -- Welcome the player and start the game -- ##
print('Hello, welcome to the madhouse!\n')

new_game = raw_input('Would you like to continue a previous game? (yes/no)\n')
if new_game == "yes":
    print('Sorry that feature is not implemented yet')
    exit(1)
else:
  print('Lets start a new game then\n')
  loc = 'matt_r1'
  print matt_r1_description # print the intro to your area

## -- Play the game -- ##

while action != 'quit':

    action = raw_input('What would you like to do? (help for list of available actions)\n')

    if action == 'help':
        help()
    elif action == 'move north':
        move('north')
    elif action == 'move south':
        move('south', loc)
    elif action == 'move east':
        move('east')
    elif action == 'move west':
        move('west')
    elif action == 'look around':
        look_around(matt_r1)
    elif action == 'quit':
        leave_game()
    else:
      print(' Please enter a valid command\n')
      help()    

