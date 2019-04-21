import discord
from discord.ext import commands
import Halp_py

description = "test"

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

#Seek 0 Halp
@bot.command()
async def Halp(ctx):
    await Halp_py.Halp(ctx)

#Seek 1 Links_Info
@bot.command()
async def Links_Info(ctx):
    await Halp_py.Links_Info(ctx)

#Seek 2 Game_Info
@bot.command()
async def Game_Info(ctx):
    await Halp_py.Game_Info(ctx)

#Seek 3 Update_Info
@bot.command()
async def Update_Info(ctx):
    await Halp_py.Update_Info(ctx)

#Seek 4 Staff_Info
@bot.command()
async def Staff_Info(ctx):
    await Halp_py.Staff_Info(ctx)

#Seek 5 Servers_Info
@bot.command()
async def Servers_Info(ctx):
    await Halp_py.Servers_Info(ctx)





#####





#Seek 6 Quests_Info
@bot.command()
async def Quests_Info(ctx):
    await Halp_py.Quests_Info(ctx)





#####





#Seek 7 Brutals_Info
@bot.command()
async def Brutals_Info(ctx):
    await Halp_py.Brutals_Info(ctx)

@bot.command()
async def Brutals_Enigma(ctx):
    await Halp_py.Brutals_Enigma(ctx)

@bot.command()
async def Brutals_TuskTrio(ctx):
    await Halp_py.Brutals_TuskTrio(ctx)

@bot.command()
async def Brutals_RatKing(ctx):
    await Halp_py.Brutals_RatKing(ctx)

@bot.command()
async def Brutals_ABane(ctx):
    await Halp_py.Brutals_ABane(ctx)

@bot.command()
async def Brutals_Xaph(ctx):
    await Halp_py.Brutals_Xaph(ctx)

@bot.command()
async def Brutals_Lerna(ctx):
    await Halp_py.Brutals_Lerna(ctx)

@bot.command()
async def Brutals_Styx(ctx):
    await Halp_py.Brutals_Styx(ctx)

@bot.command()
async def Brutals_SpiritBros(ctx):
    await Halp_py.Brutals_SpiritBros(ctx)

@bot.command()
async def Brutals_MotherOfWolfs(ctx):
    await Halp_py.Brutals_MotherOfWolfs(ctx)

@bot.command()
async def Brutals_BeastOfValley(ctx):
    await Halp_py.Brutals_BeastOfValley(ctx)

@bot.command()
async def Brutals_CaveDweller(ctx):
    await Halp_py.Brutals_CaveDweller(ctx)

@bot.command()
async def Brutals_DeathsAdvocate(ctx):
    await Halp_py.Brutals_DeathsAdvocate(ctx)

@bot.command()
async def Brutals_Fulacks(ctx):
    await Halp_py.Brutals_Fulacks(ctx)

@bot.command()
async def Brutals_HunterKiller(ctx):
    await Halp_py.Brutals_HunterKiller(ctx)

@bot.command()
async def Brutals_RatTree(ctx):
    await Halp_py.Brutals_RatTree(ctx)

@bot.command()
async def Brutals_TheSeals(ctx):
    await Halp_py.Brutals_TheSeals(ctx)




#####





#Seek 8 Mights_Info
@bot.command()
async def Mights_Info(ctx):
    await Halp_py.Mights_Info(ctx)





#####





#Seek 9 Reborn_Info
@bot.command()
async def Reborn_Info(ctx):
    await Halp_py.Reborn_Info(ctx)





#####



































