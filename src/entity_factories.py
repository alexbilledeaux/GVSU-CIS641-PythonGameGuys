from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter, Ranger, Warrior, Mage
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
arrow = Item(
    char="-",
    color=(51, 0, 0),
    name="Arrow",
    consumable=consumable.Arrow(),
)
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)
antidote = Item(
    char="!",
    color=(50, 255, 70),
    name="Antidote",
    consumable=consumable.AntidoteConsumable(),
)
armor_repair_kit = Item(
    char="!",
    color=(125, 123, 122),
    name="Armor Repair Kit",
    consumable=consumable.ArmorRepairConsumable(amount=15),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

dagger = Item(
    char="/", color=(0, 191, 255), name="Dagger", equippable=equippable.Dagger()
)

sword = Item(char="/", color=(0, 191, 255), name="Sword", equippable=equippable.Sword())

short_bow = Item(char="D", color=(51, 0, 0), name="Short Bow", equippable=equippable.ShortBow())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)

player = Actor(
    char = "@",
    color = (255, 255, 255),
    name = "Player",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 30, base_defense = 1, base_power = 2, poison_dmg = 0),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

player_ranger = Actor(
    char = "@",
    color = (255, 255, 255),
    name = "Player",
    ai_cls = HostileEnemy,
    equipment=Equipment(short_bow, leather_armor),
    fighter = Ranger(hp = 25, base_defense = 1, base_power = 2, poison_dmg = 0),
    inventory=Inventory(capacity=26, items=[short_bow, leather_armor, arrow, arrow, arrow, arrow, armor_repair_kit]),
    level=Level(level_up_base=200),
)

player_warrior = Actor(
    char = "@",
    color = (255, 255, 255),
    name = "Player",
    ai_cls = HostileEnemy,
    equipment=Equipment(sword, chain_mail),
    fighter = Warrior(hp = 30, base_defense = 1, base_power = 2, poison_dmg = 0),
    inventory=Inventory(capacity=26, items=[sword, chain_mail]),
    level=Level(level_up_base=200),
)

player_mage = Actor(
    char = "@",
    color = (255, 255, 255),
    name = "Player",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Mage(hp = 25, base_defense = 1, base_power = 1, poison_dmg = 0),
    inventory=Inventory(capacity=26, items=[lightning_scroll, fireball_scroll, confusion_scroll]),
    level=Level(level_up_base=200),
)


orc = Actor(
    char = "o",
    color = (63, 127, 63),
    name = "Orc",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 10, base_defense = 0, base_power = 3, poison_dmg = 0),
    inventory=Inventory(capacity=8),
    level=Level(xp_given=35),
)

troll = Actor(
    char = "T",
    color = (0, 127, 0),
    name = "Troll",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 16, base_defense = 1, base_power = 4, poison_dmg = 0),
    inventory=Inventory(capacity=10),
    level=Level(xp_given=100),
)

bat = Actor(
    char = "w",
    color = (90, 90, 92),
    name = "Bat",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 8, base_defense = 0, base_power = 0, poison_dmg = 1),
    inventory=Inventory(capacity=2),
    level=Level(xp_given=50),
)

spider = Actor(
    char = "M",
    color = (46, 46, 46),
    name = "Spider",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 14, base_defense = 0, base_power = 0, poison_dmg = 2),
    inventory=Inventory(capacity=2),
    level=Level(xp_given=35),
)