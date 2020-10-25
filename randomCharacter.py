import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


def race_class():
    races = ['elf', 'dwarf', 'human', 'half-elf', 'half-orc', 'gnome', 'halfling', 'dragonborn', 'tiefling', 'goliath',
             'genasi', 'triton', 'kobold', 'bugbear']
    classes = ['barbarian', 'wizard', 'paladin', 'bard', 'sorceror', 'rogue', 'fighter', 'cleric', 'druid', 'monk',
               'ranger', 'warlock']
    alignments = ['lawful good', 'lawful neutral', 'lawful evil', 'neutral good', 'true neutral', 'neutral evil',
                  'chaotic good', 'chaotic neutral', 'chaotic evil']
    ages = ['child', 'young', 'adult', 'middle-aged', 'older']
    ch_race = random.choice(races)
    ch_class = random.choice(classes)
    ch_align = random.choice(alignments)
    ch_age = random.choice(ages)
    character = f'```Your {ch_age} {ch_race} {ch_class} is {ch_align}.```'
    return character


def stat_roll():
    stats = [[], [], [], [], [], [], []]
    newList = []
    for each in stats:
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
    for each in stats:
        each.remove(min(each))
        newList.append(sum(each))
    newList.remove(min(newList))
    return f'```Your stats are {newList[0]} {newList[1]} {newList[2]} {newList[3]} {newList[4]} {newList[5]}.```'


def full_character():
    """
    TODO: build a function that builds an entire character, including assigned stats
    :return:
    """
    # RACE AND CLASS
    races = ['elf', 'dwarf', 'human', 'half-elf', 'half-orc', 'gnome', 'halfling', 'dragonborn', 'tiefling', 'goliath',
             'genasi', 'triton', 'kobold', 'bugbear']
    classes = ['barbarian', 'wizard', 'paladin', 'bard', 'sorceror', 'rogue', 'fighter', 'cleric', 'druid', 'monk',
               'ranger', 'warlock']
    alignments = ['lawful good', 'lawful neutral', 'lawful evil', 'neutral good', 'true neutral', 'neutral evil',
                  'chaotic good', 'chaotic neutral', 'chaotic evil']
    ages = ['child', 'young', 'adult', 'middle-aged', 'older']
    ch_race = random.choice(races)
    ch_class = random.choice(classes)
    ch_align = random.choice(alignments)
    ch_age = random.choice(ages)
    race_and_class = f'Your {ch_age} {ch_race} {ch_class} is {ch_align}.'
    # BACKGROUND AND FEATURE
    backgrounds = {'acolyte': 'shelter of the faithful', 'criminal/spy': 'criminal contact',
                   'folk hero': 'rustic hospitality', 'noble': 'position of privilege', 'sage': 'researcher',
                   'soldier': 'military rank', 'charlatan': 'false identity', 'entertainer': 'by popular demand',
                   'gladiator': 'by popular demand', 'guild artisan / guild merchant': 'guild membership',
                   'hermit': 'discovery', 'knight': 'retainers', 'outlander': 'wanderer', 'pirate': 'bad reputation',
                   'sailor': 'ships passage', 'urchin': 'city secrets'}
    char_background = random.choice(list(backgrounds))
    char_feat = backgrounds[char_background]
    back_feat = f'Your background is {char_background}, which grants you {char_feat}.'
    # STAT GENERATION AND ASSIGNMENT
    stats = [[], [], [], [], [], [], []]
    newList = []
    for each in stats:
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
    for each in stats:
        each.remove(min(each))
        newList.append(sum(each))
    newList.remove(min(newList))
    if ch_class == 'barbarian':
        abilities = {'Constitution': sorted(newList)[5], 'Strength': sorted(newList)[4]}
    elif ch_class == 'bard':
        abilities = {'Charisma': sorted(newList)[5], 'Intelligence': sorted(newList)[4]}
    elif ch_class == 'cleric':
        abilities = {'Wisdom': sorted(newList)[5], 'Charisma': sorted(newList)[4]}
    elif ch_class == 'druid':
        abilities = {'Wisdom': sorted(newList)[5], 'Dexterity': sorted(newList)[4]}
    elif ch_class == 'fighter':
        abilities = {'Strength': sorted(newList)[5], 'Constitution': sorted(newList)[4]}
    elif ch_class == 'monk':
        abilities = {'Dexterity': sorted(newList)[5], 'Wisdom': sorted(newList)[4]}
    elif ch_class == 'paladin':
        abilities = {'Charisma': sorted(newList)[5], 'Strength': sorted(newList)[4]}
    elif ch_class == 'ranger':
        abilities = {'Strength': sorted(newList)[5], 'Dexterity': sorted(newList)[4]}
    elif ch_class == 'rogue':
        abilities = {'Dexterity': sorted(newList)[5], 'Charisma': sorted(newList)[4]}
    elif ch_class == 'sorcerer':
        abilities = {'Constitution': sorted(newList)[5], 'Intelligence': sorted(newList)[4]}
    elif ch_class == 'warlock':
        abilities = {'Intelligence': sorted(newList)[5], 'Constitution': sorted(newList)[4]}
    elif ch_class == 'wizard':
        abilities = {'Intelligence': sorted(newList)[5], 'Wisdom': sorted(newList)[4]}
    stat_assign = ''
    for each in abilities:
        stat_assign += f'{each}: {str(abilities[each])}\n'
    # RETURN STATEMENT
    return f'```' \
           f'{race_and_class} \n' \
           f'{back_feat} \n' \
           f'{stat_assign}' \
           f'with remaining stats {sorted(newList)[3]}, {sorted(newList)[2]}, {sorted(newList)[1]}, ' \
           f'{sorted(newList)[0]}.' \
           f'```'


def help_message():
    return '''```Welcome to randomCharacter
enter "!dnd" to get the attention of the bot.
in the same message include your command:
    "character" generates a character for you.
    "stats" gives you an array of stats. 4d6 are rolled seven times. The 
        lowest die is dropped from each group, and the lowest group is
        dropped. This tends to build more powerful characters.
    "background" generates a background and feature for you.
    "help" shows you this message.```'''


def background():
    backgrounds = {'acolyte': 'shelter of the faithful', 'criminal/spy': 'criminal contact',
                   'folk hero': 'rustic hospitality', 'noble': 'position of privilege', 'sage': 'researcher',
                   'soldier': 'military rank', 'charlatan': 'false identity', 'entertainer': 'by popular demand',
                   'gladiator': 'by popular demand', 'guild artisan / guild merchant': 'guild membership',
                   'hermit': 'discovery', 'knight': 'retainers', 'outlander': 'wanderer', 'pirate': 'bad reputation',
                   'sailor': 'ships passage', 'urchin': 'city secrets'}
    return f'```Your background is {random.choice(list(backgrounds))}, which grants you {backgrounds[bg]}.```'


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
