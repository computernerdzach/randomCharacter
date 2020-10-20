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
    stat1 = []
    stat2 = []
    stat3 = []
    stat4 = []
    stat5 = []
    stat6 = []
    stat7 = []
    stats = [stat1, stat2, stat3, stat4, stat5, stat6, stat7]
    for each in stats:
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
    for each in stats:
        each.remove(min(each))
    newList = []
    for each in stats:
        newList.append(sum(each))
    newList.remove(min(newList))
    string = f'```Your stats are {newList[0]} {newList[1]} {newList[2]} {newList[3]} {newList[4]} {newList[5]}```'
    return string


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

client.run(TOKEN)
