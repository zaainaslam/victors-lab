
import pygame, sys, math, random, time, ast
from pygame.locals import *

pygame.init()
pygame.mixer.init()

FPS = 30
fpsClock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 680
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
LAYERSURF = DISPLAYSURF.convert_alpha()
pygame.display.set_caption('THING')

LEFT_BORDER = 10
RIGHT_BORDER = 10
UP_BORDER = 10
DOWN_BORDER = 10
DONUTS = 4
DONUT_PICKED = False
VICTOR_FED = False
HINT_TIMER = 0
HINT = ""
HINT_NUMBER = 0
HINT_DURATION = 100
REFLUX = False
REFLUX_TIMER = 0
REFLUX_DURATION = 100
REFLUXED = False
SHAKE_AMOUNT = 50
WAITED = False


WASTE = 0
WASTE_STEP = 10
GAME_OVER = False

SOUND_POUR = False
SOUND_POUR_T = 0

SUBMITTED_CORRECT = False

FREEZEXY = (0, 0)

SHOP = False

SHOP_SHELF_OPEN = [True, False, False, False, False]

SHAKE_TIMER = 60
SHAKE_ORIGINAL = 60
MOVEMENT = 0

SHAKEN = False
WAIT_TIMER = 90
WAIT_ORIGINAL = 90

#SAVE

savefile = open('save.txt', 'r+')
SAVE_DATA = savefile.readlines()
savefile.close()

def truth(string):
    if string == '0\n':
        return False
    elif string == '1\n' or string == '1':
        return True

def beauty(boolean):
    if boolean == True:
        return '1\n'
    if boolean == False:
        return '0\n'

def savegame():
    
    file = open('save.txt', 'r+')

    #1 - 5
    
    file.write(str(MONEY) + "\n")
    file.write(str(BEAKER_UNLOCKED[0]) + "\n")
    file.write(str(BEAKER_UNLOCKED[1]) + "\n")
    file.write(str(BEAKER_UNLOCKED[2]) + "\n")
    file.write(str(BEAKER_UNLOCKED[3]) + "\n")
    file.write(str(BEAKER_UNLOCKED[4]) + "\n")

    #6 - 7
    
    file.write(str(PLAYER_NAME) + "\n")
    file.write(str(HIGH_SCORE) + "\n")

    
    file.write("1" + "\n")
    
    
    file.write("0")

    file.close()

def erasegame():
    
    file = open('save.txt', 'r+')

    #WRITE YOUR MONEY
    
    file.write("0\n")

    #WRITE YOUR UNLOCKED BEAKERS
    
    file.write("[1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]" + "\n")
    file.write("[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]" + "\n")
    file.write("[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" + "\n")
    file.write("[1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]" + "\n")
    file.write("[1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]" + "\n")
    
    #7 - 8
    
    file.write("NEW PLAYER\n")
    file.write("0\n")

    file.write("1" + "\n")
    
    file.write("0")

    file.close()




#FONTS

LfontObj = pygame.font.Font('freesansbold.ttf', 32)
MfontObj = pygame.font.Font('freesansbold.ttf', 18)
SfontObj = pygame.font.Font('freesansbold.ttf', 12)

#SOUNDS

pourchemical = pygame.mixer.Sound('pourchemical.wav')
tempbeep = pygame.mixer.Sound('tempbeep.wav')
correctanswer = pygame.mixer.Sound('correctanswer.wav')
answerwrong = pygame.mixer.Sound('answerwrong.wav')
buttonpress = pygame.mixer.Sound('buttonpress.wav')
holdbeaker = pygame.mixer.Sound('holdbeaker.wav')
opencurtain = pygame.mixer.Sound('opencurtain.wav')
placebeaker = pygame.mixer.Sound('placebeaker.wav')
breakbeaker = pygame.mixer.Sound('breakbeaker.wav')
success = pygame.mixer.Sound('success.wav')
reaction = pygame.mixer.Sound('reaction.wav')


#COLORS

RAMBO_GREEN   = ( 75,  83,  32)
GREEN         = (  0, 225,  50)
MINT_GREEN    = (100, 225,  50)
GREEN         = ( 44, 135,   0)
BLUE          = ( 21,  50,  80)
WHITE         = (255, 255, 255)
YELLOW        = (255, 255,   0)
RED           = (255,   0,   0)
BLACK         = (  0,   0,   0)
STEEL_BLUE    = (174, 198, 219)
BROWN         = (180, 141,  12)
GREY          = (128, 128, 128)

LAYER = pygame.Color(255, 0, 0, 0)

##OBJECTS

draw_start_button = DISPLAYSURF.blit(pygame.image.load('startbutton.png'), (150, 300))

##ENVIRONMENTS

HIGH_SCORE = int(SAVE_DATA[7])


##POSITIONS

PLAYER_X = 250
PLAYER_Y = 450
PLAYER_DIRECTION = 'UP'
PLAYER_MOVERATE = 3
PLAYER_WALKTIMER = 0
IS_PLAYER_WALKING = False
PLAYER_STEP = 'RIGHT'
LOCATION = 'CLASS'

LETTER_X = 300
LETTER_Y = 200
PLAYER_NAME = (SAVE_DATA[6])[:-1]
TYPING_NAME = False

MONEY = int(SAVE_DATA[0])
SCORE = 0
ANSWERS_RIGHT = 0
ANSWERS_WRONG = 0
QUESTION_ANSWERED = False

WAS_POURED = False
POUR_CHECKED = False

MICE = False

CHECK_BEAKER = False

CHEMICAL_CORRECT = False

SHOP_SHELF_FOCUSED = [False, False, False, False, False]

##LEVELS

LEVELS = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
LEVEL = 0
LEVEL_UP_SCREEN = False

##SCREENS

START_SCREEN = True
LEVEL_SELECT = False
PLAYING_GAME = False

STORY = True

SHELF_FOCUSED = [False, False, False, False, False]
SHELF_OPEN = [False, False, False, False, False]
SHELF_LAYOUT = [['transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',
                 'transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',
                 'transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',],
                ##ACIDS AND ALKALIS AND SALTS AND STUFF
                ['transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',
                 'transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',
                 'transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',],

                ['brownsolid', 'yellowishwhitesolid', 'greysolid', 'transparent', 'transparent', 'transparent',
                 'greysolid', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',
                 'transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',],

                ['transparent', 'transparent', 'transparent', 'purple', 'transparent', 'transparent',
                 'transparent', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',
                 'yellowishwhitesolid', 'transparent', 'transparent', 'transparent', 'transparent', 'transparent',],

                ['transparentgas', 'brown', 'transparent', 'orange', 'transparent', 'transparent',
                 'transparent', 'blue', 'transparent', 'transparent', 'transparent', 'transparent',
                 'violet', 'palepink', 'palebluegreen', 'yellow', 'green', 'blue',]]


BEAKER_NAMES = [['benzene', 'chloromethane', 'ethanoyl chloride', 'ethene', 0, 0,
                 'phenol', 'naphthalene', 'nitrobenzene', 'phenylamine', 0, 0,
                 'methylamine', 'butylamine', 0, 0, 0, 0,],
                ##ACIDS
                ['conc. sulfuric acid', 'conc. nitric acid', 'conc. hydrochloric acid', 'fuming sulfuric acid', 'conc. hydrobromic acid', 0,
                 'dil. sulfuric acid' , 'dil. nitric acid', 'dil. hydrochloric acid', 'ethanoic acid', 0, 0,
                 0, 0 , 0, 0 , 0, 0,],
                #CATALYSTS
                ['iron(III) bromide', 'aluminium chloride', 'tin', 'copper nitrile', 'copper chloride', 'copper bromide',
                 'raney nickel', 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,],
                #SALTS AND BASES
                ['potassium iodide', 'silver nitrate', 'sodium hydroxide', 'potassium permanganate', 0, 0,
                 'sodium nitrate', 'sodium nitrite', 'phosphorous(V) chloride', 'sodium nitrile', 'benzenediazonium chloride', 0,
                 "ammonium vanadate(V)", 0, 0, 0, 0, 0,],
                #MISCELLANEOUS
                ['hydrogen', 'bromine water', '2,4-dinitrophenylhydrazine', 'potassium dichromate', 'ammonia', 0,
                 'ethanol', "dioxovanadium(V)", 0, 0, 0, 0,
                 'chromium (III)', 'manganese (II)', 'iron (II)', 'iron (III)', 'nickel (II)', 'copper (II)',]]

BEAKER_IMAGES = [[1, 1, 1, 0, 0, 0,
                 1, 1, 1, 1, 0, 0,
                 1, 0, 0, 0, 0, 0,],
                ##ACIDS
                [1, 1, 1, 0, 1, 0,
                 1 , 1, 1, 1, 0, 0,
                 0, 0 , 0, 0 , 0, 0,],
                #CATALYSTS
                [0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,],
                #SALTS AND BASES
                [1, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,],
                #MISCELLANEOUS
                [0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,]]

BEAKER_UNLOCKED = [ast.literal_eval(SAVE_DATA[1]),
                ##ACIDS
                ast.literal_eval(SAVE_DATA[2]),
                #CATALYSTS
                ast.literal_eval(SAVE_DATA[3]),
                #SALTS AND BASES
                ast.literal_eval(SAVE_DATA[4]),
                #MISCELLANEOUS
                ast.literal_eval(SAVE_DATA[5])]

BEAKER_PRICE = [[1, 1, 1, 10, 0, 0,
                 1, 1, 20, 20, 20, 10,
                 1, 1, 1, 2, 2, 20,],
                ##ACIDS
                [1, 1, 1, 1, 1, 0,
                 1 , 1, 1, 1, 0, 0,
                 0, 0 , 0, 0 , 0, 0,],
                #CATALYSTS
                [1, 1, 1, 1, 1, 1,
                 1, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,],
                #SALTS AND BASES
                [1, 1, 1, 1, 0, 0,
                 1, 1, 1, 1, 200, 0,
                 0, 0, 0, 0, 0, 0,],
                #MISCELLANEOUS
                [1, 1, 1, 1, 1, 0,
                 1, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0,]]

PRODUCT_COLORS = {"bromobenzene" : "brown",
                  "nasty stuff" : "transparent",
                  "benzenesulfonic acid" : "transparent",
                  "nitrobenzene" : "transparent",
                  "methylbenzene": "transparent",
                  "phenylethanone": "transparent",
                  "2,4,6-tribromophenol": "transparent",
                  "2,4,6-trinitrophenol": "transparent",
                  "methylamine": "transparent",
                  "phenylamine": "transparent",
                  "ammonium chloride": "transparent",
                  "N-methyl ethanamide": "transparent",
                  "dimethylamine": "transparent",
                  "trimethylamine": "transparent",
                  "ethyl ethanoate": "transparent",
                  "cyclohexane": "transparent",
                  "4-nitrophenol": "transparent",
                  "nitrous acid": "transparent",
                  "benzenediazonium chloride": "transparent",
                  "ethanoyl chloride": "transparent",
                  "N-butyl ethanamide": "transparent",
                  "iodobenzene": "transparent",
                  "(4-hydroxyphenyl)azobenzene": "transparent",
                  "bromobenzene": "transparent",
                  "chlorobenzene": "transparent",
                  "benzonitrile": "transparent",
                  "1,2-dibromoethane" : "brown",
                  "dioxovanadium(V)" : "yellow",
                  "oxovanadium(V)" : "blue",
                  "vanadium(III)" : "green",
                  "vanadium(II)" : "purple",
                  "chromium (III) hydroxide" : "bluevioletppt",
                  "manganese (II) hydroxide" : "gelwhiteppt",
                  "iron (II) hydroxide" : "gelpalegreenppt",
                  "iron (III) hydroxide" : "redbrownppt",
                  "nickel (II) hydroxide" : "emeraldgreenppt",
                  "copper (II) hydroxide" : "gelblueppt",

                  #SHELF 1
                  "benzene" : "transparent",
                  "chloromethane" : "transparent",
                  "ethanoyl chloride" : "transparent",
                  "ethene" : "transparent",
                  "phenol" : "transparent",
                  "naphthalene" : "transparent",
                  "nitrobenzene" : "transparent",
                  "phenylamine" : "transparent",
                  "methylamine" : "transparent",
                  "butylamine" : "transparent",

                  #SHELF 2: ACIDS
                  "conc. sulfuric acid" : "transparent",
                  "conc. nitric acid" : "transparent",
                  "conc. hydrochloric acid" : "transparent",
                  "fuming sulfuric acid" : "transparent",
                  "conc. hydrobromic acid" : "transparent",
                  "dil. sulfuric acid" : "transparent",
                  "dil. nitric acid" : "transparent",
                  "dil. hydrochloric acid" : "transparent",
                  "ethanoic acid" : "transparent",

                  #SHELF 3: CATALYSTS
                  "iron(III) bromide" : "brownsolid",
                  "aluminium chloride" : "yellowishwhitesolid",
                  "tin" : "greysolid",
                  "copper nitrile" : "transparent",
                  "copper chloride" : "transparent",
                  "copper bromide" : "transparent",
                  "raney nickel" : "greysolid",


                  #SHELF 4: SALTS AND BASES
                  "potassium iodide" : "transparent",
                  "silver nitrate" : "transparent",
                  "sodium hydroxide" : "transparent",
                  "potassium permanganate" : "purple",
                  "sodium nitrate" : "transparent",
                  "sodium nitrite" : "transparent",
                  "phosphorous(V) chloride" : "transparent",
                  "sodium nitrile" : "transparent",
                  "benzenediazonium chloride" : "transparent",
                  "ammonium vanadate(V)" : "yellowishwhitesolid",

                  #MISCELLANEOUS

                  "hydrogen" : "transparentgas",
                  "bromine water" : "brown",
                  "2,4-dinitrophenylhydrazine" : "transparent",
                  "potassium dichromate" : "orange",
                  "ammonia" : "transparent",
                  "ethanol" : "transparent",
                  "chromium (III)" : "violet",
                  "manganese (II)" : "palepink",
                  "iron (II)" : "palebluegreen",
                  "iron (III)" : "yellow",
                  "nickel (II)" : "green",
                  "copper (II)" : "blue",
                  0 : "transparent",
                  
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",

                  }
PRODUCT_DESCRIPTIONS = {"bromobenzene" : "brown",
                  "nasty stuff" : "transparent",
                  "benzenesulfonic acid" : "transparent",
                  "nitrobenzene" : "transparent",
                  "methylbenzene": "transparent",
                  "phenylethanone": "transparent",
                  "2,4,6-tribromophenol": "transparent",
                  "2,4,6-trinitrophenol": "transparent",
                  "methylamine": "transparent",
                  "phenylamine": "transparent",
                  "ammonium chloride": "transparent",
                  "N-methyl ethanamide": "transparent",
                  "dimethylamine": "transparent",
                  "trimethylamine": "transparent",
                  "ethyl ethanoate": "transparent",
                  "cyclohexane": "transparent",
                  "4-nitrophenol": "transparent",
                  "nitrous acid": "transparent",
                  "benzenediazonium chloride": "transparent",
                  "ethanoyl chloride": "transparent",
                  "N-butyl ethanamide": "transparent",
                  "iodobenzene": "transparent",
                  "(4-hydroxyphenyl)azobenzene": "transparent",
                  "bromobenzene": "transparent",
                  "chlorobenzene": "transparent",
                  "benzonitrile": "transparent",
                  "1,2-dibromoethane" : "brown",
                  "dioxovanadium(V)" : "yellow",
                  "oxovanadium(V)" : "blue",
                  "vanadium(III)" : "green",
                  "vanadium(II)" : "purple",
                  "chromium (III) hydroxide" : "blue-violet precipitate",
                  "manganese (II) hydroxide" : "gelatinous white precipitate",
                  "iron (II) hydroxide" : "gelatinous pale green precipitate",
                  "iron (III) hydroxide" : "reddish-brown precipitate",
                  "nickel (II) hydroxide" : "emerald green precipitate",
                  "copper (II) hydroxide" : "gelatinous blue precipitate",

                  #SHELF 1
                  "benzene" : "transparent",
                  "chloromethane" : "transparent",
                  "ethanoyl chloride" : "transparent",
                  "ethene" : "transparent",
                  "phenol" : "transparent",
                  "naphthalene" : "transparent",
                  "nitrobenzene" : "transparent",
                  "phenylamine" : "transparent",
                  "methylamine" : "transparent",
                  "butylamine" : "transparent",

                  #SHELF 2: ACIDS
                  "conc. sulfuric acid" : "transparent",
                  "conc. nitric acid" : "transparent",
                  "conc. hydrochloric acid" : "transparent",
                  "fuming sulfuric acid" : "transparent",
                  "conc. hydrobromic acid" : "transparent",
                  "dil. sulfuric acid" : "transparent",
                  "dil. nitric acid" : "transparent",
                  "dil. hydrochloric acid" : "transparent",
                  "ethanoic acid" : "transparent",

                  #SHELF 3: CATALYSTS
                  "iron(III) bromide" : "brownsolid",
                  "aluminium chloride" : "yellowishwhitesolid",
                  "tin" : "greysolid",
                  "copper nitrile" : "transparent",
                  "copper chloride" : "transparent",
                  "copper bromide" : "transparent",
                  "raney nickel" : "greysolid",


                  #SHELF 4: SALTS AND BASES
                  "potassium iodide" : "transparent",
                  "silver nitrate" : "transparent",
                  "sodium hydroxide" : "transparent",
                  "potassium permanganate" : "purple",
                  "sodium nitrate" : "transparent",
                  "sodium nitrite" : "transparent",
                  "phosphorous(V) chloride" : "transparent",
                  "sodium nitrile" : "transparent",
                  "benzenediazonium chloride" : "transparent",
                  "ammonium vanadate(V)" : "yellowishwhitesolid",

                  #MISCELLANEOUS

                  "hydrogen" : "transparentgas",
                  "bromine water" : "brown",
                  "2,4-dinitrophenylhydrazine" : "transparent",
                  "potassium dichromate" : "orange",
                  "ammonia" : "transparent",
                  "ethanol" : "transparent",
                  "chromium (III)" : "violet solution",
                  "manganese (II)" : "very pale pink solution",
                  "iron (II)" : "pale blue-green solution",
                  "iron (III)" : "yellow solution",
                  "nickel (II)" : "emerald green solution",
                  "copper (II)" : "blue solution",
                  0 : "transparent",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",

                  }



PRODUCT_IMAGES = ["bromobenzene",
                  "nasty stuff",
                  "benzenesulfonic acid",
                  "nitrobenzene",
                  "methylbenzene",
                  "phenylethanone",
                  "2,4,6-tribromophenol",
                  "2,4,6-trinitrophenol",
                  "methylamine",
                  "phenylamine",
                  "ammonium chloride",
                  "N-methyl ethanamide",
                  "dimethylamine",
                  "trimethylamine",
                  "ethyl ethanoate",
                  "cyclohexane",
                  "4-nitrophenol",
                  "nitrous acid",
                  "benzenediazonium chloride",
                  "ethanoyl chloride",
                  "N-butyl ethanamide",
                  "iodobenzene",
                  "(4-hydroxyphenyl)azobenzene",
                  "bromobenzene",
                  "chlorobenzene",
                  "benzonitrile",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",
##                  "",

                  ]



BEAKER_FOCUSED = [[False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,]]

SHOP_BEAKER_FOCUSED = [[False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,]]


BEAKER_REMOVED = [[False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,]]

BEAKER_REMOVED_ORIGINAL = [[False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,]]

COMBINATIONS = [

                #0-4

                [["benzene", "bromine water", "iron(III) bromide"],"bromobenzene", "closed", 0, 100, "no reflux", "no shake", ""],
                [["bromine water", "potassium permanganate", ""],"nasty stuff", "", 0, 100,"no reflux", "no shake", ""],
                [["benzene", "fuming sulfuric acid", ""],"benzenesulfonic acid", "", 0, 100,"no reflux", "no shake", ""],
                [["benzene", "conc. nitric acid", "conc. sulfuric acid"],"nitrobenzene", "", 0, 55,"no reflux", "no shake", ""],
                [["benzene", "chloromethane", "aluminium chloride"],"methylbenzene", "", 0, 100,"reflux", "no shake", ""],

                #5-9
                [["benzene", "ethanoyl chloride", "aluminium chloride"],"phenylethanone", "", 0, 100,"reflux", "no shake", ""],
                [["phenol", "bromine water", ""],"2,4,6-tribromophenol", "", 0, 100,"no reflux", "no shake", ""],
                [["phenol", "dil. nitric acid", ""],"2,4,6-trinitrophenol", "", 0, 100,"no reflux", "no shake", ""],
                [["chloromethane", "ammonia", ""], "methylamine", "", 0, 100,"no reflux", "no shake", ""],
                [["nitrobenzene", "conc. hydrochloric acid", "tin"], "phenylamine", "", 0, 100,"reflux", "no shake", ""],

                #10-14
                [["ammonia", "dil. hydrochloric acid", ""], "ammonium chloride", "", 0, 100,"no reflux", "no shake", ""],
                [["methylamine", "ethanoyl chloride", ""], "N-methyl ethanamide", "", 0, 100,"no reflux", "no shake", ""],
                [["chloromethane", "methylamine", ""], "dimethylamine", "", 0, 100,"no reflux", "no shake", ""],
                [["dimethylamine", "chloromethane", ""], "trimethylamine", "", 0, 100,"no reflux", "no shake", ""],
                [["ethanoic acid", "ethanol", ""], "ethyl ethanoate", "", 0, 100,"no reflux", "no shake", ""],

                #15-19
                [["ethanoyl chloride", "ethanol", ""], "ethyl ethanoate", "", 0, 100,"no reflux", "no shake", ""],
                [["benzene", "hydrogen", "raney nickel"], "cyclohexane", "", 150, 200,"no reflux", "no shake", ""],
                [["phenol", "sodium nitrate", "dil. sulfuric acid"], "4-nitrophenol", "", 0, 100,"no reflux", "no shake", ""],
                [["sodium nitrite", "dil. hydrochloric acid", ""], "nitrous acid", "", 0, 5,"no reflux", "no shake", ""],
                [["phenylamine", "nitrous acid", "dil. hydrochloric acid"], "benzenediazonium chloride", "", 0, 5,"no reflux", "no shake", ""],

                #20-24
                [["ethanoic acid", "phosphorous(V) chloride", ""], "ethanoyl chloride", "", 0, 100,"no reflux", "no shake", ""],
                [["butylamine", "ethanoyl chloride", ""], "N-butyl ethanamide", "", 0, 100,"no reflux", "no shake", ""],
                [["benzenediazonium chloride", "potassium iodide", ""], "iodobenzene", "", 0, 10,"reflux", "no shake", ""],
                [["benzenediazonium chloride", "phenol", ""], "(4-hydroxyphenyl)azobenzene", "", 0, 10,"no reflux", "no shake", ""],
                [["sodium hydroxide", "dil. sulfuric acid", "ammonium vanadate(V)"], "dioxovanadium(V)", "", 0, 100, "no reflux", "no shake", ""],

                #25-29
                [["benzenediazonium chloride", "conc. hydrobromic acid", "copper bromide"], "bromobenzene", "", 0, 10,"reflux", "no shake", ""],
                [["benzenediazonium chloride", "conc. hydrochloric acid", "copper chloride"], "chlorobenzene", "", 0, 10,"reflux", "no shake", ""],
                [["benzenediazonium chloride", "sodium nitrile", "copper nitrile"], "benzonitrile", "", 0, 10,"no reflux", "no shake", ""],
                [["benzene", "bromine water", ""], "1,2,3,4,5,6-hexabromocyclohexane", "open", 0, 100,"no reflux", "no shake", ""],
                [["nitrobenzene", "dil. nitric acid", ""], "1,3-dinitrobenzene", "", 55, 100,"no reflux", "no shake", ""],

                #30-34
                [["ethene", "bromine water", ""], "1,2-dibromoethane", "", 0, 100, "no reflux", "no shake", ""],
                [["dioxovanadium(V)", "", ""], "oxovanadium(V)", "", 0, 100, "no reflux", "shake", ""],
                [["oxovanadium(V)", "", ""], "vanadium(III)", "", 0, 100, "no reflux", "no shake", "wait"],
                [["vanadium(III)", "", ""], "vanadium(II)", "", 0, 100, "no reflux", "no shake", "wait"],
                [["chromium (III)", "sodium hydroxide", ""], "chromium (III) hydroxide", "", 0, 100, "no reflux", "no shake", ""],
                [["manganese (II)", "sodium hydroxide", ""], "manganese (II) hydroxide", "", 0, 100, "no reflux", "no shake", ""],
                [["iron (II)", "sodium hydroxide", ""], "iron (II) hydroxide", "", 0, 100, "no reflux", "no shake", ""],
                [["iron (III)", "sodium hydroxide", ""], "iron (III) hydroxide", "", 0, 100, "no reflux", "no shake", ""],
                [["nickel (II)", "sodium hydroxide", ""], "nickel (II) hydroxide", "", 0, 100, "no reflux", "no shake", ""],
                [["copper (II)", "sodium hydroxide", ""], "copper (II) hydroxide", "", 0, 100, "no reflux", "no shake", ""],
##                [["", "", ""], "", "", 0, 100, ""]],
##                [["", "", ""], "", "", 0, 100, ""]],
##                [["", "", ""], "", "", 0, 100, ""]],
##                [["", "", ""], "", "", 0, 100, ""]],
##                [["", "", ""], ""],
##                [["", "", ""], ""],
##                [["", "", ""], ""],
##                [["", "", ""], ""],
##                [["", "", ""], ""],
                
                ]


##                [["", "", ""], ""]

BEAKER = [500, 400, False]
MOUSE_BEAKER = False

REQUEST = ["", "", 0]



NEW_QUESTIONS = [["DAD DAD", "I require one beaker of bromobenzene for my daughter's birthday.","bromobenzene", 10, ["Some things should stay in the dark..","Iron(III) bromide will make everything alright..."]],
                 ["Angry Students", "Nasty stuff needed for prank on nasty teacher","nasty stuff", 5, ["The dev made it herself, mix purple and brown", "This doesn't actually exist"]],
                 ["DAD DAD", "THIS CHEMICAL TOTEZ HARDCOREZ PLZ SEND", "benzenesulfonic acid", 10, ["Sometimes I get fuming mad...", "GO CHOKE ON SULFUR AND BENZENE"]],
                  ["DAD DAD", "For unspecified purposes","nitrobenzene", 10, ["Concentrate, concentrate, concentrate...", "Two acids"]],
                  ["DAD DAD", "Is it like meth?","methylbenzene", 10, ["Pick up the pieces...", "Oh, the chlorine ran away..."]],
                  ["DAD DAD", "For christmas gifts","phenylethanone", 10, ["Like methylbenzene but different", "Acyl chloride..."]],
                  ["DAD DAD", "To poison unlikable relatives","2,4,6-tribromophenol", 10, ["Brown water... tee hee hee...", "Dark stuff"]],
                  ["Victor Senpai Fan Club", "SQUEEEE VICTOR SAN NOTICE ME","2,4,6-trinitrophenol", 10, ["My feelings are dilute...", "Night..."]],
                  ["DAD DAD", "Is it like meth?","methylamine", 10, ["A + C", "NOOOO NOT THE CHLORINE"]],
                  ["DAD DAD", "I wanna get high" , "phenylamine", 10, ["Feelsy anime?", "Phenyl is a fancy name for benzene, pfft"]],
                  ["DAD DAD", "For secret coca cola recipe" ,"ammonium chloride", 5, ["White powder and fumes...", "Like 1+ 1"]],
                  ["DAD DAD", "For the lulz" , "N-methyl ethanamide", 10, ["The methyl and the ethyl...", "Not the chlorine"]],
                  ["G0THGURL78", "It has 'die' in it #SuchGoth #VeryEmo" , "dimethylamine", 20, ["A + 2C", "Do it"]],
                  ["DAD DAD", "I want to kill the president" , "trimethylamine", 30, ["A + 3C", "egg"]],
                  ["DAD DAD", "It sounds nice to drink" , "ethyl ethanoate", 10, ["Piece together the pieces...", "There's an alcohol and an acyl chloride..."]],
                  ["DAD DAD", "I like hexagons" , "cyclohexane", 10, ["Raney nickel... I think... maybe...?", "I LIKE IT HOT"]],
                  ["DAD DAD", "For the manufacture of highly dangerous explosives", "4-nitrophenol", 10, ["Night rate!", "Concentrated sulfuric acid was involved"]],
                  ["DAD DAD", "I WANNA GET HIGH" , "nitrous acid", 10, ["Her soul was icy cold, like, 5 degrees or something...", "Night right!"]],
                  ["DAD DAD", "I just hate you" , "benzenediazonium chloride", 30, ["One which loves the cold, one which was reduced, one that's dilute...", "Do it at ten degrees"]],
                  ["DAD DAD", "I heard it makes you fairer", "ethanoyl chloride", 10, ["It's like a puzzle", "Five tentacles"]],
                  ["DAD DAD", "N is my favourite letter","N-butyl ethanamide", 10, ["A + C", "Moose"]],
                  ["DAD DAD", "I wanna make your life hell","iodobenzene", 40, ["KILL", "You need benzenediazonium chloride maybe"]],
                  ["DAD DAD", "For dyeing mankinis","(4-hydroxyphenyl)azobenzene", 40, ["Chlorine eloped with hydrogen", "This is a coupling reaction"]],
                  ["DAD DAD", "For the manufacture of methamphetamine","1,2,3,4,5,6-hexabromocyclohexane", 40, ["LET THERE BE LIGHT", "Just add bromine"]],
                  ["DAD DAD", "It's kinda cool","chlorobenzene", 40, ["I wanna do acid. Which acid?", "Catalyst needed"]],
                  ["DAD DAD", "Just wanna waste my parents' money","benzonitrile", 40, ["Cyanide...", "You'll figure it out"]],
                  ["DAD DAD", "Here's a baby one","1,2-dibromoethane", 10, ["Cyanide...", "You'll figure it out"]],

                 ["DAD DAD", "Here's a baby one","dioxovanadium(V)", 10, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","oxovanadium(V)", 20, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","vanadium(III)", 30, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","vanadium(II)", 40, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","chromium (III) hydroxide", 10, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","manganese (II) hydroxide", 10, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","iron (II) hydroxide", 10, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","iron (III) hydroxide", 10, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","nickel (II) hydroxide", 10, ["Cyanide...", "You'll figure it out"]],
                 ["DAD DAD", "Here's a baby one","copper (II) hydroxide", 10, ["Cyanide...", "You'll figure it out"]],
##                 ["DAD DAD", "Here's a baby one","1,2-dibromoethane", 10, ["Cyanide...", "You'll figure it out"]],

                ]

BEAKER_PICKED = [0, "", 0, 0]
IS_BEAKER_PICKED = False
BEAKER_COLOR = 0
LEVEL_PASSED = False

MOUSEXY = (0, 0)


#               0       1       2       3           4   5 6
#           PICKED, COLOR,  NAME, MOUSED,   BEING HELD, i,j

CHEMICAL = [[False,     "",     "", False,  False, 10000, 10000, False, 0,0, False],
            [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False],
            [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]]

REAGENTS_ADDED = ["", "", ""]
CATALYSTS_ADDED = ["", ""]
TEMPERATURE = 25
PRESSURE = 1
WINDOW_OPEN = False
UV_LIGHT = False
PRODUCT = ""
ANSWER = ""

##GAMEPLAY FUNCTIONS

def check_mouseon(point, object_to_check):
    if object_to_check.collidepoint(point):
        return True


            
    

##DRAWING FUNCTIONS: START + OTHER SCREENS

    

def draw_startscreen():
    if START_SCREEN == True:
        DISPLAYSURF.fill(BLACK)
        

        textSurfaceObj = LfontObj.render('WELCOME ' + PLAYER_NAME, True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2) - 40)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)


        if TYPING_NAME == False:
            textSurfaceObj = MfontObj.render('Not your name? Click here to change', True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2) - 20)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        elif TYPING_NAME == True:
            textSurfaceObj = MfontObj.render('Type your name', True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2) - 20)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = MfontObj.render(str(TYPING_NAME), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (SCREEN_WIDTH/2 + 50, (SCREEN_HEIGHT/2) - 100)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        DISPLAYSURF.blit(pygame.image.load('startbutton.png'), (150, 300))

def draw_shop():
    if SHOP == True:
        DISPLAYSURF.fill(GREEN)

        TILEX = 50
        TILEY = 550
        
        for num in SHOP_SHELF_FOCUSED:
            
            if num == False:
                DISPLAYSURF.blit(pygame.image.load('shelfthumb.png'), (TILEX, TILEY))
            elif num == True:
                DISPLAYSURF.blit(pygame.image.load('shelfthumblarge.png'), (TILEX, TILEY))
                

            TILEX = TILEX + 150

        for num in SHOP_SHELF_OPEN:
            if num == True:
                DISPLAYSURF.blit(pygame.image.load('shelfzoom.png'), (70, 50))
                DISPLAYSURF.blit(pygame.image.load('backbutton.png'), (600, 480))
        i = 0
        j = 0
        
        
        for num in SHOP_SHELF_OPEN:

            
            if num == True:

                TILEX = 100
                TILEY = 115
                BEAKERS = 0

                for beaker in SHELF_LAYOUT[i]:

                    if BEAKER_REMOVED[i][j] == False and (not (CHEMICAL[0][5] == i and CHEMICAL[0][6] == j)) and (not (CHEMICAL[1][5] == i and CHEMICAL[1][6] == j))and (not (CHEMICAL[2][5] == i and CHEMICAL[2][6] == j)):
                        if BEAKER_UNLOCKED[i][j] == 0:
                        
                            DISPLAYSURF.blit(pygame.image.load('beaker'+ PRODUCT_COLORS[BEAKER_NAMES[i][j]]+ '.png'), (TILEX, TILEY))


                    TILEX = TILEX + 70
                    BEAKERS = BEAKERS + 1
                    if BEAKERS == 6:
                        TILEX = 100
                        TILEY = 263
                    if BEAKERS == 12:
                        TILEX = 100
                        TILEY = 415
                    j = j + 1

            i = 1 + i
            j = 0

        i = 0
        j = 0
        
        for num in SHOP_BEAKER_FOCUSED:
            for beaker in num:
                if beaker == True:
                    if BEAKER_UNLOCKED[i][j] == 0:
                        textSurfaceObj = MfontObj.render(str(BEAKER_NAMES[i][j]), True, YELLOW)
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = (780, 100)
                        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

                        textSurfaceObj = MfontObj.render(str(BEAKER_PRICE[i][j]), True, YELLOW)
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = (780, 400)
                        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

                        if not BEAKER_IMAGES[i][j] == 0:
                            
                            DISPLAYSURF.blit(pygame.image.load(str(BEAKER_NAMES[i][j]) + '.png'), (700, 200))

                j = j + 1

            i = i + 1
            j = 0

        textSurfaceObj = MfontObj.render("MONEY: $" + str(MONEY), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 50)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

def draw_levelselect():
    if LEVEL_SELECT == True:
        DISPLAYSURF.fill(BLUE)

        textSurfaceObj = LfontObj.render("SELECT LEVEL " + str(LEVEL), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 80)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        TILEX = 40
        TILEY = 150
        TILEWIDTH = 25
        TILEHEIGHT = 25
        TILENUMBER = 1

        for TILE in LEVELS:
            
            if TILE == 0:
                pygame.draw.circle(DISPLAYSURF, RED, (TILEX, TILEY), TILEWIDTH)
            elif TILE == 1:
                pygame.draw.circle(DISPLAYSURF, GREEN, (TILEX, TILEY), TILEWIDTH)

            textSurfaceObj = MfontObj.render(str(TILENUMBER), True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (TILEX, TILEY)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                

            TILEX = TILEX + TILEWIDTH*2 + 2
            if (TILEX+TILEWIDTH) >= SCREEN_WIDTH:
                TILEX = 40
                TILEY += TILEHEIGHT*2 + 2

            TILENUMBER = TILENUMBER + 1

        textSurfaceObj = LfontObj.render("MONEY: $" + str(MONEY), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 400)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        DISPLAYSURF.blit(pygame.image.load('beakerpurple.png'), (900, 500))
        DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (830, 500))

        textSurfaceObj = LfontObj.render("HIGH SCORE: $" + str(HIGH_SCORE), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (200, 430)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

##        textSurfaceObj = SfontObj.render(str(BEAKER_UNLOCKED[1]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (200, 450)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        DISPLAYSURF.blit(pygame.image.load('shopbutton.png'), (300, 500))

        DISPLAYSURF.blit(pygame.image.load('freemodebutton.png'), (40, 500))

##DRAWING FUNCTIONS:GAMEPLAY

def draw_gamescreen():
    if PLAYING_GAME == True:
        DISPLAYSURF.fill(BLACK)
        
        if WINDOW_OPEN == False:
            DISPLAYSURF.blit(pygame.image.load('windowclosed.png'), (50, 100))
        elif WINDOW_OPEN == True:
            DISPLAYSURF.blit(pygame.image.load('windowopen.png'), (50, 100))

        DISPLAYSURF.blit(pygame.image.load('tempcontrol.png'), (55, 310))

        textSurfaceObj = SfontObj.render(str(TEMPERATURE) + '*C', True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (88, 327)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        if not (True in SHELF_OPEN):

            DISPLAYSURF.blit(pygame.image.load('victor.png'), (800, 250))

##        pygame.draw.rect(DISPLAYSURF, BLUE, (60, 348, 15, 10))
##
##        pygame.draw.rect(DISPLAYSURF, BLUE, (60, 360, 15, 10))

def draw_story():
    
    DISPLAYSURF.fill(RED)
    
    textSurfaceObj = MfontObj.render("This is Victor the Mad Scientist.", True, YELLOW)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (SCREEN_WIDTH/2, 100)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = MfontObj.render("Victor the Mad Scientist is a bad scientist.", True, YELLOW)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (SCREEN_WIDTH/2, 300)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = MfontObj.render("He failed medical school. And high school, and primary school. Basically all the schools.", True, YELLOW)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (SCREEN_WIDTH/2, 350)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = MfontObj.render("But some idiot hired him.", True, YELLOW)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (SCREEN_WIDTH/2, 400)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = MfontObj.render("It's your job to make sure he makes the right chemicals so people don't die.", True, YELLOW)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (SCREEN_WIDTH/2, 450)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    DISPLAYSURF.blit(pygame.image.load('goddamnitvictor.png'), (SCREEN_WIDTH/2 - 300, 500))


def draw_shelves():
    if PLAYING_GAME == True:

        if SHELF_OPEN == [False, False, False, False, False]:
            DISPLAYSURF.blit(pygame.image.load('bench.png'), (30, 400))
##            DISPLAYSURF.blit(pygame.image.load('discardbutton.png'), (800, 50))
            DISPLAYSURF.blit(pygame.image.load('submitbutton.png'), (800, 50))
            DISPLAYSURF.blit(pygame.image.load('quitbutton.png'), (800, 600))
            DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (800, 120))
            DISPLAYSURF.blit(pygame.image.load('ledge.png'), (790, 181))

            textSurfaceObj = SfontObj.render("BEAKERS", True, BROWN)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (835, 193)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = SfontObj.render("<REFLUX", True, BROWN)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (930, 193)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = SfontObj.render("DISCARD HERE", True, BROWN)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (90, 415)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

##            pygame.draw.rect(DISPLAYSURF, WHITE, (885, 185, 15, 15))
            

        TILEX = 50
        TILEY = 550
        
        for num in SHELF_FOCUSED:
            
            if num == False:
                DISPLAYSURF.blit(pygame.image.load('shelfthumb.png'), (TILEX, TILEY))
            elif num == True:
                DISPLAYSURF.blit(pygame.image.load('shelfthumblarge.png'), (TILEX, TILEY))
                

            TILEX = TILEX + 150
 


        textSurfaceObj = SfontObj.render("ORGANIC", True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 580)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render("COMPOUNDS", True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 620)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render("ACIDS", True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 580)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

##        textSurfaceObj = SfontObj.render("COMPOUNDS", True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (100, 620)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render("CATALYSTS", True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (400, 580)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render("SALTS", True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (550, 580)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render("AND BASES", True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (550, 620)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render("MISC.", True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (700, 580)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

##        textSurfaceObj = SfontObj.render("ORGANIC", True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (100, 580)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = SfontObj.render("COMPOUNDS", True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (100, 620)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        for num in SHELF_OPEN:
            if num == True:
                DISPLAYSURF.blit(pygame.image.load('shelfzoom.png'), (70, 50))
                DISPLAYSURF.blit(pygame.image.load('backbutton.png'), (600, 480))

        if not (True in SHELF_OPEN):
            if ANSWER in PRODUCT_IMAGES:
                DISPLAYSURF.blit(pygame.image.load(str(ANSWER) + '.png'), (570, 50))

            textSurfaceObj = SfontObj.render(str(ANSWER), True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (670, 270)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = SfontObj.render("REQUESTED BY: ", True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (670, 290)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = SfontObj.render("'" + str(REQUEST[0]) + "'", True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (670, 310)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            textSurfaceObj = SfontObj.render("'" + str(REQUEST[1]) + "'", True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (670, 330)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        #DEBUG HELP

        
        textSurfaceObj = SfontObj.render(str(CHEMICAL[0]), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 50)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render(str(CHEMICAL[1]), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 60)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render(str(CHEMICAL[2]), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 70)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = SfontObj.render(str(WAITED), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 80)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##

##
##        textSurfaceObj = SfontObj.render(str(SCORE), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 100)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##        
##        textSurfaceObj = SfontObj.render(str(LEVELS), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 110)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = SfontObj.render(str(ANSWERS_WRONG), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 120)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = SfontObj.render(str(CHEMICAL), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 130)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def wait():
    global WAIT_TIMER, WAITED
    if PLAYING_GAME == True and WAITED == False:
        if WAIT_TIMER > 0:
            WAIT_TIMER = WAIT_TIMER - 1

        elif WAIT_TIMER == 0:
            WAIT_TIMER = WAIT_ORIGINAL
            WAITED = True
                    
def draw_shelf_chemicals():
    if PLAYING_GAME == True:
        i = 0
        j = 0
        
        
        for num in SHELF_OPEN:

            
            if num == True:

                TILEX = 100
                TILEY = 115
                BEAKERS = 0

                for beaker in SHELF_LAYOUT[i]:

                    if BEAKER_REMOVED[i][j] == False and (not (CHEMICAL[0][5] == i and CHEMICAL[0][6] == j)) and (not (CHEMICAL[1][5] == i and CHEMICAL[1][6] == j))and (not (CHEMICAL[2][5] == i and CHEMICAL[2][6] == j)):
                        if BEAKER_UNLOCKED[i][j] == 1:
                        
                            DISPLAYSURF.blit(pygame.image.load('beaker'+PRODUCT_COLORS[BEAKER_NAMES[i][j]]+ '.png'), (TILEX, TILEY))


                    TILEX = TILEX + 70
                    BEAKERS = BEAKERS + 1
                    if BEAKERS == 6:
                        TILEX = 100
                        TILEY = 263
                    if BEAKERS == 12:
                        TILEX = 100
                        TILEY = 415
                    j = j + 1

            i = 1 + i
            j = 0

        i = 0
        j = 0
        
        for num in BEAKER_FOCUSED:
            for beaker in num:
                if beaker == True:
                    if BEAKER_UNLOCKED[i][j] == 1:
                        textSurfaceObj = MfontObj.render(str(BEAKER_NAMES[i][j]), True, YELLOW)
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = (780, 100)
                        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

                        if not BEAKER_IMAGES[i][j] == 0:
                            
                            DISPLAYSURF.blit(pygame.image.load(str(BEAKER_NAMES[i][j]) + '.png'), (700, 200))

                j = j + 1

            i = i + 1
            j = 0

def play_sound():
    global SOUND_POUR, SOUND_POUR_T
    if SOUND_POUR == True:
        SOUND_POUR_T += 1
        pygame.mouse.set_pos([FREEZEXY[0], FREEZEXY[1]])

        if SOUND_POUR_T > 25:
            SOUND_POUR_T = 0
            SOUND_POUR = False

            pourchemical.stop()
            
            
def hold_chemical(TILEX, TILEY):
    global BEAKER_COLOR
    if PLAYING_GAME == True:

        #DRAW BEAKER THAT IS BEING POURED

        if SOUND_POUR == True:
            DISPLAYSURF.blit(pygame.image.load('beakerpourleft.png'), (FREEZEXY[0], FREEZEXY[1]))

        elif SOUND_POUR == False:
            if IS_BEAKER_PICKED == True:
                BEAKER_COLOR = BEAKER_PICKED[0]
                DISPLAYSURF.blit(pygame.image.load('beaker'+ BEAKER_COLOR+ '.png'), (TILEX, TILEY))

            #DRAW BEAKER THAT HAS BEEN PICKED FROM BENCH

            elif CHEMICAL[0][4] == True:
                
                    DISPLAYSURF.blit(pygame.image.load('beaker'+CHEMICAL[0][1]+'.png'), (TILEX, TILEY))


            elif CHEMICAL[1][4] == True:
                
                DISPLAYSURF.blit(pygame.image.load('beaker'+CHEMICAL[1][1]+'.png'), (TILEX, TILEY))

            elif CHEMICAL[2][4] == True:
                
                DISPLAYSURF.blit(pygame.image.load('beaker'+CHEMICAL[2][1]+'.png'), (TILEX, TILEY))

            if BEAKER[2] == True:
                how_empty = 0

                for reagent in REAGENTS_ADDED:
                    if reagent == "":
                        how_empty = how_empty + 1

                if how_empty == 0:
                    DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (TILEX, TILEY))
                elif how_empty == 1:
                    DISPLAYSURF.blit(pygame.image.load('beakertwo.png'), (TILEX, TILEY))
                elif how_empty == 2:
                    DISPLAYSURF.blit(pygame.image.load('beakerone.png'), (TILEX, TILEY))
                elif how_empty == 3:
                    DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (TILEX, TILEY))

        if DONUT_PICKED == True:
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (TILEX + 50, TILEY))
                
        

            

def draw_bench():
    global REFLUX, REFLUX_TIMER, REFLUXED
    if PLAYING_GAME == True and not (True in SHELF_OPEN):

        #DRAW CHEMICALS ON BENCH
        
        if CHEMICAL[0][0] == True and CHEMICAL[0][4] == False:
            
                DISPLAYSURF.blit(pygame.image.load('beaker'+CHEMICAL[0][1]+'.png'), (CHEMICAL[0][8] - 50, 400))
                
        if CHEMICAL[1][0] == True and CHEMICAL[1][4] == False:
            
            DISPLAYSURF.blit(pygame.image.load('beaker'+CHEMICAL[1][1]+'.png'), (CHEMICAL[1][8] - 50, 400))
                
        if CHEMICAL[2][0] == True and CHEMICAL[2][4] == False:
            
            DISPLAYSURF.blit(pygame.image.load('beaker'+CHEMICAL[2][1]+'.png'), (CHEMICAL[2][8] - 50, 400))

        if BEAKER[2] == False:

            if REFLUX == False:

                how_empty = 0

                for reagent in REAGENTS_ADDED:
                    if reagent == "":
                        how_empty = how_empty + 1

                if how_empty == 0:
                    DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (BEAKER[0], BEAKER[1]))
                elif how_empty == 1:
                    DISPLAYSURF.blit(pygame.image.load('beakertwo.png'), (BEAKER[0], BEAKER[1]))
                elif how_empty == 2:
                    DISPLAYSURF.blit(pygame.image.load('beakerone.png'), (BEAKER[0], BEAKER[1]))
                elif how_empty == 3:
                    DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (BEAKER[0], BEAKER[1]))

            elif REFLUX == True:
                if REFLUX_TIMER < REFLUX_DURATION:
                    DISPLAYSURF.blit(pygame.image.load('reflux.png'), (BEAKER[0], BEAKER[1] - 221 + 61))
                    REFLUX_TIMER = REFLUX_TIMER + 1

                elif REFLUX_TIMER == REFLUX_DURATION:
                    REFLUX = False
                    REFLUX_TIMER = 0
                    REFLUXED = True

                    
                     
                
            
            

        #SHOW CHEMICAL NAMES ON MOUSEOVER

        if CHEMICAL[0][3] == True and CHEMICAL[0][4] == False:
            textSurfaceObj = SfontObj.render(str(CHEMICAL[0][2]), True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (450, 270)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)


            textSurfaceObj = SfontObj.render(PRODUCT_DESCRIPTIONS[CHEMICAL[0][2]], True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (450, 280)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            if (not CHEMICAL[0][5] > 100) and (not BEAKER_IMAGES[CHEMICAL[0][5]][CHEMICAL[0][6]] == 0):
                 DISPLAYSURF.blit(pygame.image.load(str(CHEMICAL[0][2]) + '.png'), (350, 50))

            elif CHEMICAL[0][5] > 100 and (CHEMICAL[0][2] in PRODUCT_IMAGES):
                DISPLAYSURF.blit(pygame.image.load(str(CHEMICAL[0][2]) + '.png'), (350, 50))
                

        if CHEMICAL[1][3] == True and CHEMICAL[1][4] == False:
            textSurfaceObj = SfontObj.render(str(CHEMICAL[1][2]), True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (450, 270)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        

            textSurfaceObj = SfontObj.render(PRODUCT_DESCRIPTIONS[CHEMICAL[1][2]], True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (450, 280)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            if (not CHEMICAL[1][5] > 100) and (not BEAKER_IMAGES[CHEMICAL[1][5]][CHEMICAL[1][6]] == 0):
                        DISPLAYSURF.blit(pygame.image.load(str(CHEMICAL[1][2]) + '.png'), (350, 50))

            elif CHEMICAL[1][5] > 100 and (CHEMICAL[1][2] in PRODUCT_IMAGES):
                DISPLAYSURF.blit(pygame.image.load(str(CHEMICAL[1][2]) + '.png'), (350, 50)) 

        if CHEMICAL[2][3] == True and CHEMICAL[2][4] == False:
            textSurfaceObj = SfontObj.render(str(CHEMICAL[2][2]), True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (450, 270)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            


            textSurfaceObj = SfontObj.render(PRODUCT_DESCRIPTIONS[CHEMICAL[2][2]], True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (450, 280)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            if (not CHEMICAL[2][5] > 100) and (not BEAKER_IMAGES[CHEMICAL[2][5]][CHEMICAL[2][6]] == 0):
                        DISPLAYSURF.blit(pygame.image.load(str(CHEMICAL[2][2]) + '.png'), (350, 50))

            elif CHEMICAL[1][5] > 100 and (CHEMICAL[1][2] in PRODUCT_IMAGES):
                DISPLAYSURF.blit(pygame.image.load(str(CHEMICAL[1][2]) + '.png'), (350, 50))

        if MOUSE_BEAKER == True:
            
            textSurfaceObj = MfontObj.render("IN BEAKER:", True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (BEAKER[0] + 30, 480)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            if REAGENTS_ADDED == ["","",""]:
                textSurfaceObj = SfontObj.render("nothing", True, YELLOW)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (BEAKER[0] + 30, 500)
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)

            else:            
            
                textSurfaceObj = SfontObj.render(str(REAGENTS_ADDED[0]), True, YELLOW)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (BEAKER[0] + 30, 500)
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = SfontObj.render(str(REAGENTS_ADDED[1]), True, YELLOW)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (BEAKER[0] + 30, 515)
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)

                textSurfaceObj = SfontObj.render(str(REAGENTS_ADDED[2]), True, YELLOW)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (BEAKER[0] + 30, 530)
                DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                
##        textSurfaceObj = SfontObj.render(str(WASTE), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 60)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

##        textSurfaceObj = SfontObj.render(str(CHEMICAL[1]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 70)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

##        textSurfaceObj = SfontObj.render(str(CHEMICAL[2]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 80)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = SfontObj.render(str(BEAKER), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 90)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = SfontObj.render(str(BEAKER_PICKED), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 100)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
                

#DISPLAY SCORE

def display_score():
    global HINT_TIMER

    if PLAYING_GAME == True:

        textSurfaceObj = MfontObj.render(str(PLAYER_NAME), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 20)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = MfontObj.render("SCORE: $" + str(SCORE), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (100, 40)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        if LEVEL == "FREE":
            textSurfaceObj = MfontObj.render("FREE MODE", True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (100, 60)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        else:
            textSurfaceObj = MfontObj.render("LEVEL: " + str(LEVEL), True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (100, 60)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        pygame.draw.rect(DISPLAYSURF, WHITE, (180, 30, 100, 20))

        HEALTH_COLOR = ""

        if WASTE >= 90:
            HEALTH_COLOR = RED
        elif WASTE >= 50:
            HEALTH_COLOR = YELLOW
        else:
            HEALTH_COLOR = GREEN

        if WASTE > 0:

            pygame.draw.rect(DISPLAYSURF, HEALTH_COLOR, (180, 30, WASTE, 20))

        to_draw = DONUTS

        if (DONUTS == 4 and DONUT_PICKED == False):
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (180, 55))
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (210, 55))
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (240, 55))
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (270, 55))

        elif (DONUTS == 3 and DONUT_PICKED == False) or (DONUTS == 4 and DONUT_PICKED == True):
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (180, 55))
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (210, 55))
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (240, 55))


        elif (DONUTS == 2 and DONUT_PICKED == False) or (DONUTS == 3 and DONUT_PICKED == True):
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (180, 55))
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (210, 55))


        elif (DONUTS == 1 and DONUT_PICKED == False) or (DONUTS == 2 and DONUT_PICKED == True):
            DISPLAYSURF.blit(pygame.image.load('donut.png'), (180, 55))

        if HINT_TIMER > 0:
            textSurfaceObj = MfontObj.render(str(HINT[HINT_NUMBER]), True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (500, 500)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            HINT_TIMER = HINT_TIMER - 1


        

#CARRY OUT REACTION

def react(number):
    global WAITED, PRODUCT, SHAKEN, REFLUXED, REAGENTS_ADDED, ANSWERS_RIGHT, ANSWERS_WRONG, SCORE, QUESTION_ANSWERED, CHECK_BEAKER, CHEMICAL_CORRECT, POUR_CHECKED

    REACTANTS = ["", "", ""]

    if number == 1:
        WAS_POURED = True

    elif number == 0:
        WAS_POURED = False

    
    for num in REAGENTS_ADDED:
        
        if not (num == ""):
            
            if REACTANTS[0] == "":
                REACTANTS[0] = num

            elif REACTANTS[1] == "":
                REACTANTS[1] = num

            elif REACTANTS[2] == "":
                REACTANTS[2] = num

    i = 0

    for combination in COMBINATIONS:
        
        if (COMBINATIONS[i][0][0] in REACTANTS) and (COMBINATIONS[i][0][1] in REACTANTS) and(COMBINATIONS[i][0][2] in REACTANTS):

            if ((COMBINATIONS[i][2] == "") or (COMBINATIONS[i][2] == "closed" and WINDOW_OPEN == False) or (COMBINATIONS[i][2] == "open" and WINDOW_OPEN == True)):

                if TEMPERATURE >= COMBINATIONS[i][3] and TEMPERATURE <= COMBINATIONS [i][4]:

                    if (REFLUXED == False and COMBINATIONS[i][5] == "no reflux") or (REFLUXED == True and COMBINATIONS[i][5] == "reflux"):

                         if ((COMBINATIONS[i][6] == "no shake") or ((COMBINATIONS[i][6] == "shake" and SHAKEN == True))):

                             if ((COMBINATIONS[i][7] == "") or ((COMBINATIONS[i][7] == "wait" and WAITED == True))):

            
                                PRODUCT = COMBINATIONS[i][1]
                            
                                if CHEMICAL[0][2] == "":
                                    if WAS_POURED == True and SHAKEN == False:
                                        BEAKER[2] = True
                                        POUR_CHECKED = True

                                    if COMBINATIONS[i][6] == "no shake":
                                        CHEMICAL[0] = [True, PRODUCT_COLORS[PRODUCT], PRODUCT, False, False, 1000, 1000, True, BEAKER[0] + 50, BEAKER[1], True]
                                    elif COMBINATIONS[i][6] == "shake" and SHAKEN == True:
                                        BEAKER[2] = False
                                        CHEMICAL[2] = [True, PRODUCT_COLORS[PRODUCT], PRODUCT, False, True, 1000, 1000, True, MOUSEXY[0] + 50, MOUSEXY[1], True]
                                    

                                elif CHEMICAL[1][2] == "":
                                    if WAS_POURED == True and SHAKEN == False:
                                        BEAKER[2] = True
                                        POUR_CHECKED = True

                                    if COMBINATIONS[i][6] == "no shake":
                                        CHEMICAL[1] = [True, PRODUCT_COLORS[PRODUCT], PRODUCT, False, False, 1000, 1000, True, BEAKER[0] + 50, BEAKER[1], True]
                                    elif COMBINATIONS[i][6] == "shake" and SHAKEN == True:
                                        BEAKER[2] = False
                                        CHEMICAL[2] = [True, PRODUCT_COLORS[PRODUCT], PRODUCT, False, True, 1000, 1000, True, MOUSEXY[0] + 50, MOUSEXY[1], True]

                                elif CHEMICAL[2][2] == "":
                                    if WAS_POURED == True and SHAKEN == False:
                                        BEAKER[2] = True
                                        POUR_CHECKED = True

                                    if COMBINATIONS[i][6] == "no shake":
                                        CHEMICAL[2] = [True, PRODUCT_COLORS[PRODUCT], PRODUCT, False, False, 1000, 1000, True, BEAKER[0] + 50, BEAKER[1], True]
                                    elif COMBINATIONS[i][6] == "shake" and SHAKEN == True:
                                        BEAKER[2] = False
                                        CHEMICAL[2] = [True, PRODUCT_COLORS[PRODUCT], PRODUCT, False, True, 1000, 1000, True, MOUSEXY[0] + 50, MOUSEXY[1], True]

                                if WAS_POURED == True and SHAKEN == False:
                                    BEAKER[0] = BEAKER[0] - 50

                                else:

                                    BEAKER[0] = -100
                                        
                                REAGENTS_ADDED = ["", "", ""]
                                MICE = True
                                REFLUXED = False
                                SHAKEN = False
                                WAITED = False
                                if PRODUCT == ANSWER:
                                    CHEMICAL_CORRECT = True
                                    success.play()

                                else:
                                        reaction.play()

                    

    

                
                

                

                

##        elif "" not in REACTANTS and QUESTION_ANSWERED == True:
##            ANSWERS_WRONG = ANSWERS_WRONG + 1
##            QUESTION_ANSWERED = False
            
        i = i + 1
    

    

#CHECK IF A BEAKER IS REMOVED

#LEVEL_LAYOUT

def level():
    global ANSWER, SCORE, QUESTION_ANSWERED, REQUEST, LEVEL, LEVEL_PASSED, ANSWERS_RIGHT, HINT

    if LEVEL == "FREE":
        if QUESTION_ANSWERED == False:
            question_number = int(random.randrange(0, (len(NEW_QUESTIONS))))
            ANSWER = NEW_QUESTIONS[question_number][2]
            REQUEST = [NEW_QUESTIONS[question_number][0],NEW_QUESTIONS[question_number][1], NEW_QUESTIONS[question_number][3]]
            HINT = NEW_QUESTIONS[question_number][4]
            QUESTION_ANSWERED = True

        

    elif LEVEL == 1:

##        textSurfaceObj = MfontObj.render(str(NEW_QUESTIONS[0][0][0]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 80)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = MfontObj.render(str(NEW_QUESTIONS[0][0][1]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 110)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        if ANSWERS_RIGHT == 0:
            question_number = 28
            ANSWER = NEW_QUESTIONS[question_number][2]
            REQUEST = [NEW_QUESTIONS[question_number][0],NEW_QUESTIONS[question_number][1], NEW_QUESTIONS[question_number][3]]
            HINT = NEW_QUESTIONS[question_number][4]
            QUESTION_ANSWERED = True

        

        elif ANSWERS_RIGHT == 5:
            question_number = 28
            ANSWER = NEW_QUESTIONS[question_number][2]
            REQUEST = [NEW_QUESTIONS[question_number][0],NEW_QUESTIONS[question_number][1], NEW_QUESTIONS[question_number][3]]
            HINT = NEW_QUESTIONS[question_number][4]
            QUESTION_ANSWERED = True
            LEVEL_PASSED = True
            LEVEL += 1
            ANSWERS_RIGHT = 0

        elif QUESTION_ANSWERED == False:
##            ANSWER = COMBINATIONS[int(random.randrange(0, (len(COMBINATIONS) - 1)))][1]
            question_number = 28
            ANSWER = NEW_QUESTIONS[question_number][2]
            REQUEST = [NEW_QUESTIONS[question_number][0],NEW_QUESTIONS[question_number][1], NEW_QUESTIONS[question_number][3]]
            HINT = NEW_QUESTIONS[question_number][4]
            QUESTION_ANSWERED = True

    elif LEVEL == 2:

##        textSurfaceObj = MfontObj.render(str(NEW_QUESTIONS[0][0][0]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 80)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = MfontObj.render(str(NEW_QUESTIONS[0][0][1]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 110)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        if ANSWERS_RIGHT == 0:
            ANSWER = COMBINATIONS[1][1]
            QUESTION_ANSWERED = True

        

        elif ANSWERS_RIGHT == 2:
            ANSWER = COMBINATIONS[1][1]
            QUESTION_ANSWERED = True
            LEVEL_PASSED = True
            LEVEL += 1
            ANSWERS_RIGHT = 0

        elif QUESTION_ANSWERED == False:
            ANSWER = COMBINATIONS[int(random.randrange(0, (len(COMBINATIONS) - 1)))][1]
            QUESTION_ANSWERED = True

    elif LEVEL == 3:

##        textSurfaceObj = MfontObj.render(str(NEW_QUESTIONS[0][0][0]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 80)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
##
##        textSurfaceObj = MfontObj.render(str(NEW_QUESTIONS[0][0][1]), True, YELLOW)
##        textRectObj = textSurfaceObj.get_rect()
##        textRectObj.center = (500, 110)
##        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        if ANSWERS_RIGHT == 0:
            ANSWER = COMBINATIONS[2][1]
            QUESTION_ANSWERED = True

        

        elif ANSWERS_RIGHT == 2:
            ANSWER = COMBINATIONS[2][1]
            QUESTION_ANSWERED = True
            LEVEL_PASSED = True
            LEVEL += 1
            ANSWERS_RIGHT = 0

        elif QUESTION_ANSWERED == False:
            ANSWER = COMBINATIONS[int(random.randrange(0, (len(COMBINATIONS) - 1)))][1]
            QUESTION_ANSWERED = True

def game_over():
    if GAME_OVER == True:
        DISPLAYSURF.fill(BLACK)
        DISPLAYSURF.blit(pygame.image.load('proceedbutton.png'), (500, 480))

        if WASTE >= 100:

            textSurfaceObj = LfontObj.render('"STOP WASTING CHEMICALS!"', True, YELLOW)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (SCREEN_WIDTH/2, 200)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = MfontObj.render("SCORE: $" + str(SCORE), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (SCREEN_WIDTH/2, 300)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = MfontObj.render("HIGH SCORE: $" + str(HIGH_SCORE), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (SCREEN_WIDTH/2, 340)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = MfontObj.render("MONEY: $" + str(MONEY), True, YELLOW)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (SCREEN_WIDTH/2, 380)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

        


def level_up():
    global LEVEL_PASSED, SCORE, LEVEL_UP_SCREEN

    if  PLAYING_GAME == True:

        if (not LEVEL == "FREE") and LEVEL_PASSED == True:

            SCORE +=1

            levels_reached = 0

 

            for level in LEVELS:

                if level == 1:
                    levels_reached += 1

            i = 0

            if LEVEL > levels_reached:

                levels_reached = LEVEL

                for level in LEVELS:

                    if levels_reached > 0:
                        LEVELS[i] = 1
                        i = i + 1
                        levels_reached -= 1

            LEVEL_UP_SCREEN = True

            LEVEL_PASSED = False

            

        
def check_shaken():
    global SHAKE_TIMER, SHAKEN, MOVEMENT
    if PLAYING_GAME == True and (BEAKER[2] == True):

        if MOVEMENT == 0:
            MOVEMENT = pygame.mouse.get_rel()

        elif SHAKE_TIMER > 0:
            SHAKE_TIMER = SHAKE_TIMER - 1

        elif SHAKE_TIMER == 0:
            MOVEMENT = pygame.mouse.get_rel()
            if SHAKEN == False and MOVEMENT[0] > SHAKE_AMOUNT:
                SHAKEN = True

            SHAKE_TIMER = SHAKE_ORIGINAL

        





        

        


#EVENT HANDLER + GAME LOOP

while True:

    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #START SCREEN EVENTS

        if START_SCREEN == True:  
            if event.type == MOUSEBUTTONUP:
                
                if check_mouseon(pygame.mouse.get_pos(), draw_start_button) == True:
                    LEVEL_SELECT = True
                    START_SCREEN = False
                    buttonpress.play()

                elif check_mouseon(pygame.mouse.get_pos(), pygame.draw.rect(DISPLAYSURF, RED, (SCREEN_WIDTH/2 - 40, (SCREEN_HEIGHT/2) - 40, 400, 40))) == True:
                    TYPING_NAME = True
                    PLAYER_NAME = ""

            
            if event.type == KEYDOWN and TYPING_NAME == True:
                if event.unicode.isalpha():
                    PLAYER_NAME += event.unicode
                elif event.key == K_BACKSPACE:
                    PLAYER_NAME = PLAYER_NAME[:-1]
                elif event.key == K_RETURN:
                    TYPING_NAME = False
            

        #LEVEL SELECT EVENTS
                    
        if LEVEL_SELECT == True:

            if event.type == MOUSEBUTTONUP:
                
                TILEX = 40
                TILEY = 150
                TILEWIDTH = 25
                TILEHEIGHT = 25
                TILENUMBER = 1

                for TILE in LEVELS:
                    
                    if TILE == 0:
                        1    
                    elif TILE == 1:
                        if check_mouseon(pygame.mouse.get_pos(), pygame.draw.circle(DISPLAYSURF, GREEN, (TILEX, TILEY), TILEWIDTH)) == True:
                            LEVEL = TILENUMBER
                            PLAYING_GAME = True
                            LEVEL_SELECT = False
                            buttonpress.play()
                        

                    TILEX = TILEX + TILEWIDTH*2 + 2
                    if (TILEX+TILEWIDTH) >= SCREEN_WIDTH:
                        TILEX = 40
                        TILEY += TILEHEIGHT*2 + 2

                    TILENUMBER = TILENUMBER + 1

                    

        

                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('freemodebutton.png'), (40, 500))) == True:
                    LEVEL = "FREE"
                    PLAYING_GAME = True
                    LEVEL_SELECT = False

                elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('shopbutton.png'), (300, 500))) == True:
                    
                    SHOP = True
                    LEVEL_SELECT = False

                #SAVE GAME

                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (900, 500))) == True:
                    savegame()

                elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (830, 500))) == True:
                    erasegame()

        #SHOP EVENTS
        
        if SHOP == True and LEVEL_SELECT == False:

            #MOUSE OVER SHOP SHELVES AND CHEMICALS

            TILEX = 50
            TILEY = 550
            i = 0
            
            for num in SHOP_SHELF_FOCUSED:
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('shelfthumb.png'), (TILEX, TILEY))) == True:
                    SHOP_SHELF_FOCUSED[i] = True
                else:
                    SHOP_SHELF_FOCUSED[i] = False

                TILEX = TILEX + 150
                i = i + 1

            TILEX = 100
            TILEY = 115
            i = 0
            j = 0
            BEAKERS = 0

            for num in SHOP_SHELF_OPEN:
                if num == True:
                    for num in SHOP_BEAKER_FOCUSED[i]:
                
                        if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (TILEX, TILEY))) == True:
                            SHOP_BEAKER_FOCUSED[i][j] = True
                        else:
                            SHOP_BEAKER_FOCUSED[i][j] = False

                        TILEX = TILEX + 70
                        BEAKERS = BEAKERS + 1
                        if BEAKERS == 6:
                            TILEX = 100
                            TILEY = 263
                        if BEAKERS == 12:
                            TILEX = 100
                            TILEY = 415
                        j = j + 1
    
                i = i + 1
                j = 0
                BEAKERS = 0
                
            if event.type == MOUSEBUTTONUP:

                #OPEN OR CLOSE A SHELF

                TILEX = 50
                TILEY = 550
                i = 0
                
                for num in SHOP_SHELF_FOCUSED:
                    if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('shelfthumb.png'), (TILEX, TILEY))) == True:
                        SHOP_SHELF_OPEN = [False, False, False, False, False]
                        SHOP_SHELF_OPEN[i] = True
                        pygame.mixer.Sound('openshelf.wav').play()
    
                    elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('backbutton.png'), (600, 480))) == True:
                        SHOP = False
                        LEVEL_SELECT = True
                        SHOP_SHELF_OPEN = [True, False, False, False, False]

                    TILEX = TILEX + 150
                    i = i + 1

                #BUY A CHEMICAL

                TILEX = 100
                TILEY = 115
                i = 0
                j = 0
                BEAKERS = 0

                for num in SHOP_SHELF_OPEN:
                    if num == True:
                        for num in SHOP_BEAKER_FOCUSED[i]:
                    
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (TILEX, TILEY))) == True  and BEAKER_UNLOCKED[i][j] == 0:

                                if MONEY >= BEAKER_PRICE[i][j]:
                                    BEAKER_UNLOCKED[i][j] = 1
                                    MONEY = MONEY - BEAKER_PRICE[i][j]
                                    holdbeaker.play()
                            

                                
    ##                        else:
    ##                            BEAKER_FOCUSED[i][j] = False

                            TILEX = TILEX + 70
                            BEAKERS = BEAKERS + 1
                            if BEAKERS == 6:
                                TILEX = 100
                                TILEY = 263
                            if BEAKERS == 12:
                                TILEX = 100
                                TILEY = 415
                            j = j + 1
        
                    i = i + 1
                    j = 0
                    BEAKERS = 0
                    
##                if check_mouseon(pygame.mouse.get_pos(), pygame.draw.circle(DISPLAYSURF, GREEN, (700, 0), 100)) == True:
##                    SHOP = False
##                    LEVEL_SELECT = True

        #GAME OVER EVENTS

        if GAME_OVER == True:
            if event.type == MOUSEBUTTONUP:
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('proceedbutton.png'), (500, 480))) == True:
                    LEVEL_SELECT = True
                    GAME_OVER = False
                    buttonpress.play()
                    
                    
                        
                    SCORE = 0
                    WASTE = 0
                    DONUTS = 4
                    DONUT_PICKED = False
                    VICTOR_FED = False
                    HINT_TIMER = 0
                    HINT = ""
                    HINT_NUMBER = 0
                    
                    ANSWERS_RIGHT = 0
                    ANSWERS_WRONG = 0
                    QUESTION_ANSWERED = False

                    BEAKER_PICKED = [0, "", 0, 0]
                    IS_BEAKER_PICKED = False
                    BEAKER_COLOR = 0
                    LEVEL_PASSED = False

                    CHEMICAL = [[False,     "",     "", False,  False, 10000, 10000, False, 0,0, False],
                                [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False],
                                [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]]

                    REAGENTS_ADDED = ["", "", ""]
                    CATALYSTS_ADDED = ["", ""]
                    TEMPERATURE = 25
                    PRESSURE = 1
                    WINDOW_OPEN = False
                    UV_LIGHT = False
                    PRODUCT = ""
                    ANSWER = ""

            


        #STORY EVENTS

        if STORY == True and LEVEL == 1:
            if event.type == MOUSEBUTTONUP:
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('goddamnitvictor.png'), (SCREEN_WIDTH/2 - 300, 500))) == True:
                    STORY = False
                    buttonpress.play()

        #GAMEPLAY EVENTS

        if PLAYING_GAME == True:

            TILEX = 50
            TILEY = 550
            i = 0
            
            for num in SHELF_FOCUSED:
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('shelfthumb.png'), (TILEX, TILEY))) == True:
                    SHELF_FOCUSED[i] = True
                else:
                    SHELF_FOCUSED[i] = False

                TILEX = TILEX + 150
                i = i + 1

            TILEX = 100
            TILEY = 115
            i = 0
            j = 0
            BEAKERS = 0

            for num in SHELF_OPEN:
                if num == True:
                    for num in BEAKER_FOCUSED[i]:
                
                        if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (TILEX, TILEY))) == True:
                            BEAKER_FOCUSED[i][j] = True
                        else:
                            BEAKER_FOCUSED[i][j] = False

                        TILEX = TILEX + 70
                        BEAKERS = BEAKERS + 1
                        if BEAKERS == 6:
                            TILEX = 100
                            TILEY = 263
                        if BEAKERS == 12:
                            TILEX = 100
                            TILEY = 415
                        j = j + 1
    
                i = i + 1
                j = 0
                BEAKERS = 0

            
            #MOUSE OVER CHEMICAL ON BENCH
            
            i = 0

            for num in CHEMICAL:
                if num[0] == True:
                    if i == 0:
                        if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (CHEMICAL[0][8] -50, 400))) == True:
                            CHEMICAL[0][3] = True
                        else:
                            CHEMICAL[0][3] = False

                    elif i == 1:
                        if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (CHEMICAL[1][8] -50, 400))) == True:
                            CHEMICAL[1][3] = True
                        else:
                            CHEMICAL[1][3] = False

                    elif i == 2:
                        if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (CHEMICAL[2][8] -50, 400))) == True:
                            CHEMICAL[2][3] = True
                        else:
                            CHEMICAL[2][3] = False

                    i = i + 1

            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (BEAKER[0], BEAKER[1]))) == True:
                MOUSE_BEAKER = True
            else:
                MOUSE_BEAKER = False


            MOUSEXY = pygame.mouse.get_pos()


            ##MOUSE BUTTON EVENTS

            if event.type == MOUSEBUTTONUP:

                #NEW BEAKER

                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (800, 120))) == True and BEAKER[0] == -100:
                    BEAKER = [500, 400, True]
                    REAGENTS_ADDED = ["", "", ""]
                    holdbeaker.play()

                #CHANGE TEMPERATURE

                if check_mouseon(pygame.mouse.get_pos(), pygame.draw.rect(DISPLAYSURF, BLUE, (60, 348, 15, 10))) == True and not (True in SHELF_OPEN):
                    TEMPERATURE = TEMPERATURE + 5
                    tempbeep.play()

                        

                elif check_mouseon(pygame.mouse.get_pos(), pygame.draw.rect(DISPLAYSURF, BLUE, (60, 360, 15, 10))) == True and not (True in SHELF_OPEN):
                    TEMPERATURE = TEMPERATURE - 5
                    tempbeep.play()

                #OPEN AND CLOSE WINDOW

                
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('windowclosed.png'), (50, 100))) == True and not (True in SHELF_OPEN):
                    if WINDOW_OPEN == False:
                        WINDOW_OPEN = True
                        opencurtain.play()
                    elif WINDOW_OPEN == True:
                        WINDOW_OPEN = False
                        opencurtain.play()

                #REFLUX

                
                if check_mouseon(pygame.mouse.get_pos(), pygame.draw.rect(DISPLAYSURF, WHITE, (885, 185, 15, 15))) == True and not (True in SHELF_OPEN):
                    if REFLUX == False:
                        REFLUX = True
                        opencurtain.play()
                    
                    
    

                #PROCEED TO NEXT LEVEL

                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('proceedbutton.png'), (500, 120))) == True:
                    LEVEL_UP_SCREEN = False

                #CHECK IF ANSWER IS RIGHT
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('submitbutton.png'), (800, 50))) == True and (CHEMICAL[0][4] == True or CHEMICAL[1][4] == True or CHEMICAL[2][4] == True):

                    

                    i = 0
                    for num in CHEMICAL:
                        if (num[4] == True) and (SHELF_OPEN == [False, False, False, False, False]) and num[7] == True:

                            if i == 0:
                                if CHEMICAL[0][2] == ANSWER:
                                    SUBMITTED_CORRECT = True
                                IS_BEAKER_PICKED = False
                                if CHEMICAL[0][10] == False and CHEMICAL[0][5] < 100:
                                    BEAKER_REMOVED[CHEMICAL[0][5]][CHEMICAL[0][6]] = False
                                CHEMICAL[0] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                CHEMICAL[1][4] = False
                                CHEMICAL[2][4] = False

                            elif i == 1:
                                if CHEMICAL[0][2] == ANSWER:
                                    SUBMITTED_CORRECT = True
                                IS_BEAKER_PICKED = False
                                if CHEMICAL[1][10] == False and CHEMICAL[1][5] < 100:
                                    BEAKER_REMOVED[CHEMICAL[1][5]][CHEMICAL[1][6]] = False
                                CHEMICAL[1] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                CHEMICAL[0][4] = False
                                CHEMICAL[2][4] = False

                            elif i == 2:
                                if CHEMICAL[0][2] == ANSWER:
                                    SUBMITTED_CORRECT = True
                                     
                                IS_BEAKER_PICKED = False
                                if CHEMICAL[2][10] == False and CHEMICAL[2][5] < 100:
                                    BEAKER_REMOVED[CHEMICAL[2][5]][CHEMICAL[2][6]] = False
                                CHEMICAL[2] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                CHEMICAL[1][4] = False
                                CHEMICAL[0][4] = False


                        i = i + 1

                    if SUBMITTED_CORRECT == True:
                        SCORE = SCORE + REQUEST[2]
                        ANSWERS_RIGHT = ANSWERS_RIGHT + 1
                        QUESTION_ANSWERED = False
                        CHEMICAL_CORRECT = False
                        SUBMITTED_CORRECT = False
                        REFLUXED = False
                        correctanswer.play()

                    elif SUBMITTED_CORRECT == False:
                        CHEMICAL_CORRECT = False
                        QUESTION_ANSWERED = False
                        ANSWERS_WRONG = ANSWERS_WRONG + 1
                        REFLUXED = False
                        answerwrong.play()


                #QUIT GAME
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('discardbutton.png'), (800, 600))) == True:
    
                    buttonpress.play()
                    GAME_OVER = True
                    PLAYING_GAME = False
                    MONEY = MONEY + SCORE

                    if SCORE > HIGH_SCORE:
                        HIGH_SCORE = SCORE

                #FEED VICTOR

                #PICK UP A DONUT


                elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('donut.png'), (180, 55))) == True:
                    if DONUTS > 0:
                        if DONUT_PICKED == False:
                            DONUT_PICKED = True
                        elif DONUT_PICKED == True:
                            DONUT_PICKED = False

                elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('donut.png'), (210, 55))) == True:
                    if DONUTS > 1:
                        if DONUT_PICKED == False:
                            DONUT_PICKED = True
                        elif DONUT_PICKED == True:
                            DONUT_PICKED = False

                elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('donut.png'), (240, 55))) == True:
                    if DONUTS > 2:
                        if DONUT_PICKED == False:
                            DONUT_PICKED = True
                        elif DONUT_PICKED == True:
                            DONUT_PICKED = False

                elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('donut.png'), (270, 55))) == True:
                    if DONUTS > 3:
                        if DONUT_PICKED == False:
                            DONUT_PICKED = True
                        elif DONUT_PICKED == True:
                            DONUT_PICKED = False

                #FEED TO VICTOR

                elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('victor.png'), (800, 250))) == True:
                    if DONUT_PICKED:
                        DONUT_PICKED = False
                        DONUTS = DONUTS - 1
                        VICTOR_FED = True
                        HINT_TIMER = HINT_DURATION
                        HINT_NUMBER = random.randrange(0, 2)

                

                

                #PICK UP AND PLACE REACTION BEAKER

                if BEAKER[2] == False:
                    if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakerempty.png'), (BEAKER[0], 400))) == True:
                        BEAKER[2] = True
                        holdbeaker.play()
                elif BEAKER[2] == True:
                    if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('benchrect.png'), (180, 400))) == True:
                        BEAKER[0] = MOUSEXY[0] - 50
                        BEAKER[1] = 400
                        BEAKER[2] = False
                        placebeaker.play()
                        
                #OPEN OR CLOSE A SHELF

                TILEX = 50
                TILEY = 550
                i = 0
                
                for num in SHELF_FOCUSED:
                    if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('shelfthumb.png'), (TILEX, TILEY))) == True:
                        SHELF_OPEN = [False, False, False, False, False]
                        SHELF_OPEN[i] = True
                        pygame.mixer.Sound('openshelf.wav').play()
    
                    elif check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('backbutton.png'), (600, 480))) == True:
                        SHELF_OPEN[i] = False
                        SHELF_OPEN = [False, False, False, False, False]

                    TILEX = TILEX + 150
                    i = i + 1

                #PICK UP A BEAKER FROM SHELF AND ADD TO LIST

                TILEX = 100
                TILEY = 115
                i = 0
                j = 0
                BEAKERS = 0

                for num in SHELF_OPEN:
                    if num == True and IS_BEAKER_PICKED == False:
                        for num in BEAKER_FOCUSED[i]:
                    
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (TILEX, TILEY))) == True  and BEAKER_UNLOCKED[i][j] == 1:
                                BEAKER_PICKED = [PRODUCT_COLORS[BEAKER_NAMES[i][j]], BEAKER_NAMES[i][j], i, j]
                                IS_BEAKER_PICKED = True
                                holdbeaker.play()
                                BEAKER_REMOVED = [[False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,],
                [False, False, False, False, False, False,
                 False, False, False, False, False, False,
                 False, False, False, False, False, False,]]

                                BEAKER_REMOVED[i][j] = True
                                if CHEMICAL[0][0] == False:
                                    CHEMICAL[0] = [True, BEAKER_PICKED[0], BEAKER_PICKED[1], False, True, BEAKER_PICKED[2], BEAKER_PICKED[3], True, MOUSEXY[0], MOUSEXY[1], False]
                                elif CHEMICAL[1][0] == False:
                                    CHEMICAL[1] = [True, BEAKER_PICKED[0], BEAKER_PICKED[1], False, True, BEAKER_PICKED[2], BEAKER_PICKED[3], True, MOUSEXY[0], MOUSEXY[1], False]
                                elif CHEMICAL[2][0] == False:
                                    CHEMICAL[2] = [True, BEAKER_PICKED[0], BEAKER_PICKED[1], False, True, BEAKER_PICKED[2], BEAKER_PICKED[3], True, MOUSEXY[0], MOUSEXY[1], False]
    ##                        else:
    ##                            BEAKER_FOCUSED[i][j] = False

                            TILEX = TILEX + 70
                            BEAKERS = BEAKERS + 1
                            if BEAKERS == 6:
                                TILEX = 100
                                TILEY = 263
                            if BEAKERS == 12:
                                TILEX = 100
                                TILEY = 415
                            j = j + 1
        
                    i = i + 1
                    j = 0
                    BEAKERS = 0

                #PLACE BEAKER ON BENCH AND ADD TO LIST OF BEAKERS ON BENCH

                if IS_BEAKER_PICKED is True and (SHELF_OPEN == [False, False, False, False, False]) and (check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('bench.png'), (180,400))) == True):
                    IS_BEAKER_PICKED = False
                    BEAKER_PICKED == [0, "", 0, 0]
                    placebeaker.play()
                    
                    if CHEMICAL[0][4] == True:
                        CHEMICAL[0][8] = MOUSEXY[0]

                    elif CHEMICAL[1][4] == True:
                        CHEMICAL[1][8] = MOUSEXY[0]

                    elif CHEMICAL[2][4] == True:
                        CHEMICAL[2][8] = MOUSEXY[0]
                    
                    CHEMICAL[0][4] = False
                    CHEMICAL[1][4] = False
                    CHEMICAL[2][4] = False
                    
                    
                    
                    
                    

                #PICK UP AND REPLACE BEAKERS ON THE BENCH

                elif IS_BEAKER_PICKED == False:

                    i = 0
                    for num in CHEMICAL:
                        if (num[4] == False) and (SHELF_OPEN == [False, False, False, False, False]) and IS_BEAKER_PICKED == False and num[7] == True:
                            if i == 0: 
                                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (CHEMICAL[0][8] - 50, 400))) == True:
                                    CHEMICAL[0][4] = True
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[2][4] = False
                                    holdbeaker.play()
                            elif i == 1: 
                                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (CHEMICAL[1][8] - 50, 400))) == True:
                                    CHEMICAL[1][4] = True
                                    CHEMICAL[0][4] = False
                                    CHEMICAL[2][4] = False
                                    holdbeaker.play()
                                    

                            elif i == 2: 
                                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('beakertransparent.png'), (CHEMICAL[2][8] - 50, 400))) == True:
                                    CHEMICAL[2][4] = True
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[0][4] = False
                                    holdbeaker.play()

                        #PLACE A BEAKER
                                    
                        elif (num[4] == True) and (SHELF_OPEN == [False, False, False, False, False]) and IS_BEAKER_PICKED == False and num[7] == True:
                            if i == 0: 
                                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('benchrect.png'), (180, 400))) == True:

                                    if CHEMICAL[0][4] == True:
                                        CHEMICAL[0][8] = MOUSEXY[0]
                                        CHEMICAL[0][9] = 400

                                    if CHEMICAL[0][3] == False:
                                        CHEMICAL[0][3] = True

                                    CHEMICAL[0][4] = False
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[2][4] = False
                                    placebeaker.play()
                                    
                            if i == 1: 
                                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('benchrect.png'), (180, 400))) == True:

                                    if CHEMICAL[1][4] == True:
                                        CHEMICAL[1][8] = MOUSEXY[0]
                                        CHEMICAL[1][9] = 400

                                    if CHEMICAL[0][3] == False:
                                        CHEMICAL[0][3] = True

                                    CHEMICAL[1][4] = False
                                    CHEMICAL[0][4] = False
                                    CHEMICAL[2][4] = False
                                    placebeaker.play()
                                    

                            if i == 2: 
                                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('benchrect.png'), (180, 400))) == True:

                                    if CHEMICAL[2][4] == True:
                                        CHEMICAL[2][8] = MOUSEXY[0]
                                        CHEMICAL[2][9] = 400

                                    elif CHEMICAL[0][3] == False:
                                        CHEMICAL[0][3] = True
                                    CHEMICAL[2][4] = False
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[0][4] = False
                                    placebeaker.play()
                                    

                            
                            

                        i = i + 1

                #POUR 

                i = 0
                for num in CHEMICAL:
                    if (num[4] == True) and (SHELF_OPEN == [False, False, False, False, False]) and num[7] == True:

                        BEAKERX = BEAKER[0] - 75
                        
                        if i == 0: 
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('startbutton.png'), (BEAKERX, 300))) == True:

                                if REAGENTS_ADDED[0] == "":
                                    REAGENTS_ADDED[0] = CHEMICAL[0][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[0][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[0][5]][CHEMICAL[0][6]] = False
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[2][4] = False
                                    CHEMICAL[0] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    WAIT_TIMER = WAIT_ORIGINAL
                                    WAITED = False
                                    
                                    
                                    
                                    react(1)

                                elif REAGENTS_ADDED[1] == "":
                                    REAGENTS_ADDED[1] = CHEMICAL[0][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[0][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[0][5]][CHEMICAL[0][6]] = False
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[2][4] = False
                                    CHEMICAL[0] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    WAIT_TIMER = WAIT_ORIGINAL
                                    WAITED = False
                                    
                                    
                                    react(1)

                                elif REAGENTS_ADDED[2] == "":
                                    REAGENTS_ADDED[2] = CHEMICAL[0][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[0][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[0][5]][CHEMICAL[0][6]] = False
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[2][4] = False
                                    CHEMICAL[0] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    WAIT_TIMER = WAIT_ORIGINAL
                                    WAITED = False
                                    
                                    react(1)
                                
                                
                        elif i == 1: 
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('startbutton.png'), (BEAKERX, 300))) == True:

                                if REAGENTS_ADDED[0] == "":
                                    REAGENTS_ADDED[0] = CHEMICAL[1][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[1][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[1][5]][CHEMICAL[1][6]] = False
                                    CHEMICAL[1] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    CHEMICAL[0][4] = False
                                    CHEMICAL[2][4] = False
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    
                                    react(1)
                                


                                elif REAGENTS_ADDED[1] == "":
                                    REAGENTS_ADDED[1] = CHEMICAL[1][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[1][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[1][5]][CHEMICAL[1][6]] = False
                                    CHEMICAL[1] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    CHEMICAL[0][4] = False
                                    CHEMICAL[2][4] = False
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    
                                    react(1)

                                elif REAGENTS_ADDED[2] == "":
                                    REAGENTS_ADDED[2] = CHEMICAL[1][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[1][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[1][5]][CHEMICAL[1][6]] = False
                                    CHEMICAL[1] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    CHEMICAL[0][4] = False
                                    CHEMICAL[2][4] = False
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    
                                    react(1)
                                

                        elif i == 2: 
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('startbutton.png'), (BEAKERX, 300))) == True:

                                if REAGENTS_ADDED[0] == "":
                                    REAGENTS_ADDED[0] = CHEMICAL[2][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[2][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[2][5]][CHEMICAL[2][6]] = False
                                    CHEMICAL[2] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[0][4] = False
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    
                                    react(1)

                                elif REAGENTS_ADDED[1] == "":
                                    REAGENTS_ADDED[1] = CHEMICAL[2][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[2][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[2][5]][CHEMICAL[2][6]] = False
                                    CHEMICAL[2] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[0][4] = False
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX+ 120, 300)
                                    
                                    react(1)

                                elif REAGENTS_ADDED[2] == "":
                                    REAGENTS_ADDED[2] = CHEMICAL[2][2]
                                    IS_BEAKER_PICKED = False
                                    if CHEMICAL[2][10] == False and CHEMICAL[0][5] < 100:
                                        BEAKER_REMOVED[CHEMICAL[2][5]][CHEMICAL[2][6]] = False
                                    CHEMICAL[2] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                    CHEMICAL[1][4] = False
                                    CHEMICAL[0][4] = False
                                    pourchemical.play()
                                    SOUND_POUR = True
                                    FREEZEXY = (BEAKERX + 120, 300)
                                    
                                    react(1)

                    

                        

                        #DISCARD A REAGENT
                        
                        if i == 0: 
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('discardbutton.png'), (30, 400))):     
                                IS_BEAKER_PICKED = False
                                if CHEMICAL[0][10] == False:
                                    BEAKER_REMOVED[CHEMICAL[0][5]][CHEMICAL[0][6]] = False
                                CHEMICAL[0] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                CHEMICAL[1][4] = False
                                CHEMICAL[2][4] = False
                                pourchemical.play()
                                SOUND_POUR = True
                                FREEZEXY = (150, 350)
                                if WASTE < 100:
                                    WASTE = WASTE + WASTE_STEP
                                    if WASTE == 100:
                                        GAME_OVER = True
                                        PLAYING_GAME = False
                                        MONEY = MONEY + SCORE

                                        if SCORE > HIGH_SCORE:
                                            HIGH_SCORE = SCORE

                        elif i == 1: 
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('discardbutton.png'), (30, 400))):     
                                IS_BEAKER_PICKED = False
                                if CHEMICAL[1][10] == False:
                                    BEAKER_REMOVED[CHEMICAL[1][5]][CHEMICAL[1][6]] = False
                                CHEMICAL[1] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                CHEMICAL[0][4] = False
                                CHEMICAL[2][4] = False
                                pourchemical.play()
                                SOUND_POUR = True
                                FREEZEXY = (150, 350)
                                if WASTE < 100:
                                    WASTE = WASTE + WASTE_STEP
                                    if WASTE == 100:
                                        GAME_OVER = True
                                        PLAYING_GAME = False
                                        MONEY = MONEY + SCORE

                                        if SCORE > HIGH_SCORE:
                                            HIGH_SCORE = SCORE

                        elif i == 2: 
                            if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('discardbutton.png'), (30, 400))):     
                                IS_BEAKER_PICKED = False
                                if CHEMICAL[2][10] == False:
                                    BEAKER_REMOVED[CHEMICAL[2][5]][CHEMICAL[2][6]] = False
                                CHEMICAL[2] = [False,     "",     "", False,  False, 10000, 10000, False, 0,0, False]
                                CHEMICAL[1][4] = False
                                CHEMICAL[0][4] = False
                                pourchemical.play()
                                SOUND_POUR = True
                                FREEZEXY = (150, 350)
                                if WASTE < 100:
                                    WASTE = WASTE + WASTE_STEP
                                    if WASTE == 100:
                                        GAME_OVER = True
                                        PLAYING_GAME = False
                                        MONEY = MONEY + SCORE

                                        if SCORE > HIGH_SCORE:
                                            HIGH_SCORE = SCORE



                        
                    i = 1+ i
                    

                    

                #DISCARD ALL REAGENTS
            
                if check_mouseon(pygame.mouse.get_pos(), DISPLAYSURF.blit(pygame.image.load('discardbutton.png'), (30, 400))) == True and BEAKER[2] == True:
##                    IS_BEAKER_PICKED = False
                    
                    if not (REAGENTS_ADDED == ["", "", ""]):
                        pourchemical.play()
                        SOUND_POUR = True
                        FREEZEXY = (150, 350)
                        
                        if WASTE < 100:
                            WASTE = WASTE + WASTE_STEP
                            if WASTE == 100:
                                GAME_OVER = True
                                PLAYING_GAME = False
                                MONEY = MONEY + SCORE

                                if SCORE > HIGH_SCORE:
                                    HIGH_SCORE = SCORE

                    else:
                        breakbeaker.play()
                        
                    REAGENTS_ADDED = ["", "", ""]
                    BEAKER = [-100, 400, False]
                    REFLUXED = False

                    
                    
 

    ##START SCREEN FUNCTIONS

    draw_startscreen()
    
    ##LEVEL SELECT FUNCTIONS

    draw_levelselect()
    
    draw_shop()
    
    ##GAMEPLAY FUNCTIONS

    draw_gamescreen()

    check_shaken()
    wait()
    
    ##FOREGROUND FUNCTIONS

    draw_shelves()
    draw_shelf_chemicals()
    

    draw_bench()

    level()

    level_up()

    hold_chemical(MOUSEXY[0] - 50, MOUSEXY[1])

    react(0)

    if LEVEL_UP_SCREEN == True and PLAYING_GAME == True:
                DISPLAYSURF.blit(pygame.image.load('proceedbutton.png'), (500, 120))

    display_score()
    
    if LEVEL == 1 and STORY == True:
        draw_story()

    game_over()

    play_sound()
    

    
    


        

            

    pygame.display.update()

    fpsClock.tick(FPS)
