import discord
from discord.ext import commands

dwacription = "test"

bot = commands.Bot(
    command_prefix='!',
    description="VFO comunity Bot",
    case_insensitive=True,
    pm_help=True)   #Not working

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Loged In")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    ignored = (commands.CommandNotFound)
    if isinstance(error, ignored):
        print("Command Error Ignored")
        return


@bot.command()
async def Halp(ctx):
    await ctx.send(
        "1-> !Commands_Info **X**\n"
        "2-> !Game_Info\n"
        "3-> !Update_Info\n"
        "4-> !Staff_Info\n"
        "5-> !Servers_List **X**\n"
        "6-> !Quest_Info **X**\n"
        "7-> !Brutals_Info **X**\n"
        "8-> !Might_Info **X**\n"
        "9-> !Reborn_Info **X**\n"
        "10-> !Item_Info **X**")

#Seek Commands Info
@bot.command()
async def Commands_Info(ctx):
    await ctx.send("**__Commands__**")

#Seek Game Info
@bot.command()
async def Game_Info(ctx):
    await ctx.send(
        "**__Developer__** --> Early Morning Studio\n"
        "**__Publisher__** --> Early Morning Studio\n"
        "**__Platforms__** --> Android / Apple\n"
        "**__Release date__** --> September 8, 2018\n"
        "**__Genre__** --> RPG\n"
        "**__Mode__** --> Singleplayer (Offline) , Multiplayer\n\n"
        "**__System requirements__**\n"
        "__Android__ - 97 MB Storage space / Android 4.1+\n"
        "__Apple__ - 468.9 MB Storage space / Requires iOS 10.0+ / Compatible with iPhone, iPad, and iPod touch.")

#Seek Update Info
@bot.command()
async def Update_Info(ctx):
    await ctx.send("__**Update 1.1.2**__\n"
                   "- NG+\n"
                   "- Stun in PvP now reduces focus instead of properly stunning in combo turns\n"
                   "- Item Augmentation\n"
                   "- Raised level cap to 75\n"
                   "- Ability to remove bloodstones from items\n"
                   "- Creature Lure potions available in stores\n"
                   "- Removed Armor Cap\n"
                   "- Less effect from bloodstones for stun, block chance, crit. dmg and crit. hit\n"
                   "- Displaying PvP-resilience values in PvP-menu\n"
                   "- Added  shield block resilience in PvP\n"
                   "- General bug fixes")

#Seek Servers List
@bot.command()
async def Servers_List(ctx):
    await ctx.send("**__All Avaleable Discord Servers__**\n\n"
                   "https://discord.gg/mjAYUTW\n"
                   "https://discord.gg/RcRAMMp\n"
                   "https://discord.gg/WHNWwM6\n"
                   "https://discord.gg/yKvyuQa\n"
                   "https://discord.gg/pg6ZW9b\n"
                   "https://discord.gg/7NJXXky\n"
                   "https://discord.gg/jSNd9fj\n"
                   "https://discord.gg/7uQFa6q")

#





