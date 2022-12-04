from __future__ import annotations

from typing import Tuple, TYPE_CHECKING

import color

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap
    from entity import Actor


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ", ".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()

def render_bar(
    console: Console, player: Actor, total_width: int
) -> None:
    bar_width = int(float(player.fighter.hp) / player.fighter.max_hp * total_width)
    bar_poison_width = int(float(player.fighter.current_poison) / player.fighter.max_hp * total_width)
    bar_xp_width = int(float(player.level.current_xp) / player.level.experience_to_next_level * total_width)

    console.draw_rect(x = 0, y = 45, width = total_width, height = 1, ch = 1, bg = color.bar_empty)
    console.draw_rect(x = 0, y = 46, width = total_width, height = 1, ch = 1, bg = color.bar_xp_empty)
    console.draw_rect(x = 0, y = 44, width = total_width, height = 1, ch = 1, bg = color.bar_armor_empty) 

    if bar_width > 0:
        console.draw_rect(
            x = 0, y = 45, width = bar_width, height = 1, ch = 1, bg = color.bar_filled
        )
    
    if bar_poison_width > 0:
        if bar_poison_width > bar_width:
            console.draw_rect(
                x = 0, y = 45, width = bar_width, height = 1, ch = 1, bg = color.bar_poison
            )
        else:
            console.draw_rect(
                x = bar_width - bar_poison_width, y = 45, width = bar_poison_width, height = 1, ch = 1, bg = color.bar_poison
            )
    
    if bar_xp_width > 0:
        console.draw_rect(
            x = 0, y = 46, width = bar_xp_width, height = 1, ch = 1, bg = color.bar_xp
        )

    if player.equipment.armor != None:
        bar_armor_width = int(float(player.equipment.armor.equippable.durability) / player.equipment.armor.equippable.max_durability * total_width)
        console.draw_rect(x = 0, y = 44, width = bar_armor_width, height = 1, ch = 1, bg = color.bar_armor)
        console.print(
            x = 1, y = 44, string = f"Armor: {player.equipment.armor.equippable.durability}/{player.equipment.armor.equippable.max_durability}", fg = color.bar_text
        )

    else:
        console.print(
            x = 1, y = 44, string = f"No Armor", fg = color.bar_text
        )

    if player.fighter.current_poison > 0:
        console.print(
                x = 1, y = 45, string = f"HP: {player.fighter.hp}/{player.fighter.max_hp} ({player.fighter.current_poison})", fg = color.bar_text
            )
        
    else:
        console.print(
                x = 1, y = 45, string = f"HP: {player.fighter.hp}/{player.fighter.max_hp}", fg = color.bar_text
            )

    console.print(
        x = 1, y = 46, string = f"XP: {player.level.current_xp}/{player.level.experience_to_next_level}", fg = color.bar_text
    )

def render_dungeon_level(
    console: Console, dungeon_level: int, location: Tuple[int, int]
) -> None:
    """
    Render the level the player is currently on, at the given location.
    """
    x, y = location

    console.print(x=x, y=y, string=f"Dungeon level: {dungeon_level}")

def render_names_at_mouse_location(
    console: Console, x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x = mouse_x, y = mouse_y, game_map = engine.game_map
    )

    console.print(x = x, y = y, string = names_at_mouse_location)