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
    # TODO: expand on background and feature
    # TODO: Saving throws
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
    r_and_c_statement = f"{race_and_class} Their class features are:\n"
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
    for i, s in enumerate(stat_list):
        if s < 8:
            stat_list[i] = 8

    # piggy backing on to the stat assignment, we're going to add spell selection for casters
    ch_cantrips_num = 0
    ch_lvl1_spl_num = 0
    ch_spl_slot_num = 0
    ch_known_spells = {'cantrips': [], 'level 1': []}

    # for each class, initialize a stat dictionary, keys are stat names, values are a list:
    # index 0 is the total stat score
    # index 1 is the modifier, initialized to 0, later updated based on stat score
    # each class assigns the stats highest to lowest based on class needs... this may need to be updated
    if ch_class == 'barbarian':
        abilities = {'Constitution': [sorted(stat_list)[5], 0], 'Strength': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Charisma': [sorted(stat_list)[2], 0],
                     'Wisdom': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
    elif ch_class == 'bard':
        abilities = {'Charisma': [sorted(stat_list)[5], 0], 'Intelligence': [sorted(stat_list)[4], 0],
                     'Constitution': [sorted(stat_list)[3], 0], 'Dexterity': [sorted(stat_list)[2], 0],
                     'Wisdom': [sorted(stat_list)[1], 0], 'Strength': [sorted(stat_list)[0], 0]}
        ch_cantrips_num += 2
        ch_lvl1_spl_num += 4
        ch_spl_slot_num += 2
        bard_cants = ['blade ward', 'dancing lights', 'friends', 'light', 'mage hand', 'mending', 'message',
                      'minor illusion', 'prestidigitation', 'true strike', 'vicious mockery']
        bard_spel1 = ['animal friendship', 'bane', 'charm person', 'comprehend language', 'cure wounds',
                      'detect magic', 'disguise self', 'dissonant whispers', 'faerie fire', 'feather fall',
                      'healing word', 'heroism', "Tasha's hideous laghter", 'identify', 'illusory script',
                      'longstrider', 'silent image', 'sleep', 'speak with animals', 'thunderwave', 'unseen servant']
        ch_known_spells['cantrips'].append(list(random.sample(bard_cants, ch_cantrips_num)))
        ch_known_spells['level 1'].append(list(random.sample(bard_spel1, ch_lvl1_spl_num)))
    elif ch_class == 'cleric':
        abilities = {'Wisdom': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Strength': [sorted(stat_list)[2], 0],
                     'Charisma': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
        ch_cantrips_num += 3
        ch_lvl1_spl_num += abilities['Wisdom'][1] + 1
        ch_spl_slot_num += 2
        cler_cants = ['guidance', 'light', 'mending', 'resistance', 'sacred flame', 'spare the dying', 'thaumaturgy']
        cler_spel1 = ['bane', 'bless', 'command', 'create or destroy water', 'cure wounds', 'detect evil and good',
                      'detect magic', 'detect poison and disease', 'guiding bold', 'healing word', 'inflict wounds',
                      'protection from evil and good', 'purify food and drink', "sanctuary", 'shield of faith']
        ch_known_spells['cantrips'].append(list(random.sample(cler_cants, ch_cantrips_num)))
        ch_known_spells['level 1'].append(list(random.sample(cler_spel1, ch_lvl1_spl_num)))
    elif ch_class == 'druid':
        abilities = {'Wisdom': [sorted(stat_list)[5], 0], 'Dexterity': [sorted(stat_list)[4], 0],
                     'Constitution': [sorted(stat_list)[3], 0], 'Intelligence': [sorted(stat_list)[2], 0],
                     'Strength': [sorted(stat_list)[1], 0], 'Charisma': [sorted(stat_list)[0], 0]}
        ch_cantrips_num += 2
        ch_lvl1_spl_num += abilities['Wisdom'][1] + 1
        ch_spl_slot_num += 2
        drui_cants = ['druidcraft', 'guidance', 'mending', 'poison spray', 'produce flame', 'resistance', 'shillelagh',
                      'thorn whip']
        drui_spel1 = ['animal friendship', 'charm person', 'create or destroy water', 'cure wounds',
                      'detect magic', 'detect poison and disease', 'entangle', 'faerie fire', 'fog cloud',
                      'goodberry', 'healing word', "jump", 'longstrider', 'purify food and drink',
                      'speak with animals', 'thunderwave']
        ch_known_spells['cantrips'].append(list(random.sample(drui_cants, ch_cantrips_num)))
        ch_known_spells['level 1'].append(list(random.sample(drui_spel1, ch_lvl1_spl_num)))
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
        ch_cantrips_num += 4
        ch_lvl1_spl_num += 2
        ch_spl_slot_num += 2
        sorc_cants = ['acid splash', 'blade ward', 'chill touch', 'dancing lights', 'fire bolt', 'friends', 'light',
                      'mage hand', 'mending', 'message', 'minor illusion', 'poison spray', 'prestidigitation',
                      'ray of frost', 'shocking grasp', 'true strike']
        sorc_spel1 = ['burning hands', 'charm person', 'chromatic orb', 'color spray', 'comprehend language',
                      'detect magic', 'disguise self', 'expeditious retreat', 'false life', 'feather fall',
                      'fogcloud', 'jump', 'mage armor', 'magic missile', 'ray of sickness', 'shield', 'silent image',
                      'sleep', 'thunderwave', 'witch bolt']
        ch_known_spells['cantrips'].append(list(random.sample(sorc_cants, ch_cantrips_num)))
        ch_known_spells['level 1'].append(list(random.sample(sorc_spel1, ch_lvl1_spl_num)))
    elif ch_class == 'warlock':
        abilities = {'Charisma': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Wisdom': [sorted(stat_list)[2], 0],
                     'Strength': [sorted(stat_list)[1], 0], 'Intelligence': [sorted(stat_list)[0], 0]}
        ch_cantrips_num += 2
        ch_lvl1_spl_num += 2
        ch_spl_slot_num += 1
        warl_cants = ['blade ward', 'chill touch', 'eldritch blast', 'friends', 'mage hand', 'minor illusion',
                      'poison spray', 'prestidigitation', 'true strike']
        warl_spel1 = ['armor of Agathys', 'arms of Hadar', 'charm person', 'comprehend language', 'expeditious retreat',
                      'hellish rebuke', 'hex', 'illusory script', 'protection from evil and good', 'unseen servant',
                      'witch bolt']
        ch_known_spells['cantrips'].append(list(random.sample(warl_cants, ch_cantrips_num)))
        ch_known_spells['level 1'].append(list(random.sample(warl_spel1, ch_lvl1_spl_num)))
    elif ch_class == 'wizard':
        abilities = {'Intelligence': [sorted(stat_list)[5], 0], 'Constitution': [sorted(stat_list)[4], 0],
                     'Dexterity': [sorted(stat_list)[3], 0], 'Wisdom': [sorted(stat_list)[2], 0],
                     'Charisma': [sorted(stat_list)[1], 0], 'Strength': [sorted(stat_list)[0], 0]}
        ch_cantrips_num += 3
        ch_lvl1_spl_num += abilities['Intelligence'][1] + 1
        ch_spl_slot_num += 2
        wizd_cants = ['acid splash', 'blade ward', 'chill touch', 'dancing lights', 'fire bolt', 'friends', 'light',
                      'mage hand', 'mending', 'message', 'minor illusion', 'poison spray', 'prestidigitation',
                      'ray of frost', 'shocking grasp', 'true strike']
        wizd_spel1 = ['alarm', 'burning hands', 'charm person', 'chromatic orb', 'color spray', 'comprehend language',
                      'detect magic', 'disguise self', 'expeditious retreat', 'false life', 'feather fall',
                      'find familiar', 'floating disk', 'fogcloud', 'grease', "Tasha's hideous laughter", 'identify',
                      'illusory script', 'jump', 'longstrider', 'mage armor', 'magic missile',
                      'protection from evil and good', 'ray of sickness', 'shield', 'silent image', 'sleep',
                      'thunderwave', 'unseen servant', 'witch bolt']
        ch_known_spells['cantrips'].append(list(random.sample(wizd_cants, ch_cantrips_num)))
        ch_known_spells['level 1'].append(list(random.sample(wizd_spel1, ch_lvl1_spl_num)))

    # printout for spells
    spell_statement = f'Your character knows {ch_cantrips_num} cantrips and {ch_lvl1_spl_num} level 1 spells.\n' \
                      f'You have {ch_spl_slot_num} level 1 spell slots.\n' \
                      f'Your spells are: \n'
    for each in ch_known_spells:
        spell_statement += f'{each} \n'
        for every in ch_known_spells[each]:
            spell_statement += f'    {every} \n'

    # variable shortcuts to refer to stat dictionary
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
        # half elf gets +2 to charisma and +1 to two other stats
        non_charisma_stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom"]
        h_elf_stats = random.sample(non_charisma_stats, 2)
        for each in h_elf_stats:
            abilities[each][0] += 1
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
    stat_assign = f'Here are your Abilities / (Modifiers)\n' \
                  f'    STR: {strh[0]} / ({strh[1]})    DEX: {dexy[0]} / ({dexy[1]})\n' \
                  f'    CON: {conn[0]} / ({conn[1]})    INT: {inte[0]} / ({inte[1]})\n' \
                  f'    WIS: {wism[0]} / ({wism[1]})    CHA: {chaa[0]} / ({chaa[1]})\n'

    # nested dictionary, outer key is stat, inner key is ability and value is 0, will add modifier next
    exp_skills = {'Strength': {'athletics': 0}, 'Dexterity': {'acrobatics': 0, 'sleight of hand': 0, 'stealth': 0},
                  'Intelligence': {'arcana': 0, 'history': 0, 'investigation': 0, 'nature': 0, 'religion': 0},
                  'Wisdom': {'animal handling': 0, 'insight': 0, 'medicine': 0, 'perception': 0, 'survival': 0},
                  'Charisma': {'deception': 0, 'intimidation': 0, 'performance': 0, 'persuasion': 0}}
    all_skills = ['athletics', 'acrobatics', 'sleight of hand', 'stealth', 'arcana', 'history', 'investigation',
                  'nature', 'religion', 'animal handling', 'insight', 'medicine', 'perception', 'survival', 'deception',
                  'intimidation', 'performance', 'persuasion']
    # PROFICIENCIES assignment and calculation
    pro_bonus = {'none': 0, 'half': 1, 'proficient': 2, 'expert': 4}
    char_pros = []
    if ch_class == 'bard':
        char_pros += random.sample(all_skills, 3)
        for each in exp_skills:
            for every in exp_skills[each]:
                if not every in char_pros:
                    exp_skills[each][every] += pro_bonus['half']
                else:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'barbarian':
        barb_pros = ['animal handling', 'athletics', 'intimidation', 'nature', 'perception', 'survival']
        char_pros += random.sample(barb_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'cleric':
        cler_pros = ['history', 'insight', 'medicine', 'persuasion', 'religion']
        char_pros += random.sample(cler_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'druid':
        drui_pros = ['arcana', 'animal handling', 'insight', 'medicine', 'nature', 'perception', 'religion', 'survival']
        char_pros += random.sample(drui_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'fighter':
        figh_pros = ['acrobatics', 'animal handling', 'athletics', 'history', 'insight', 'intimidation', 'perception',
                     'survival']
        char_pros += random.sample(figh_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'monk':
        monk_pros = ['acrobatics', 'athletics', 'history', 'insight', 'religion', 'stealth']
        char_pros += random.sample(monk_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'paladin':
        pala_pros = ['athletics', 'insight', 'intimidation', 'medicine', 'persuasion', 'religion']
        char_pros += random.sample(pala_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'ranger':
        rang_pros = ['animal handling', 'athletics', 'insight', 'investigation', 'nature', 'perception', 'stealth',
                     'survival']
        char_pros += random.sample(rang_pros, 3)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'rogue':
        rogu_pros = ['acrobatics', 'athletics', 'deception', 'insight', 'intimidation', 'investigation', 'perception',
                     'performance', 'persuasion', 'sleight of hand', 'stealth']
        char_pros += random.sample(rogu_pros, 4)
        char_expert = []
        while len(char_expert) < 2:
            new_choice = random.choice(rogu_pros)
            if not new_choice in char_pros:
                char_expert.append(new_choice)
        for each in exp_skills:
            for every in exp_skills[each]:
                if (every in char_pros) and (not every in char_expert):
                    exp_skills[each][every] += pro_bonus['proficient']
                elif every in char_expert:
                    exp_skills[each][every] += pro_bonus['expert']
    elif ch_class == 'sorcerer':
        sorc_pros = ['arcana', 'deception', 'insight', 'intimidation', 'persuasion', 'religion']
        char_pros += random.sample(sorc_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'warlock':
        warl_pros = ['arcana', 'deception', 'history', 'intimidation', 'investigation', 'nature', 'religion']
        char_pros += random.sample(warl_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']
    elif ch_class == 'wizard':
        barb_pros = ['arcana', 'history', 'insight', 'investigation', 'medicine', 'religion']
        char_pros += random.sample(barb_pros, 2)
        for each in exp_skills:
            for every in exp_skills[each]:
                if every in char_pros:
                    exp_skills[each][every] += pro_bonus['proficient']

    # background proficiencies
    if char_background == 'acolyte':
        exp_skills['Wisdom']['insight'] += pro_bonus['proficient']
        exp_skills['Intelligence']['religion'] += pro_bonus['proficient']
    elif char_background == 'charlatan':
        exp_skills['Charisma']['deception'] += pro_bonus['proficient']
        exp_skills['Dexterity']['sleight of hand'] += pro_bonus['proficient']
    elif char_background == 'criminal/spy':
        exp_skills['Charisma']['deception'] += pro_bonus['proficient']
        exp_skills['Dexterity']['stealth'] += pro_bonus['proficient']
    elif char_background == 'entertainer':
        exp_skills['Dexterity']['acrobatics'] += pro_bonus['proficient']
        exp_skills['Charisma']['performance'] += pro_bonus['proficient']
    elif char_background == 'folk hero':
        exp_skills['Wisdom']['animal handling'] += pro_bonus['proficient']
        exp_skills['Wisdom']['survival'] += pro_bonus['proficient']
    elif char_background == 'gladiator':
        exp_skills['Dexterity']['acrobatics'] += pro_bonus['proficient']
        exp_skills['Charisma']['performance'] += pro_bonus['proficient']
    elif char_background == 'guild artisan / guild merchant':
        exp_skills['Wisdom']['insight'] += pro_bonus['proficient']
        exp_skills['Charisma']['persuasion'] += pro_bonus['proficient']
    elif char_background == 'hermit':
        exp_skills['Wisdom']['medicine'] += pro_bonus['proficient']
        exp_skills['Intelligence']['religion'] += pro_bonus['proficient']
    elif char_background == 'knight':
        exp_skills['Intelligence']['history'] += pro_bonus['proficient']
        exp_skills['Charisma']['persuasion'] += pro_bonus['proficient']
    elif char_background == 'noble':
        exp_skills['Intelligence']['history'] += pro_bonus['proficient']
        exp_skills['Charisma']['persuasion'] += pro_bonus['proficient']
    elif char_background == 'outlander':
        exp_skills['Strength']['athletics'] += pro_bonus['proficient']
        exp_skills['Wisdom']['survival'] += pro_bonus['proficient']
    elif char_background == 'pirate':
        exp_skills['Strength']['athletics'] += pro_bonus['proficient']
        exp_skills['Wisdom']['perception'] += pro_bonus['proficient']
    elif char_background == 'sage':
        exp_skills['Intelligence']['arcana'] += pro_bonus['proficient']
        exp_skills['Intelligence']['history'] += pro_bonus['proficient']
    elif char_background == 'sailor':
        exp_skills['Strength']['athletics'] += pro_bonus['proficient']
        exp_skills['Wisdom']['perception'] += pro_bonus['proficient']
    elif char_background == 'soldier':
        exp_skills['Strength']['athletics'] += pro_bonus['proficient']
        exp_skills['Charisma']['intimidation'] += pro_bonus['proficient']
    elif char_background == 'urchin':
        exp_skills['Dexterity']['sleight of hand'] += pro_bonus['proficient']
        exp_skills['Dexterity']['stealth'] += pro_bonus['proficient']

    # nested for loop to spread out ability scores
    for each in exp_skills:
        for every in abilities:
            if each == every:
                for skateboard in exp_skills[each]:
                    exp_skills[each][skateboard] += int(abilities[every][1])
    stat_assign += f'\nYour expanded skills are skill / score \n'
    for each in exp_skills:
        stat_assign += f'{each} \n'
        for every in exp_skills[each]:
            stat_assign += ' ' * (17 - len(every)) + every + f' / {exp_skills[each][every]} \n'

    # ASSIGN HP, AC, SPEED, INITIATIVE TODO finish
    armors = {'unarmored': 10, 'padded': 11, 'leather': 11, 'hide': 12, 'chain shirt': 13, 'ring': 14}
    char_ac = abilities['Dexterity'][1]
    char_hp = 0
    char_initiative = dexy[1]
    if ch_class == 'barbarian':
        char_ac += conn[1] + armors['unarmored']
        char_hp += 12 + conn[1]
        armor = 'unarmored'
    elif ch_class == 'monk':
        char_ac += wism[1] + armors['unarmored']
        char_hp += 8 + conn[1]
        armor = 'unarmored'
    elif ch_class == 'bard':
        char_ac += armors['padded']
        char_hp += 8 + conn[1]
        armor = 'padded'
        char_initiative += pro_bonus['half']
    elif ch_class == 'cleric':
        char_ac += armors['chain shirt']
        char_hp += 8 + conn[1]
        armor = 'chain shirt'
    elif ch_class == 'druid':
        char_ac += armors['hide']
        char_hp += 8 + conn[1]
        armor = 'hide'
    elif ch_class == 'fighter':
        char_ac += armors['ring']
        char_hp += 10 + conn[1]
        armor = 'ring'
    elif ch_class == 'paladin':
        char_ac += armors['ring']
        char_hp += 10 + conn[1]
        armor = 'ring'
    elif ch_class == 'ranger':
        char_ac += armors['chain shirt']
        char_hp += 10 + conn[1]
        armor = 'chain shirt'
    elif ch_class == 'rogue':
        char_ac += armors['leather']
        char_hp += 8 + conn[1]
        armor = 'leather'
    elif ch_class == 'warlock':
        char_ac += armors['padded']
        char_hp += 8 + conn[1]
        armor = 'padded'
    elif ch_class == 'sorcerer':
        char_hp += 6 + conn[1]
        char_ac += armors['unarmored']
        armor = 'unarmored'
    elif ch_class == 'wizard':
        char_hp += 6 + conn[1]
        char_ac += armors['unarmored']
        armor = 'unarmored'

    char_speed = 30
    if (ch_race == 'dwarf') or (ch_race == 'gnome') or (ch_race == 'halfling'):
        char_speed = 25

    ac_speed_statement = f'Your AC is {str(char_ac)} with {armor} for armor. Your HP is {char_hp}. \n'
    ac_speed_statement += f'Your base speed is {char_speed} and your initiative bonus is {char_initiative}. \n'

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
                'A tiny cage with no door', 'An old key', 'An indecipherable treasure map',
                'A hilt from a broken sword', 'A rabbit’s foot', 'A glass eye',
                'A cameo carved in the likeness of a hideous person', 'A silver skull the size of a coin',
                'An alabaster mask', 'A pyramid of sticky black incense that smells very bad',
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
           f'{ac_speed_statement} \n' \
           f'{back_feat} \n' \
           f'{stat_assign} \n' \
           f'{spell_statement} \n' \
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
    "fullcharacter" is in development, but generates a complete random character sheet.
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
            print(f'{user} generated a complete character')
        if ' help' in message.content.lower():
            await message.channel.send(help_message())
            print(f'{user} asked for help')

client.run(TOKEN)
