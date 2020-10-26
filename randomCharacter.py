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
    # generate 4 d6 rolls for each stat (6 stats)
    for each in stats:
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
        each.append(random.randint(1, 6))
    # remove the lowest roll from each group and collect the remaining sums into a list of ability scores
    for each in stats:
        each.remove(min(each))
        stat_list.append(sum(each))
    # make sure all stats are at least 8
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
    # TODO incorporate expanded skills (racial, class, subclass, etc)
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
    r_and_c_statement = f"{race_and_class} This character's class features are:\n"
    for each in classes[ch_class]:
        r_and_c_statement += f"    *    {each}\n"
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
    strh = abilities["Strength"]
    dexy = abilities["Dexterity"]
    conn = abilities["Constitution"]
    inte = abilities["Intelligence"]
    wism = abilities["Wisdom"]
    chaa = abilities["Charisma"]
    # RACIAL BONUSES
    if ch_race == 'dwarf':
        conn[0] += 2
        wism[0] += 1
    elif ch_race == 'dragonborn':
        strh[0] += 2
        chaa[0] += 1
    elif ch_race == 'elf':
        dexy[0] += 2
        wism[0] += 1
    elif ch_race == 'gnome':
        inte[0] += 2
        conn[0] += 1
    elif ch_race == 'halfling':
        dexy[0] += 2
        chaa[0] += 1
    elif ch_race == 'half-elf':
        chaa[0] += 2
    elif ch_race == 'half-orc':
        strh[0] += 2
        conn[0] += 1
    elif ch_race == 'human':
        for i in abilities:
            abilities[i][0] += 1
    elif ch_race == 'tiefling':
        chaa[0] += 2
        inte[0] += 1
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
    # STATEMENT OF STATS AND MODIFIERS
    stat_assign = f'STR: {strh[0]} ({strh[1]})     DEX: {dexy[0]} ({dexy[1]})\n' \
                  f'CON: {conn[0]} ({conn[1]})     INT: {inte[0]} ({inte[1]})\n' \
                  f'WIS: {wism[0]} ({wism[1]})     CHA: {chaa[0]} ({chaa[1]})\n'
    if ch_race == 'half-elf':
        stat_assign += 'Racial Bonus: +1 bonus to two abilities (not charisma, which has already been raised by 2)\n'
    # UNIQUE STARTING ITEM
    starters = ['A mummified goblin hand', 'A piece of crystal that faintly glows in the moonlight',
                'A gold coin minted in an unknown land', "A diary written in a language you don’t know",
                'A brass ring that never tarnishes', 'An old chess piece made from glass',
                'A pair of knucklebone dice, each with a skull symbol on the side that would normally show six pips',
                'A small idol depicting a nightmarish creature that gives you unsettling dreams when you sleep near it',
                'A rope necklace from which dangles four mummified elf fingers',
                'The deed for a parcel of land in a realm unknown to you',
                'A 1-ounce block made from an unknown material', 'A small cloth doll skewered with needles',
                'A tooth from an unknown beast', 'An enormous scale, perhaps from a dragon', 'A bright green feather',
                'An old divination card bearing your likeness', 'A glass orb filled with moving smoke',
                'A 1-pound egg with a bright red shell', 'A pipe that blows bubbles',
                'A glass jar containing a weird bit of flesh floating in pickling fluid',
                'A tiny gnome-crafted music box that plays a song you dimly remember from your childhood',
                'A small wooden statuette of a smug halfling', 'A brass orb etched with strange runes',
                'A multicolored stone disk', 'A tiny silver icon of a raven',
                'A bag containing forty-seven humanoid teeth, one of which is rotten',
                'A shard of obsidian that always feels warm to the touch',
                "A dragon's bony talon hanging from a plain leather necklace", 'A pair of old socks',
                'A blank book whose pages refuse to hold ink, chalk, graphite, or any other substance or marking',
                'A silver badge in the shape of a five-pointed star', 'A knife that belonged to a relative',
                'A glass vial filled with nail clippings',
                'A rectangular metal device with two tiny metal cups on one end that throws sparks when wet',
                'A white, sequined glove sized for a human', 'A vest with one hundred tiny pockets',
                'A small, weightless stone block', 'A tiny sketch portrait of a goblin',
                'An empty glass vial that smells of perfume when opened',
                'A gemstone that looks like a lump of coal when examined by anyone but you',
                'A scrap of cloth from an old banner', 'A rank insignia from a lost legionnaire',
                'A tiny silver bell without a clapper', 'A mechanical canary inside a gnome-crafted lamp',
                'A tiny chest carved to look like it has numerous feet on the bottom',
                'A dead sprite inside a clear glass bottle',
                'A metal can that has no opening but sounds as if it is filled with liquid, sand, spiders, or broken '
                'glass (your choice)', 'A glass orb filled with water, in which swims a clockwork goldfish',
                'A silver spoon with an M engraved on the handle', 'A whistle made from gold-colored wood',
                'A dead scarab beetle the size of your hand', 'Two toy soldiers, one with a missing head',
                'A small box filled with different-sized buttons', 'A candle that can’t be lit',
                'A tiny cage with no door', 'An old key', 'An indecipherable treasure map', 'A hilt from a broken sword',
                'A rabbit’s foot', 'A glass eye', 'A cameo carved in the likeness of a hideous person',
                'A silver skull the size of a coin', 'An alabaster mask',
                'A pyramid of sticky black incense that smells very bad',
                'A nightcap that, when worn, gives you pleasant dreams', 'A single caltrop made from bone',
                'A gold monocle frame without the lens', 'A 1-inch cube, each side painted a different color',
                'A crystal knob from a door', 'A small packet filled with pink dust',
                'A fragment of a beautiful song, written as musical notes on two pieces of parchment',
                'A silver teardrop earring made from a real teardrop',
                'The shell of an egg painted with scenes of human misery in disturbing detail',
                'A fan that, when unfolded, shows a sleeping cat', 'A set of bone pipes',
                'A four-leaf clover pressed inside a book discussing manners and etiquette',
                'A sheet of parchment upon which is drawn a complex mechanical contraption',
                'An ornate scabbard that fits no blade you have found so far',
                'An invitation to a party where a murder happened',
                "A bronze pentacle with an etching of a rat's head in its center",
                'A purple handkerchief embroidered with the name of a powerful archmage',
                'Half of a floorplan for a temple, castle, or some other structure',
                'A bit of folded cloth that, when unfolded, turns into a stylish cap',
                'A receipt of deposit at a bank in a far-flung city', 'A diary with seven missing pages',
                'An empty silver snuffbox bearing an inscription on the surface that says “dreams”',
                'An iron holy symbol devoted to an unknown god',
                "A book that tells the story of a legendary hero's rise and fall, with the last chapter missing",
                'A vial of dragon blood', 'An ancient arrow of elven design', 'A needle that never bends',
                'An ornate brooch of dwarven design',
                'An empty wine bottle bearing a pretty label that says, “The Wizard of Wines Winery, Red Dragon Crush, '
                '331422-W”', 'A mosaic tile with a multicolored, glazed surface', 'A petrified mouse',
                "A black pirate flag adorned with a dragon's skull and crossbones",
                "A tiny mechanical crab or spider that moves about when it’s not being observed",
                'A glass jar containing lard with a label that reads, “Griffon Grease”',
                'A wooden box with a ceramic bottom that holds a living worm with a head on each end of its body',
                'A metal urn containing the ashes of a hero']
    start_item = random.choice(starters)
    start_statement = f'Among your belongings, some might find this interesting or unique:\n    *    {start_item}'
    # RETURN STATEMENT
    return f'```{r_and_c_statement} \n' \
           f'{back_feat} \n' \
           f'{stat_assign} \n' \
           f'{start_statement} ```'


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
