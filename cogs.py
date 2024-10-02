import nextcord
from nextcord.ext import commands
import time
from api_client import APIClient

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(f'Pong! `{round(self.bot.latency * 1000)}ms`')

    @commands.command(name="query", aliases=["q"])
    async def query(self, ctx: commands.Context, *args):

        # get clear lb data
        api_client = APIClient()
        response, mode = api_client.get_clears(args)
        data = response.json()

        if response.status_code != 200:
            await ctx.send(f"Error: Status {response.status_code} - {response.text}")

        # embed
        content = "```pascal\n"
        for row in data['players']:
            fixed_user = row['name'].ljust(17)
            fixed_rank = str(row['rank']).ljust(3)
            fixed_number = row['clears']

            content = f'{content}#{fixed_rank} | {fixed_user} | {fixed_number}\n'

        if content == "```pascal\n":
            content += "No result\n"

        datetime = time.strftime('%H:%M', time.localtime(time.time()))

        mode_icons = (
            'https://cdn.discordapp.com/emojis/1201755183516753920.webp',  # std, 0, 4, 8
            'https://cdn.discordapp.com/emojis/1201755185425154048.webp',  # taiko 1, 5
            'https://cdn.discordapp.com/emojis/1201755188608892938.webp',  # ctb 2, 6
            'https://cdn.discordapp.com/emojis/1201755192115068948.webp'   # mania 3, 7
        )

        if mode in [0, 4, 8]:
            icon_url = mode_icons[0]
        elif mode in [1, 5]:
            icon_url = mode_icons[1]
        elif mode in [2, 6]:
            icon_url = mode_icons[2]
        elif mode in [3, 7]:
            icon_url = mode_icons[3]
        else:
            icon_url = mode_icons[0]


        embed = nextcord.Embed(color=0xb260e3, title='Clears')
        embed.description = content + '```'
        embed.set_footer(text='Requested by ' + ctx.author.display_name + ' at ' + datetime, icon_url=icon_url)

        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Commands(bot))