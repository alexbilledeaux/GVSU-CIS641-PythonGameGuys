from __future__ import annotations

import copy
import random
from typing import TYPE_CHECKING

import color
from components.base_component import BaseComponent
import components.ai
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor

class Fighter(BaseComponent):
    parent: Actor

    def __init__(self, hp: int, base_defense: int, base_power: int, poison_dmg: int):
        self.max_hp = hp
        self._hp = hp
        self.base_defense = base_defense
        self.base_power = base_power
        self.fov = 8
        self.poison_dmg = poison_dmg
        self.current_poison = 0
        self.class_ability_rank = 0
        self.poison_active = False
        self.poison_threshold = int(float(self.max_hp * 0.2))

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

        # Enemies drop inventory when killed
        items = [i for i in self.parent.inventory.items]
        for item in items:
            self.parent.inventory.drop(item)

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
        if self.parent.equipment.armor:
            armor = self.parent.equipment.armor
            armor.take_damage(amount)
            if armor.equippable.durability <= 0:
                self.parent.equipment.destroy_message(armor.name)
                self.parent.equipment.armor = None
                self.parent.inventory.destroy(armor, logs_message=False)
        else:
            self.hp -= amount    
    
    def heal_poison(self, amount) -> None:
        new_poison_value = self.current_poison - amount

        if new_poison_value < 0:
            new_poison_value = 0

        self.current_poison = new_poison_value

    def take_poison_damage(self) -> None:
        if not self.poison_active:
            if self.current_poison > self.poison_threshold:
                self.poison_active = True
                self.hp -= 1
                self.engine.message_log.add_message(f"Your poison build-up was too much! You start to take damage as your body begins to purge the toxins!")
                self.current_poison -= 1
        else:
            self.hp -= 1
            self.engine.message_log.add_message(f"You take 1 point of damage from your poison build up!")
            self.current_poison -= 1
            if self.current_poison == 0:
                self.engine.message_log.add_message(f"Your body has been purged of toxins!")
                self.poison_active = False

class Ranger(Fighter):
    def __init__(self, hp: int, base_defense: int, base_power: int, poison_dmg: int):
        super().__init__(hp, base_defense, base_power, poison_dmg)
        self.fov = 16
        self.abilityIncrement = 5
        self.abilityDescription = "recover arrows"

    def use_consumable(self, item, target) -> None:
        # The ranger has a chance to spawn arrows on targets struck by arrows
        if item.char == "-":
            if random.random() < (0.5 + ((self.abilityIncrement/100) * self.class_ability_rank)) and target.is_alive and len(target.inventory.items) < target.inventory.capacity:
                _copy = copy.deepcopy(item)
                _copy.parent = target.inventory
                target.inventory.items.append(_copy)
                self.engine.message_log.add_message(f"The {item.name} looks recoverable!")
            elif random.random() < (0.8 + ((self.abilityIncrement/100) * self.class_ability_rank)) and not target.is_alive and len(target.inventory.items) < target.inventory.capacity:
                _copy = copy.deepcopy(item)
                _copy.spawn(self.gamemap, target.x, target.y)
            else:
                self.engine.message_log.add_message(f"The {item.name} broke as it hit the {target.name}.")

    def on_enemy_hit(self, target) -> None:
        # Do nothing
        pass

class Warrior(Fighter):
    def __init__(self, hp: int, base_defense: int, base_power: int, poison_dmg: int):
        super().__init__(hp, base_defense, base_power, poison_dmg)
        self.fov = 8
        self.abilityIncrement = 1
        self.abilityDescription = "stun enemies"
    
    def use_consumable(self, item, target) -> None:
        # Do nothing
        pass

    def on_enemy_hit(self, target) -> None:
        # The warrior has a chance to apply the confusion effect
        if random.random() < (0.05 + ((self.abilityIncrement/100) * self.class_ability_rank)):
            target.ai = components.ai.ConfusedEnemy(
                entity=target, previous_ai=target.ai, turns_remaining=5,
            )
            self.engine.message_log.add_message(
                f"Your strike dazes the {target.name} and it begins to stumble around!",
                color.status_effect_applied,
            )

class Mage(Fighter):
    def __init__(self, hp: int, base_defense: int, base_power: int, poison_dmg: int):
        super().__init__(hp, base_defense, base_power, poison_dmg)
        self.fov = 10
        self.abilityIncrement = 5
        self.abilityDescription = "preserve scrolls"

    # Event hooks for actions
    def use_consumable(self, item, target) -> None:
        # The mage has a chance to recover scrolls upon use
        if item.char == "~":
            if random.random() < (0.6 + ((self.abilityIncrement/100) * self.class_ability_rank)):
                _copy = copy.deepcopy(item)
                _copy.parent = self.parent.inventory
                self.parent.inventory.items.append(_copy)
                self.engine.message_log.add_message(f"You managed to preserve the {item.name}!")

    def on_enemy_hit(self, target) -> None:
        # Do nothing
        pass