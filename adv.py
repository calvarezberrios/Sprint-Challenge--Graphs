from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from collections import deque

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited = set()
reversed_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}
queue = deque()
queue.append([player.current_room])
go_back = []

while len(queue) > 0:
    curr_path = queue.pop()
    curr_room = curr_path[-1] 
    next_move = None

    if player.current_room not in visited:
        visited.add(player.current_room)

    for exit_path in curr_room.get_exits():
        if curr_room.get_room_in_direction(exit_path) not in visited:
            next_move = exit_path
            go_back.append(reversed_direction[next_move])
            break

    if next_move is not None:
        traversal_path.append(next_move)
        player.travel(next_move)
        newPath = list(curr_path)
        newPath.append(player.current_room)
        queue.append(newPath)
    else:
        curr_path.pop()
        
        if len(visited) < len(world.rooms):
            traversal_path.append(go_back[-1])
            player.travel(go_back.pop())
            queue.append(curr_path)
        
        
   






# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
