from item import Item
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'staff': Item('Staff of Magius', 'You have found the War staff of the Red God Magius'),
    'axe': Item("Flint's Axe", "Flint's axe uses magical properties to propel itself through all objects"),
    'torch': Item("Silver Torch", "The silver torch shines with the light of a thousand stars"),
    'quilt': Item("Dagor's Quilt", "Long ago the Demon Dagor created the quilt of space, use it to the best of you ability"),
    'mirror': Item("Syron's Mirror", "Syron mirror of values, show you the path least taken")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# staff, axe, torch, quilt, mirror
room['foyer'].items.append('staff')
room['overlook'].items.append('axe')
room['narrow'].items.append('quilt')
room['treasure'].items.append('mirror')
room['foyer'].items.append('torch')


# new instance of player with name and current room
player = Player(input('Name? '), room['outside'])

while True:
    # create a variable that holds the current players current room
    current_room = player.current_room
    # display the current room for the player after each turn
    print(
        f'Current Room: {current_room.name} \n {current_room.description}')

    print(f'Avaialble Items: {current_room.items}')

    command = input('command: ').strip().lower().split(' ')
# Input Errors and "q", quit the game.
    if command[0] not in ['n', 's', 'e', 'w', 'q']:
        print("Please enter a valid direction")
        continue
    if command[0] == 'q':
        print('Thank you for playing and good bye!')
        break
# navigation
    if command[0] == 'n':
        if current_room.n_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = current_room.n_to
    elif command[0] == 's':
        if current_room.s_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = current_room.s_to
    elif command[0] == 'e':
        if current_room.e_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = current_room.e_to
    elif command[0] == 'w':
        if current_room.w_to is None:
            print('Cant go that way')
            continue
        else:
            player.current_room = current_room.w_to

    else:
        print('please enter only n, s, e, w or q for quit')
