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
    consumable=consumable.Arrow(damage=1),
)
broadhead_arrow = Item(
    char="-",
    color=(51, 0, 0),
    name="Broadhead Arrow",
    consumable=consumable.Arrow(damage=2),
)
barbed_arrow = Item(
    char="-",
    color=(51, 0, 0),
    name="Barbed Arrow",
    consumable=consumable.Arrow(damage=3),
)
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=6),
)
greater_health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Greater Health Potion",
    consumable=consumable.HealingConsumable(amount=12),
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

shortsword = Item(char="/", color=(0, 191, 255), name="Short Sword", equippable=equippable.Shortsword())

short_bow = Item(char="D", color=(51, 0, 0), name="Short Bow", equippable=equippable.ShortBow())

long_bow = Item(char="D", color=(51, 0, 0), name="Long Bow", equippable=equippable.LongBow())

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", color=(139, 69, 19), name="Chain Mail", equippable=equippable.ChainMail()
)

steel_plate = Item(
    char="[", color=(139, 69, 19), name="Steel Plate", equippable=equippable.SteelPlate()
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
    inventory=Inventory(capacity=26, items=[short_bow, leather_armor, arrow, arrow, arrow, arrow, arrow, arrow, arrow, arrow, arrow, arrow]),
    level=Level(level_up_base=200),
)

player_warrior = Actor(
    char = "@",
    color = (255, 255, 255),
    name = "Player",
    ai_cls = HostileEnemy,
    equipment=Equipment(dagger, chain_mail),
    fighter = Warrior(hp = 30, base_defense = 1, base_power = 2, poison_dmg = 0),
    inventory=Inventory(capacity=26, items=[dagger, chain_mail]),
    level=Level(level_up_base=200),
)

player_mage = Actor(
    char = "@",
    color = (255, 255, 255),
    name = "Player",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Mage(hp = 25, base_defense = 1, base_power = 1, poison_dmg = 0),
    inventory=Inventory(capacity=26, items=[lightning_scroll, lightning_scroll, fireball_scroll, fireball_scroll, confusion_scroll, confusion_scroll]),
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

elite_orc = Actor(
    char = "O",
    color = (63, 127, 63),
    name = "Elite Orc",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 20, base_defense = 0, base_power = 5, poison_dmg = 0),
    inventory=Inventory(capacity=8),
    level=Level(xp_given=75),
)

troll = Actor(
    char = "t",
    color = (0, 127, 0),
    name = "Troll",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 16, base_defense = 1, base_power = 4, poison_dmg = 0),
    inventory=Inventory(capacity=10),
    level=Level(xp_given=100),
)

elite_troll = Actor(
    char = "T",
    color = (0, 127, 0),
    name = "Elite Troll",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 24, base_defense = 2, base_power = 7, poison_dmg = 0),
    inventory=Inventory(capacity=10),
    level=Level(xp_given=200),
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

giant_bat = Actor(
    char = "W",
    color = (90, 90, 92),
    name = "Giant Bat",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 12, base_defense = 0, base_power = 0, poison_dmg = 3),
    inventory=Inventory(capacity=2),
    level=Level(xp_given=100),
)

spider = Actor(
    char = "m",
    color = (46, 46, 46),
    name = "Spider",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 14, base_defense = 0, base_power = 0, poison_dmg = 2),
    inventory=Inventory(capacity=2),
    level=Level(xp_given=70),
)

giant_spider = Actor(
    char = "M",
    color = (46, 46, 46),
    name = "Giant Spider",
    ai_cls = HostileEnemy,
    equipment=Equipment(),
    fighter = Fighter(hp = 20, base_defense = 0, base_power = 0, poison_dmg = 5),
    inventory=Inventory(capacity=2),
    level=Level(xp_given=150),
)