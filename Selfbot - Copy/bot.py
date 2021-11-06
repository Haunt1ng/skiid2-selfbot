import discord
from discord.ext import commands
from lol import token
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = ">", self_bot = True, intents = discord.Intents().all(), help_command=None)

@bot.event
async def on_ready():
    print("bot is ready")

@bot.command()
async def help(ctx):
    e = discord.Embed(title='commands', description='cmds', color=0x00FF00)
    await ctx.send(embed=e)

bot.run(token, bot=False)
