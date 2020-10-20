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
    character = f'```Your {random.choice(ages)} {random.choice(races)} {random.choice(classes)} is ' \
                f'{random.choice(alignments)}.```'
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


def help_message():
    return '''```Welcome to randomCharacter
enter "!dnd" to get the attention of the bot.
in the same message include your command:
    "character" generates a character for you.
    "stats" gives you an array of stats. 4d6 are rolled seven times. The lowest die is dropped from each group, and the lowest group is dropped. This tends to build more powerful characters.
    "background" generates a background and feature for you.
    "help" shows you this message.```'''


def background():
    backgrounds = {'acolyte': 'shelter of the faithful', 'criminal/spy': 'criminal contact',
                   'folk hero': 'rustic hospitality', 'noble': 'position of privilege', 'sage': 'researcher',
                   'soldier': 'military rank'}
    bg = random.choice(list(backgrounds))
    feature = backgrounds[bg]
    return f'```Your background is {bg}, which grants you {feature}.```'


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    user = str(message.author)
    if message.author == client.user:
        return

    if '!dnd' in message.content.lower():
        if 'character' in message.content.lower():
            await message.channel.send(race_class())
        if 'stats' in message.content.lower():
            await message.channel.send(stat_roll())
        if 'background' in message.content.lower():
            await message.channel.send(background())
        if 'help' in message.content.lower():
            await message.channel.send(help_message())

client.run(TOKEN)
