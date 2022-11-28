from __future__ import annotations

from typing import List, TYPE_CHECKING

from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor, Item


class Inventory(BaseComponent):
    parent: Actor

    def __init__(self, capacity: int, items: List[Item] = []):
        self.capacity = capacity
        self.items: List[Item] = []
        for item in items:
            item.parent = self
            self.items.append(item)

    def item_count(self, item: Item) -> Number:
        """
        Returns the total number of a given item in the inventory
        """
        return sum(i.name == item.name for i in self.items)

    def get_unique_items(self) -> List:
        """
        Returns a list of the unique items in the inventory
        """
        unique_items = []
        for item in self.items:
            item_is_unique = True
            for unique_item in unique_items:
                if item.name == unique_item.name:
                    item_is_unique = False
            if item_is_unique:
                unique_items.append(item)
        return unique_items
    
    def drop(self, item: Item, logs_message: bool = True) -> None:
        """
        Removes an item from the inventory and restores it to the game map, at the owner's current location.
        """
        if self.parent == self.engine.player and logs_message:
            self.engine.message_log.add_message(f"You dropped the {item.name}.")

        item.spawn(self.gamemap, self.parent.x, self.parent.y)
        self.items.remove(item)

    def destroy(self, item: Item, logs_message: bool = True) -> None:
        """
        Removes an item from the inventory.
        """
        if self.parent == self.engine.player and logs_message:
            self.engine.message_log.add_message(f"Your {item.name} was destroyed.")

        self.items.remove(item)