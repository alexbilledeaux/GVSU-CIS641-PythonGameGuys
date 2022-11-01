from __future__ import annotations

import copy
from typing import TYPE_CHECKING

import color
from components.base_component import BaseComponent
from render_order import RenderOrder
import entity_factories

if TYPE_CHECKING:
    from entity import Actor

class Fighter(BaseComponent):
    parent: Actor

    def __init__(self, hp: int, base_defense: int, base_power: int):
        self.max_hp = hp
        self._hp = hp
        self.base_defense = base_defense
        self.base_power = base_power
        self.fov = 8

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()

    @property
    def defense(self) -> int:
        return self.base_defense + self.defense_bonus

    @property
    def power(self) -> int:
        return self.base_power + self.power_bonus

    @property
    def defense_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.defense_bonus
        else:
            return 0

    @property
    def power_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.power_bonus
        else:
            return 0

    def die(self) -> None:
        if self.engine.player is self.parent:
            death_message = "You died!"
            death_message_color = color.player_die
        else:
            death_message = f"{self.parent.name} is dead!"
            death_message_color = color.enemy_die

        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"remains of {self.parent.name}"
        self.parent.render_order = RenderOrder.CORPSE
        
        self.engine.message_log.add_message(death_message, death_message_color)

        self.engine.player.level.add_xp(self.parent.level.xp_given)

    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def take_damage(self, amount: int) -> None:
        self.hp -= amount
    
    def give_loadout(self, player) -> None:
        items = self.starting_items
        equipment = self.starting_equipment
        for item in items:
            _copy = copy.deepcopy(item)
            _copy.parent = player.inventory
            player.inventory.items.append(_copy)

        for equippable in equipment:
            _copy = copy.deepcopy(equippable)
            _copy.parent = player.inventory
            player.inventory.items.append(_copy)
            player.equipment.toggle_equip(_copy, add_message=False)

class Ranger(Fighter):
    def __init__(self, hp: int, base_defense: int, base_power: int):
        super().__init__(hp, base_defense, base_power)
        self.fov = 16
        self.starting_items = [entity_factories.quiver]
        self.starting_equipment = [entity_factories.short_bow, entity_factories.leather_armor]

class Warrior(Fighter):
    def __init__(self, hp: int, base_defense: int, base_power: int):
        super().__init__(hp, base_defense, base_power)
        self.fov = 8
        self.starting_items = []
        self.starting_equipment = [entity_factories.sword, entity_factories.chain_mail]

class Mage(Fighter):
    def __init__(self, hp: int, base_defense: int, base_power: int):
        super().__init__(hp, base_defense, base_power)
        self.fov = 10
        self.starting_items = [entity_factories.lightning_scroll, entity_factories.fireball_scroll, entity_factories.confusion_scroll]
        self.starting_equipment = []

    # We can use methods like this to apply custom logic at certain event hooks based on the player's class
    def use_consumable(self) -> None:
        # Have a % chance of recovering the scroll
        pass