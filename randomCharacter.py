import os
import random
import discord
from dotenv import load_dotenv

# initialize dotenv, which will read data from a .env file
load_dotenv()
# retrieve discord token from .env file
TOKEN = os.getenv('DISCORD_TOKEN')
# set shortcut for ease of launching and listening
client = discord.Client()


# function that returns an age, race, class, alignment and list of class features for a random character
def race_class():
    races = ['elf', 'dwarf', 'human', 'half-elf', 'half-orc', 'gnome', 'halfling', 'dragonborn', 'tiefling']
    # dictionary keys are classes and values are lists of class features
    classes = {'barbarian': ('rage', 'unarmored defense'), 'wizard': ('spellcasting', 'arcane recovery'),
               'paladin': ('divine sense', 'lay on hands'), 'bard': ('spellcasting', 'bardic inspiration'),
               'sorcerer': ('spellcasting', 'sorcerous origin'),
               'rogue': ('expertise', 'sneak attack', "thieve's cant"), 'fighter': ('fighting style', 'second wind'),
               'cleric': ('spellcasting', 'divine domain'), 'druid': ('druidic', 'spellcasting'),
               'monk': ('unarmored defense', 'martial arts'),
               'ranger': ('favored enemy', 'natural explorer'), 'warlock': ('otherwordly patron', 'pact magic')}
    alignments = ['lawful good', 'lawful neutral', 'lawful evil', 'neutral good', 'true neutral', 'neutral evil',
                  'chaotic good', 'chaotic neutral', 'chaotic evil']
    ages = ['child', 'teen', 'adult', 'middle-aged', 'older']
    ch_race = random.choice(races)
    ch_class = random.choice(list(classes.keys()))
    ch_align = random.choice(alignments)
    ch_age = random.choice(ages)
    character = f'Your {ch_age} {ch_race} {ch_class} is {ch_align}.'
    statement = f"```{character} This character's class features are:\n"
    # list out each class feature
    for each in classes[ch_class]:
        statement += f"    *    {each}\n"
    statement += '```'
    return statement


def stat_roll():
    stats = [[], [], [], [], [], []]
    stat_list = []
    for each in stats:
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
    for each in stats:
        each.remove(min(each))
        stat_list.append(sum(each))
    # for each in stat_list:
    for item in stat_list:
        if item < 8:
            stat_list[item] = 8
    return f'```Your stats are {stat_list[0]} {stat_list[1]} {stat_list[2]} {stat_list[3]} {stat_list[4]} {stat_list[5]}.```'


def background():
    backgrounds = {'acolyte': 'shelter of the faithful', 'criminal/spy': 'criminal contact',
                   'folk hero': 'rustic hospitality', 'noble': 'position of privilege', 'sage': 'researcher',
                   'soldier': 'military rank', 'charlatan': 'false identity', 'entertainer': 'by popular demand',
                   'gladiator': 'by popular demand', 'guild artisan / guild merchant': 'guild membership',
                   'hermit': 'discovery', 'knight': 'retainers', 'outlander': 'wanderer', 'pirate': 'bad reputation',
                   'sailor': 'ships passage', 'urchin': 'city secrets'}
    char_bg = random.choice(list(backgrounds))
    char_feat = backgrounds[char_bg]
    return f'```Your background is {char_bg}, which grants you {char_feat}.```'


def full_character():
    # TODO incorporate expanded skills
    # TODO initiative, proficiency bonus
    # TODO expand on background and feature
    # RACE AND CLASS
    races = ['elf', 'dwarf', 'human', 'half-elf', 'half-orc', 'gnome', 'halfling', 'dragonborn', 'tiefling']
    classes = {'barbarian': ('rage', 'unarmored defense'), 'wizard': ('spellcasting', 'arcane recovery'),
               'paladin': ('divine sense', 'lay on hands'), 'bard': ('spellcasting', 'bardic inspiration'),
               'sorcerer': ('spellcasting', 'sorcerous origin'),
               'rogue': ('expertise', 'sneak attack', "thieve's cant"),
               'fighter': ('fighting style', 'second wind'), 'cleric': ('spellcasting', 'divine domain'),
               'druid': ('druidic', 'spellcasting'), 'monk': ('unarmored defense', 'martial arts'),
               'ranger': ('favored enemy', 'natural explorer'), 'warlock': ('otherwordly patron', 'pact magic')}
    alignments = ['lawful good', 'lawful neutral', 'lawful evil', 'neutral good', 'true neutral', 'neutral evil',
                  'chaotic good', 'chaotic neutral', 'chaotic evil']
    ages = ['child', 'young', 'adult', 'middle-aged', 'older']
    ch_race = random.choice(races)
    ch_class = random.choice(list(classes.keys()))
    ch_align = random.choice(alignments)
    ch_age = random.choice(ages)
    race_and_class = f'Your {ch_age} {ch_race} {ch_class} is {ch_align}.'
    randcstatement = f"{race_and_class} This character's class features are:\n"
    for each in classes[ch_class]:
        randcstatement += f"    *    {each}\n"
    # BACKGROUND AND FEATURE
    backgrounds = {'acolyte': 'shelter of the faithful', 'criminal/spy': 'criminal contact',
                   'folk hero': 'rustic hospitality', 'noble': 'position of privilege', 'sage': 'researcher',
                   'soldier': 'military rank', 'charlatan': 'false identity', 'entertainer': 'by popular demand',
                   'gladiator': 'by popular demand', 'guild artisan / guild merchant': 'guild membership',
                   'hermit': 'discovery', 'knight': 'retainers', 'outlander': 'wanderer', 'pirate': 'bad reputation',
                   'sailor': 'ships passage', 'urchin': 'city secrets'}
    char_background = random.choice(list(backgrounds))
    char_feat = backgrounds[char_background]
    back_feat = f'Your background is {char_background}, which grants you "{char_feat}."\n'
    # STAT GENERATION AND ASSIGNMENT
    stats = [[], [], [], [], [], []]
    stat_list = []
    for each in stats:
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
    for each in stats:
        each.remove(min(each))
        stat_list.append(sum(each))
    for each in stat_list:
        if each < 8:
            each = 8
    if ch_class == 'barbarian':
        abilities = {'Constitution': [sorted(stat_list)[5], 0], 'Strength': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Charisma': [sorted(stat_list)[2], 0],
                     'Wisdom': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'bard':
        abilities = {'Charisma': [sorted(stat_list)[5], 0], 'Intelligence': [sorted(stat_list)[4], 0],
                     'Constitution': [sorted(stat_list)[3], 0], 'Dexterity': [sorted(stat_list)[2], 0],
                     'Wisdom': [sorted(stat_list)[1], 0], 'Strength': [sorted(stat_list)[0], 0]}
    elif ch_class == 'cleric':
        abilities = {'Wisdom': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Strength': [sorted(stat_list)[2], 0],
                     'Charisma': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'druid':
        abilities = {'Wisdom': [sorted(stat_list)[5], 0], 'Dexterity': [sorted(stat_list)[4], 0],
                     'Constitution': [sorted(stat_list)[3], 0], 'Intelligence': [sorted(stat_list)[2], 0],
                     'Strength': [sorted(stat_list)[1], 0], 'Charisma': [sorted(stat_list)[0], 0]}
    elif ch_class == 'fighter':
        abilities = {'Strength': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Wisdom': [sorted(stat_list)[2], 0],
                     'Intelligence': [sorted(stat_list)[1], 0], 'Charisma': [sorted(stat_list)[0], 0]}
    elif ch_class == 'monk':
        abilities = {'Dexterity': [sorted(stat_list)[5], 0], 'Wisdom': [sorted(stat_list)[4], 0],
                     'Constitution': [sorted(stat_list)[3], 0], 'Strength': [sorted(stat_list)[2], 0],
                     'Charisma': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'paladin':
        abilities = {'Strength': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Charisma': [sorted(stat_list)[2], 0],
                     'Wisdom': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'ranger':
        abilities = {'Dexterity': [sorted(stat_list)[5], 0], 'Wisdom': [sorted(stat_list)[4], 0],
                     'Constitution': [sorted(stat_list)[3], 0], 'Charisma': [sorted(stat_list)[2], 0],
                     'Strength': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'rogue':
        abilities = {'Dexterity': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Charisma': [sorted(stat_list)[3], 0], 'Wisdom': [sorted(stat_list)[2], 0],
                     'Strength': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'sorcerer':
        abilities = {'Charisma': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Wisdom': [sorted(stat_list)[3], 0], 'Dexterity': [sorted(stat_list)[2], 0],
                     'Intelligence': [sorted(stat_list)[1], 0], 'Strength': [sorted(stat_list)[0], 0]}
    elif ch_class == 'warlock':
        abilities = {'Charisma': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Wisdom': [sorted(stat_list)[2], 0],
                     'Strength': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'wizard':
        abilities = {'Intelligence': (sorted(stat_list)[5], 0), 'Constitution': (sorted(stat_list)[4], 0),
                     'Dexterity': (sorted(stat_list)[3], 0), 'Wisdom': (sorted(stat_list)[2], 0),
                     'Charisma': (sorted(stat_list)[1], 0), 'Strength': (sorted(stat_list)[0], 0)}
    # RACIAL BONUSES
    if ch_race == 'dwarf':
        abilities['Constitution'][0] += 2
        abilities['Wisdom'][0] += 1
    elif ch_race == 'dragonborn':
        abilities['Strength'][0] += 2
        abilities['Charisma'][0] += 1
    elif ch_race == 'elf':
        abilities['Dexterity'][0] += 2
        abilities['Wisdom'][0] += 1
    elif ch_race == 'gnome':
        abilities['Intelligence'][0] += 2
        abilities['Constitution'][0] += 1
    elif ch_race == 'halfling':
        abilities['Dexterity'][0] += 2
        abilities['Charisma'][0] += 1
    elif ch_race == 'half-elf':
        abilities['Charisma'][0] += 2
    elif ch_race == 'half-orc':
        abilities['Strength'][0] += 2
        abilities['Constitution'][0] += 1
    elif ch_race == 'human':
        for i in abilities:
            abilities[i][0] += 1
    elif ch_race == 'tiefling':
        abilities['Charisma'][0] += 2
        abilities['Intelligence'][0] += 1
    # FIGURE AND INCLUDE STAT MODIFIERS
    for each in abilities:
        if abilities[each][0] <= 9:
            abilities[each][1] = -1
        elif abilities[each][0] <= 11:
            abilities[each][1] = 0
        elif abilities[each][0] <= 13:
            abilities[each][1] = 1
        elif abilities[each][0] <= 15:
            abilities[each][1] = 2
        elif abilities[each][0] <= 17:
            abilities[each][1] = 3
        elif abilities[each][0] <= 19:
            abilities[each][1] = 4
        elif abilities[each][0] == 20:
            abilities[each][1] = 5
    STR = abilities["Strength"]
    DEX = abilities["Dexterity"]
    CON = abilities["Constitution"]
    INT = abilities["Intelligence"]
    WIS = abilities["Wisdom"]
    CHA = abilities["Charisma"]
    stat_assign = f'STR: {STR[0]} ({STR[1]})     DEX: {DEX[0]} ({DEX[1]})\n' \
                  f'CON: {CON[0]} ({CON[1]})     INT: {INT[0]} ({INT[1]})\n' \
                  f'WIS: {WIS[0]} ({WIS[1]})     CHA: {CHA[0]} ({CHA[1]})\n'
    if ch_race == 'half-elf':
        stat_assign += 'Racial Bonus: +1 bonus to two abilities (not charisma, which has already been raised by 2)\n'
    # RETURN STATEMENT
    return f'```{randcstatement} \n' \
           f'{back_feat} \n' \
           f'{stat_assign}```'


def help_message():
    return '''```Welcome to randomCharacter
enter "!dnd" to get the attention of the bot.
in the same message include your command:
    "character" generates a character for you.
    "stats" gives you an array of stats. 
        * 4d6 are rolled six times. 
        * The lowest die is dropped from each group. 
        * Stats lower than 8, simply become 8.
    "background" generates a background and feature for you.
    "help" shows you this message.
This bot assumes you are creating a character of level 1.```'''


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    user = str(message.author)
    if message.author == client.user:
        return

    if '!dnd' in message.content.lower():
        if ' character' in message.content.lower():
            await message.channel.send(race_class())
            print(f'{user} generated a character.')
        if ' stats' in message.content.lower():
            await message.channel.send(stat_roll())
            print(f'{user} generated a stat roll')
        if ' background' in message.content.lower():
            await message.channel.send(background())
            print(f'{user} generated a background')
        if ' fullcharacter' in message.content.lower():
            await message.channel.send(full_character())
        if ' help' in message.content.lower():
            await message.channel.send(help_message())
            print(f'{user} asked for help')


client.run(TOKEN)
