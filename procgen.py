from __future__ import annotations

import random
from typing import Iterator, List, Tuple, TYPE_CHECKING

import tcod

from game_map import GameMap
import numpy as np
from shapes import octagon
import sys

import tile_types
np.set_printoptions(threshold=sys.maxsize)


if TYPE_CHECKING:
    from entity import Entity


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    def intersects(self, other: RectangularRoom) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )


def tunnel_between(
    start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:  # 50% chance.
        # Move horizontally, then vertically.
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y


def generate_dungeon(
    max_rooms: int,
    room_min_size: int,
    room_max_size: int,
    map_width: int,
    map_height: int,
    player: Entity,
) -> GameMap:
    """Generate a new dungeon map."""
    dungeon = GameMap(map_width, map_height)

    rooms: List[RectangularRoom] = []

    for r in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        # "RectangularRoom" class makes rectangles easier to work with
        new_room = RectangularRoom(x, y, room_width, room_height)

        # Run through the other rooms and see if they intersect with this one.
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue  # This room intersects, so go to the next attempt.
        # If there are no intersections then the room is valid.

        # Dig out this rooms inner area.
        dungeon.tiles[new_room.inner] = tile_types.floor

        if len(rooms) == 0:
            # The first room, where the player starts.
            player.x, player.y = new_room.center
        else:  # All rooms after the first.
            # Dig out a tunnel between this room and the previous one.
            for x, y in tunnel_between(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tile_types.floor

        # Finally, append the new room to the list.
        rooms.append(new_room)

    return dungeon

def generate_dungeon2(
    map_width: int,
    map_height: int,
    player: Entity
) -> GameMap:
    """Generate a new dungeon map."""
    dungeon = GameMap(map_width, map_height)
    dungeon_array=octagon()
    print(dungeon_array)
    for x in range(map_width):
        for y in range(map_height):
            if dungeon_array[y][x]==1:
                dungeon.tiles[x, y]=tile_types.wall
            elif dungeon_array[y][x]==0:
                dungeon.tiles[x, y]=tile_types.floor

    return dungeon

def generate_dungeon3():
    while True:
        map_outline=np.zeros((4,4),int)
        column=np.random.randint(3)
        row=0
        done=False
        while True:
            x_direction=0
            y_direction=0
            if np.random.random_sample()<0.5:
                room_type=3
            else:
                room_type=1
            #need to make it flip directions on hitting walls
            room_type_number=np.random.randint(1,6)
            
            if room_type_number in set([1,2]):
                x_direction=-1
                y_direction=0
            elif room_type_number in set([3,4]):
                x_direction=1
                y_direction=0
            else:
                y_direction=1
            
            if y_direction>0 and row<3:
                room_type=2
            
            if column==3 and x_direction==1 and row<3:
                x_direction=0
                y_direction=1
                room_type=2
            elif column==0 and x_direction==-1 and row<3:
                x_direction=0
                y_direction=1
                room_type=2
            elif column==3 and x_direction==1:
                room_type=4
                done=True
            elif column==0  and x_direction==-1:
                room_type=4
                done=True
            elif row==3 and y_direction==1:
                room_type=4
                done=True
            else:
                y_direction=0
            
            map_outline[row][column]=room_type

            print(map_outline)
            if done:
                break
            column+=x_direction
            row+=y_direction
            if room_type==2 and column==3:
                x_direction=-1
            elif room_type==2 and column==0:
                x_direction=1
        if np.count_nonzero(map_outline)>10:
            break