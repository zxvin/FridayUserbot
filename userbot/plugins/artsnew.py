#New arts added by @Sur_vivor
import asyncio
from telethon import events
from telethon.tl import functions, types
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

n = str(ALIVE_NAME) if ALIVE_NAME else "Sur_vivor"

emojis = {
    "yee": "ツ",
    "happy": "(ʘ‿ʘ)",
    "veryhappy": "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
    "amazed": "ヾ(o✪‿✪o)ｼ",
    "crying": "༎ຶ︵༎ຶ",
    "dicc": "╰U╯☜(◉ɷ◉ )",
    "fek": "╰U╯\n(‿ˠ‿)",
    "ded": "✖‿✖",
    "sad": "⊙︿⊙",
    "lenny": "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "idc": "¯\_(ツ)_/¯",
    "f": "😂😂😂😂😂😂😂😂\n😂😂😂😂😂😂😂😂😂\n😂😂\n😂😂\n😂😂😂😂😂😂\n😂😂😂😂😂😂\n😂😂\n😂😂\n😂😂\n😂😂\n😂😂"
}

unpacked_emojis = ""

for emoji in emojis:
    unpacked_emojis += f"`{emoji}`\n"

ascii = {
    "mf": "'                            / ¯͡  ) \n                           /...../ \n                         /´¯´/ \n                       /¯..../ \n                    /....  / \n             /´¯/'...' /´¯¯·¸ \n          / '/.../..../..../.. /¨¯\ \n        ('(...´...´.... ¯~'/...')  /\n         \.................'..... /´ \n          \................ _.·´\n            \..............( \n'             \.............\ ",
    "dislike": "███████▄▄███████████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀░░█░░░░██████▀\n░░░░░░░░░█░░░░█\n░░░░░░░░░░█░░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░░▀▀ ",
    "music": "╔══╗ \n║██║ \n║(O)║♫ ♪ ♫ ♪\n╚══╝\n▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █\n\nVol- --------------------------● Vol+ ",
    "chess": "♜♞♝♚♛♝♞♜\n♟♟♟♟♟♟♟♟\n▓░▓░▓░▓░\n░▓░▓░▓░▓\n▓░▓░▓░▓░\n░▓░▓░▓░▓\n♙♙♙♙♙♙♙♙\n♖♘♗♔♕♗♘♖ ",
    "shitos": "╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯ ",
    "qrcode": "█▀▀▀▀▀█░▀▀░░░█░░░░█▀▀▀▀▀█\n█░███░█░█▄░█▀▀░▄▄░█░███░█\n█░▀▀▀░█░▀█▀▀▄▀█▀▀░█░▀▀▀░█\n▀▀▀▀▀▀▀░▀▄▀▄▀▄█▄▀░▀▀▀▀▀▀▀\n█▀█▀▄▄▀░█▄░░░▀▀░▄█░▄▀█▀░▀\n░█▄▀░▄▀▀░░░▄▄▄█░▀▄▄▄▀▄▄▀▄\n░░▀█░▀▀▀▀▀▄█░▄░████ ██▀█▄\n▄▀█░░▄▀█▀█▀░█▄▀░▀█▄██▀░█▄\n░░▀▀▀░▀░█▄▀▀▄▄░▄█▀▀▀█░█▀▀\n█▀▀▀▀▀█░░██▀█░░▄█░▀░█▄░██\n█░███░█░▄▀█▀██▄▄▀▀█▀█▄░▄▄\n█░▀▀▀░█░█░░▀▀▀░█░▀▀▀▀▄█▀░\n▀▀▀▀▀▀▀░▀▀░░▀░▀░░░▀▀░▀▀▀▀` ",
    "youjoined": "━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When \n┓┓┓┓┓┃.      /　        You Joined\n┓┓┓┓┓┃  ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃ "
}

unpacked_ascii = ""

for art in ascii:
    unpacked_ascii += f"{art}\n"

@borg.on(admin_cmd(pattern="hek ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    for _ in range(5):
        await event.edit(";_;")
        await event.edit("_;;")
        await event.edit(";;_")
    await event.edit(";_;")


@borg.on(admin_cmd(pattern="sed ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    for _ in range(4):
        await event.edit(":/")
        await event.edit(":|")
        await event.edit(":\\")
        await event.edit(":|")
    await event.edit(":/")


@borg.on(admin_cmd(pattern="emoji ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_emoji = emojis[str(input_str)]
        await event.edit(req_emoji)
    except KeyError:
        await event.edit("Emoji not found!")


@borg.on(admin_cmd(pattern="ascii ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_ascii = ascii[str(input_str)]
        await event.edit(req_ascii)
    except KeyError:
        await event.edit("ASCII art not found!")    
    
@borg.on(admin_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await ded.edit(n + " ==             |\n　　　　　|" "\n　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")

M = ("…………..$…………………GO…...…………..$…\n"
"…………$$…………………TO....................$$…\n"
"…………$$……………….HELL…………...$$…\n"
"…………..$$s………………………………s$$………\n"
"…………….$$$$……………………….$$$$………\n"
"………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………\n"
"_………………..³$$$$..¶¶¶¶¶¶..$$$$³………\n"
"………………¶..$$$$$..¶¶¶¶..$$$$$..¶………"\n
"…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶…"\n
"………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶…\n"
"………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n"
"……………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶…\n"
"……………..¶¶……..¶¶¶¶……….¶……………\n"
"……………..¶¶……..¶¶¶¶……….¶¶…………\n"
"……………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶……\n"
"……………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………\n"
"…………………….¶¶¶¶¶¶¶¶¶………………\n"
"…………………….¶..¶..¶..¶..¶…………………\n"
"………¶…………..¶…………..¶……...¶………….\n"
"…….¶¶…DON'T MESS WITH ....¶¶………\n"
"…….¶¶……………………………….….¶¶……\n"
"……¶¶………..¶¶…......….¶¶……..¶¶……\n"
"…¶¶..¶¶..¶¶..¶……...….¶..¶¶..¶¶..¶¶……\n"
"¶..¶¶..¶¶..¶¶..¶……....¶..¶¶..¶¶..¶¶..¶…\n"
"¶¶..¶¶..¶¶..¶¶..¶……..¶..¶¶..¶¶..¶¶..¶¶\n"
"…¶¶¶¶..¶¶..¶¶……....….¶¶..¶¶..¶¶¶¶…\n")
     
     
     
P = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")

K = ("_/﹋\_\n"
"(҂`_´)\n"
"<,︻╦╤─ ҉ - -\n"
"_/﹋\_\n")

G = ("╔══╗        🎧\n"
"║██║  Nice ya ! ( •̮ •)\n"
"║(O)║♫ ♪ ♫ ♪      /█\\n"
"╚══╝                     .Π.\n"
"▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █\n"
"Min- - - - - - - - - - - -●Max\n")

D = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
H = ("╔┓┏╦━╦┓╔┓╔━━╗\n" 
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n")
E = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

C = ("┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
"┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
"┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
"┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
"┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
"┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
"┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
"┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
"┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
"┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
"┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
"┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
"┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
"┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
"Love You Forever,,,,\n")

S = (".......🦋🦋........🦋🦋\n"
"...🦋.........🦋🦋.......🦋\n"
"...🦋............💙...........🦋\n"
".....🦋🅣🅗🅐🅝🅚🅢🦋\n"
"......... 🦋.................🦋\n"
"................🦋......🦋\n"
"......................💙\n")

W = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

Z = ("░░░░▓\n"
"░░░▓▓\n"
"░░█▓▓█\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓███\n"
"░░░░██▓▓████\n"
"░░░░░██▓▓█████\n"
"░░░░░░██▓▓██████\n"
"░░░░░░███▓▓███████\n"
"░░░░░████▓▓████████\n"
"░░░░█████▓▓█████████\n"
"░░░█████░░░█████●███\n"
"░░████░░░░░░░███████\n"
"░░███░░░░░░░░░██████\n"
"░░██░░░░░░░░░░░████\n"
"░░░░░░░░░░░░░░░░███\n"
"░░░░░░░░░░░░░░░░░░░\n")

B = ("────██───\n"
"──▄▀█▄▄▄─────\n"
"▄▀──█▄▄──────\n"
"─▄▄▄▀──▀▄───\n"
"─▀───────▀▀─\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ..")


@borg.on(admin_cmd(pattern=r"monster"))
async def bluedevilmonster(monster):
    await monster.edit(M)
@borg.on(admin_cmd(pattern=r"pig"))
async def bluedevilpig(pig):
    await pig.edit(P)
@borg.on(admin_cmd(pattern=r"kiler"))
async def bluedevilkiller(kiler):
    await kiler.edit(K)
@borg.on(admin_cmd(pattern=r"muusic"))
async def bluedevilgun(gun):
    await gun.edit(G)
@borg.on(admin_cmd(pattern=r"dog"))
async def bluedevildog(dog):
    await dog.edit(D)    
@borg.on(admin_cmd(pattern=r"hello"))
async def bluedevilhello(hello):
    await hello.edit(H)
@borg.on(admin_cmd(pattern=r"hmf"))
async def bluedevilhmf(hmf):
    await hmf.edit(E)
@borg.on(admin_cmd(pattern=r"couple"))
async def bluedevilcouple(couple):
    await couple.edit(C)
@borg.on(admin_cmd(pattern=r"tnk"))
async def bluedevilsupreme(supreme):
    await supreme.edit(S)
@borg.on(admin_cmd(pattern=r"wlcm"))
async def bluedevilwelcome(welcome):
    await welcome.edit(W)
@borg.on(admin_cmd(pattern=r"snk"))
async def bluedevilsnake(snake):
    await snake.edit(Z)
@borg.on(admin_cmd(pattern=r"bye"))
async def bluedevilbye(bye):
    await bye.edit(B)    
