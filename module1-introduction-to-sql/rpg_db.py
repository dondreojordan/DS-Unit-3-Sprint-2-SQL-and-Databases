""" Use sqlite3 to load and write queries to explore the data, and answer the following questions: """


### How many total Characters are there? 
SELECT
    COUNT(DISTINCT "name") AS char_name_count
FROM
    charactercreator_character 

### How many of each specific subclass? (w/ assumption a Mage can be a Necromancer)
SELECT
    COUNT(DISTINCT cleric.character_ptr_id) AS cleric_count,
    COUNT(DISTINCT fighter.character_ptr_id) AS fighter_count,
    COUNT(DISTINCT mage.character_ptr_id) AS cleric_count,
    COUNT(DISTINCT necromancer.mage_ptr_id) AS necromancer_count,
    COUNT(DISTINCT thief.character_ptr_id) AS thief_count
FROM
    charactercreator_cleric as cleric, 
    charactercreator_fighter as fighter,
    charactercreator_mage as mage,
    charactercreator_necromancer as necromancer,
    charactercreator_thief as thief
    
# Output:
# cleric_count: 75, fighter_count: 68, cleric_count: 108
# necromancer_count: 11, thief_count: 51 

### How many total Items? 
SELECT
    COUNT(DISTINCT name) AS items_count
FROM
    armory_item

# Output:
# items_count: 172

### How many of the Items are weapons? How many are not?
SELECT * FROM armory_item  # 174 (Total Inventory)
select count(name) from armory_item
# Minus
SELECT * FROM armory_weapon  # 37 (Weapons)
select count(item_ptr_id) from armory_weapon
# Total = 137 Weapons (Not Weapons)

""" OR"""
SELECT
    COUNT(DISTINCT armory_weapon.item_ptr_id) AS are_weapons,
    COUNT(DISTINCT armory_item.item_id) - COUNT(DISTINCT armory_weapon.item_ptr_id) AS not_weapons
FROM
    armory_item,
    armory_weapon

# Output: 
# are_weapons: 37, not_weapons: 137

### How many Items does each character have? (Return first 20 rows)
SELECT
    character_id,
    COUNT(DISTINCT item_id) AS num_items
FROM
    charactercreator_character_inventory
GROUP BY
    character_id
LIMIT
    20


# Output:    
# Ranges from 1-5 items per character. 
    
### How many Weapons does each character have? (Return first 20 rows)
SELECT
    charactercreator_character_inventory.character_id,
    COUNT(
        DISTINCT charactercreator_character_inventory.item_id
    ) AS weapons_count
FROM
    charactercreator_character_inventory
    LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
    INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY
    charactercreator_character_inventory.character_id
LIMIT
    20

# Output:
# Each character can have anywhere from 1-3 weapons

### On average, how many Items does each Character have?
SELECT
    AVG(Items_Count) AS Average_Items
FROM
    (
        SELECT
            COUNT(DISTINCT item_id) AS Items_Count
        FROM
            charactercreator_character_inventory
        GROUP BY
            character_id
    )

# Output:
# 2.97350993377483 is the avg. number of items for each character

# On average, how many Weapons does each character have?
SELECT
    AVG(Weapons_Count) AS Average_Weapons
FROM
    (
        SELECT
            COUNT(
                DISTINCT charactercreator_character_inventory.item_id
            ) AS Weapons_Count
        FROM
            charactercreator_character_inventory
            LEFT JOIN armory_item ON charactercreator_character_inventory.item_id = armory_item.item_id
            INNER JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
        GROUP BY
            charactercreator_character_inventory.character_id
    )

# Output: 
# 1.30967741935484 is the avg. number of weapons for each character