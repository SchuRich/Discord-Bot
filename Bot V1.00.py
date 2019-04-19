import discord
from discord.ext import commands
import Halp_py_test

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

#Seek 0 Halp
@bot.command()
async def Halp(ctx):
    await Halp_py_test.Halp(ctx)

#Seek 1 Links_Info
@bot.command()
async def Links_Info(ctx):
    await Halp_py_test.Links_Info(ctx)

#Seek 2 Game_Info
@bot.command()
async def Game_Info(ctx):
    await Halp_py_test.Game_Info(ctx)

#Seek 3 Update_Info
@bot.command()
async def Update_Info(ctx):
    await Halp_py_test.Update_Info(ctx)

#Seek 4 Staff_Info
@bot.command()
async def Staff_Info(ctx):
    await Halp_py_test.Staff_Info(ctx)

#Seek 5 Servers_Info
@bot.command()
async def Servers_Info(ctx):
    await Halp_py_test.Servers_Info(ctx)


#Seek 6 Quests_Info
@bot.command()
async def Quests_Info(ctx):
    await Halp_py_test.Quests_Info(ctx)

#Seek 7 Brutals_Info
@bot.command()
async def Brutals_Info(ctx):
    await Halp_py_test.Brutals_Info(ctx)


@bot.command()
async def Brutals_Enigma(ctx):
    await Halp_py_test.Brutals_Enigma(ctx)











#Seek 8 Mights_Info
@bot.command()
async def Mights_Info(ctx):
    await Halp_py_test.Mights_Info(ctx)

#Seek 9 Reborn_Info
@bot.command()
async def Reborn_Info(ctx):
    await Halp_py_test.Reborn_Info(ctx)







































