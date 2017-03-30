#! /usr/bin/env python

DIRECTIONS = ['north', 'south', 'east', 'west']

# room maps
MATT_R1_MAP = {'north': 'matt_entrance',
          'south': 'matt_r2',
          'east': 'matt_r3',
          'west': 'matt_r4'}

MATT_R2_MAP = {'north': 'matt_entrance'}

MATT_R3_MAP = {'west': 'matt_entrance'}

MATT_R4_MAP = {'east': 'matt_entrance'}

# room functions
def matt_outside():
    print("""
    outside
    """)

def matt_entrance():
    print("""
Welcome to Matt's area. Be prepared for anything, you never know what is around the next corner or the next room.

You are in a wide empty room with doors to the south, east, and west. There is a chair in the middle of the room and an empty table.
    """)

def matt_r2():
    print( """
    you are in room 2
    """)

def matt_r3():
    print( """
    you are in room 3
    """)

def matt_r4():
    print( """
    you are in room 4
    """)

# general functions
def help() :
    if local_actions == '':
      print('\ncommon actions: ' + common_actions + '\n')
    else:
      print('\ncommon actions: ' + common_actions + ', ' + local_actions + '\n')
    
    print('The simplest thing to do is look around\n')

def move(action, location, map):
    p = False # make sure we have a valid direction to move
    direction = action.partition(' ')[2]
    for d in DIRECTIONS:
        if d == direction:
            p = True
    if p:
        map[location]
    else:
        print('please enter a valid direction to move in (north, south, east, west')

def look_around(room):
    print room

def go_home():
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
  # set the global location
  location = MATT_R1_MAP['north']
  map = MATT_R1_MAP
  action = ''
  print location
  getattr('', location)()

## -- Play the game -- ##

while action != 'quit':

    action = raw_input('What would you like to do? (help for list of available actions)\n')

    # if action == 'help':
    #     help()
    if 'move' in action:
        move(action, location, map)
    # elif action == 'look':
    #     look_around(matt_r1)
    elif action == 'quit':
        go_home()
    else:
      print(' Please enter a valid command\n')
      # help()

