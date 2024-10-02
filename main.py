import nextcord
from nextcord.ext import commands
from config import BOT_TOKEN

class DiscordBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')


intents = nextcord.Intents.default()
intents.message_content = True

bot = DiscordBot(command_prefix='!', intents=intents)
extensions = ['cogs']

# Befehle zum Laden, Entladen und Neuladen von Cogs
@bot.command(name='load')
@commands.is_owner()  # Nur der Besitzer des Bots kann diesen Befehl ausführen
async def load_cog(ctx, cog: str):
    try:
        bot.load_extension(f'{cog}')
        await ctx.send(f'{cog} wurde geladen.')
    except Exception as e:
        await ctx.send(f'Fehler beim Laden des Cogs {cog}: {e}')

@bot.command(name='unload')
@commands.is_owner()
async def unload_cog(ctx, cog: str):
    try:
        bot.unload_extension(f'{cog}')
        await ctx.send(f'{cog} wurde entladen.')
    except Exception as e:
        await ctx.send(f'Fehler beim Entladen des Cogs {cog}: {e}')

@bot.command(name='reload')
@commands.is_owner()
async def reload_cogs(ctx: commands.Context):
    for extension in extensions:
        try:
            bot.reload_extension(f'{extension}')
        except Exception as e:
            await ctx.message.add_reaction('❌')
            await ctx.send(f'Fehler beim Neuladen des Cogs {extension}: {e}')
    await ctx.message.add_reaction('✅')

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

bot.run(BOT_TOKEN)