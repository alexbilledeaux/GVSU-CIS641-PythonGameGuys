from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        power_bonus: int = 0,
        defense_bonus: int = 0,
        max_durability: int = 15,
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_durability = max_durability
        self.durability = max_durability
    
    def take_damage(self, amount: int) -> None:
        self.durability -= amount

    def repair_damage(self, amount: int) -> int:
        amount_repaired = amount
        new_durability = self.durability + amount_repaired
        if new_durability > self.max_durability:
            amount_repaired -= (new_durability - self.max_durability)
            new_durability = self.max_durability
        self.durability = new_durability
        return amount_repaired


class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=1)

class Shortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)

class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=3)

class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=1, max_durability=15)

class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=1, max_durability=25)

class SteelPlate(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=2, max_durability=25)

class ShortBow(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=1)

class LongBow(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)