import os 
import discord
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

keep_alive()
bot.run(os.environ['token'])