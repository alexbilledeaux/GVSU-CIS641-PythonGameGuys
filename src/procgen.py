from __future__ import annotations

import random
from typing import Dict, Iterator, List, Tuple, TYPE_CHECKING

import tcod
import numpy as np # type: ignore

import entity_factories
from game_map import GameMap
import tile_types


if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


max_items_by_floor = [
    (1, 1),
    (4, 2),
    (6, 3),
]

cave_min_items_by_floor = [
    (2, 5),
    (4, 10),
    (6, 15),
]

cave_max_items_by_floor = [
    (2, 15),
    (4, 25),
    (6, 30),
]

max_monsters_by_floor = [
    (1, 2),
    (4, 3),
    (6, 4),
]

cave_min_monsters_by_floor = [
    (2, 5),
    (4, 10),
    (6, 15),
]

cave_max_monsters_by_floor = [
    (2, 20),
    (4, 25),
    (6, 35),
]

item_chances: Dict[int, List[Tuple[Entity, int]]] = {
    0: [(entity_factories.health_potion, 35), (entity_factories.armor_repair_kit, 15), (entity_factories.arrow, 20), (entity_factories.dagger, 5)],
    2: [(entity_factories.confusion_scroll, 10), (entity_factories.arrow, 10), (entity_factories.broadhead_arrow, 10), (entity_factories.antidote, 15),
     (entity_factories.leather_armor, 10), (entity_factories.short_bow, 5), (entity_factories.shortsword, 5), (entity_factories.greater_health_potion, 2)],
    4: [(entity_factories.lightning_scroll, 25), (entity_factories.broadhead_arrow, 10), (entity_factories.long_bow, 5), (entity_factories.sword, 5),
     (entity_factories.chain_mail, 10), (entity_factories.greater_health_potion, 18)],
    6: [(entity_factories.fireball_scroll, 25), (entity_factories.steel_plate, 10), (entity_factories.broadhead_arrow, 10), (entity_factories.barbed_arrow, 10)],
}

enemy_chances: Dict[int, List[Tuple[Entity, int]]] = {
    0: [(entity_factories.orc, 80)],
    3: [(entity_factories.troll, 15)],
    5: [(entity_factories.troll, 30), (entity_factories.elite_orc, 20)],
    7: [(entity_factories.elite_troll, 15), (entity_factories.elite_orc, 70)],
}

cave_enemy_chances: Dict[int, List[Tuple[Entity, int]]] = {
    0:[(entity_factories.orc, 50)],
    2:[(entity_factories.bat, 40)],
    4:[(entity_factories.bat, 60), (entity_factories.spider, 10)],
    6:[(entity_factories.spider, 25), (entity_factories.giant_bat, 10)],
    8:[(entity_factories.giant_spider, 10), (entity_factories.giant_bat, 30)]

}

def get_max_value_for_floor(
    max_value_by_floor: List[Tuple[int, int]], floor: int
) -> int:
    current_value = 0

    for floor_minimum, value in max_value_by_floor:
        if floor_minimum > floor:
            break
        else:
            current_value = value

    return current_value

def get_min_value_for_floor(
    min_value_by_floor: List[Tuple[int, int]], floor: int
) -> int:
    current_value = 0

    for floor_minimum, value in min_value_by_floor:
        if floor_minimum > floor:
            break
        else:
            current_value = value

    return current_value

def get_entities_at_random(
    weighted_chances_by_floor: Dict[int, List[Tuple[Entity, int]]],
    number_of_entities: int,
    floor: int,
) -> List[Entity]:
    entity_weighted_chances = {}

    for key, values in weighted_chances_by_floor.items():
        if key > floor:
            break
        else:
            for value in values:
                entity = value[0]
                weighted_chance = value[1]

                entity_weighted_chances[entity] = weighted_chance

    entities = list(entity_weighted_chances.keys())
    entity_weighted_chance_values = list(entity_weighted_chances.values())

    chosen_entities = random.choices(
        entities, weights=entity_weighted_chance_values, k=number_of_entities
    )

    return chosen_entities

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


def place_entities(room: RectangularRoom, dungeon: GameMap, floor_number: int,) -> None:
    number_of_monsters = random.randint(
        0, get_max_value_for_floor(max_monsters_by_floor, floor_number)
    )
    number_of_items = random.randint(
        0, get_max_value_for_floor(max_items_by_floor, floor_number)
    )

    monsters: List[Entity] = get_entities_at_random(
        enemy_chances, number_of_monsters, floor_number
    )
    items: List[Entity] = get_entities_at_random(
        item_chances, number_of_items, floor_number
    )

    for entity in monsters + items:
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            entity.spawn(dungeon, x, y)

def place_cave_entities(list, map, dungeon: GameMap, floor_number: int,) -> None:
    number_of_monsters = random.randint(
        get_min_value_for_floor(cave_min_monsters_by_floor, floor_number),
        get_max_value_for_floor(cave_max_monsters_by_floor, floor_number)
    )
    number_of_items = random.randint(
        get_min_value_for_floor(cave_min_items_by_floor, floor_number),
        get_max_value_for_floor(cave_max_items_by_floor, floor_number)
    )

    monsters: List[Entity] = get_entities_at_random(
        cave_enemy_chances, number_of_monsters, floor_number
    )
    items: List[Entity] = get_entities_at_random(
        item_chances, number_of_items, floor_number
    )

    for entity in monsters + items:
        space = random.randint(1, len(list)-1)
        x = list[space][0]
        y = list[space][1]

        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            entity.spawn(dungeon, x, y)


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
    engine: Engine,
) -> GameMap:
    """Generate a new dungeon map."""
    player = engine.player
    dungeon = GameMap(engine, map_width, map_height, entities=[player])

    rooms: List[RectangularRoom] = []

    center_of_last_room = (0, 0)

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
            player.place(*new_room.center, dungeon)
        else:  # All rooms after the first.
            # Dig out a tunnel between this room and the previous one.
            for x, y in tunnel_between(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tile_types.floor

            center_of_last_room = new_room.center
        
        place_entities(new_room, dungeon, engine.game_world.current_floor)

        dungeon.tiles[center_of_last_room] = tile_types.down_stairs
        dungeon.downstairs_location = center_of_last_room

        # Finally, append the new room to the list.
        rooms.append(new_room)

    return dungeon

def generate_cave(
    max_rooms: int,
    room_min_size: int,
    room_max_size: int,
    map_width: int,
    map_height: int,
    engine: Engine,
) -> GameMap:
    """Generate a new cave map."""
    player = engine.player
    chanceToStartAlive = 0.3
    # alive in this context means being a wall rather than a floor
    stepCount = 2
    dungeon = GameMap(engine, map_width, map_height, entities=[player])

    validCave = False
    while not validCave:
        cellMap = []
        for j in range(map_width):
            row = []
            for k in range(map_height):
                if random.random() < chanceToStartAlive:
                    row.append(True)
                else:
                    row.append(False)
            cellMap.append(row)

        cellMap = doSimulationStep(cellMap, map_width, map_height)
        cellMap = doSimulationStep(cellMap, map_width, map_height)
        cellMap = doSimulationStep(cellMap, map_width, map_height)
        cellMap = doSimulationStep(cellMap, map_width, map_height)

        validStart = False
        while not validStart:
            rand_x = random.randint(0, map_width-1)
            rand_y = random.randint(0, map_height-1)
            if not cellMap[rand_x][rand_y]:
                validStart = True
        list = fillCheck([], cellMap, rand_x, rand_y)
        if len(list) > 800 & len(list) < 1250:
            validCave = True
    
    for x in range(map_width):
        for y in range(map_height):
            dungeon.tiles[x, y] = tile_types.wall
    
    for i in list:
        dungeon.tiles[i[0], i[1]] = tile_types.floor

    
    player.place(rand_x, rand_y, dungeon)
    if len(list) % 2 == 1:
        startInt = (len(list) + 1)/2
    else:
        startInt = len(list)/2
    end = random.randint(startInt, len(list) - 1)
    dungeon.tiles[list[end][0], list[end][1]] = tile_types.down_stairs
    dungeon.downstairs_location = (list[end][0], list[end][1])

    place_cave_entities(list, cellMap, dungeon, engine.game_world.current_floor)

    return dungeon

def doSimulationStep(
    oldMap,
    map_width: int,
    map_height: int,
):
    newMap = []
    for j in range(map_width):
        row = []
        for k in range(map_height):
            row.append(False)
        newMap.append(row)

    for x in range(map_width):
        for y in range(map_height):
            nbs = countAliveNeighbors(oldMap, x, y)
            if oldMap[x][y]:
                if nbs >= 3:
                    newMap[x][y] = True
            else:
                if nbs > 4:
                    newMap[x][y] = True
    
    return newMap



def countAliveNeighbors(
    map,
    x: int,
    y: int,
):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            n_x = x + i
            n_y = y + j
            if i == 0 & j == 0:
                pass
            elif n_x < 0 | n_x > len(map) | n_y < 0 | n_y > len(map[x]):
                count = count + 1
            elif(map[x][y]):
                count = count + 1
    
    return count

def fillCheck(
    list,
    map,
    x: int,
    y: int,
):
    list.append([x, y])
    if len(list) > 1250:
        return list
    if x - 1 >= 0:
        if not map[x-1][y]:
            found = False
            for i in list:
                if i == [x-1, y]:
                    found = True
            if not found:
                list = fillCheck(list, map, x-1, y)
    
    if y - 1 >= 0:
        if not map[x][y-1]:
            found = False
            for i in list:
                if i == [x, y-1]:
                    found = True
            if not found:
                list = fillCheck(list, map, x, y-1)
    
    if x + 1 < 80:
        if not map[x+1][y]:
            found = False
            for i in list:
                if i == [x+1, y]:
                    found = True
            if not found:
                list = fillCheck(list, map, x+1, y)

    if y + 1 < 43:
        if not map[x][y+1]:
            found = False
            for i in list:
                if i == [x, y+1]:
                    found = True
            if not found:
                list = fillCheck(list, map, x, y+1)
    
    return list