import nextcord
from nextcord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.api_client = bot.get_cog('APIClient')
    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'Pong! `{round(self.bot.latency * 1000)}ms`')

    @commands.command(name="query", aliases=["q"])
    async def query(self, ctx: commands.Context, *args):
        if self.api_client is not None:
            response = self.api_client.get_clears()
            if response is None:
                response = "bruh etwas kaputt"
            await ctx.send(response)

def setup(bot):
    bot.add_cog(Commands(bot))