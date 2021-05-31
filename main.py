import os 
import discord
import random
from discord.ext import commands
from keep_alive import keep_alive

welcome_message = ['Welcome {}','You made it.{} is here.','{} Did you brought a pizza for us?','Welcome! We’re thrilled to have you with us {}']

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),intents=intents)

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
      ch = bot.get_channel(848784007487029260)
      await ch.send(random.choice(welcome_message).format(member.mention))
      
    @commands.Cog.listener()
    async def on_member_remove(self,member):
      ch = bot.get_channel(848793823106957343)
      await ch.send("🥺 Bye {0.name}".format(member))
      
bot.add_cog(Greetings(bot))
      
keep_alive()
bot.run(os.environ['token'])