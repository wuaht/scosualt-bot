import nextcord
from nextcord.ext import commands
import requests

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'Pong! `{round(self.bot.latency * 1000)}ms`')



def setup(bot):
    bot.add_cog(Commands(bot))