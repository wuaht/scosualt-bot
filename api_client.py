import requests
from nextcord.ext import commands

class APIClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = 'https://api.scosu.net/v1'
    def get_clears(self):
        api_url = f'{self.url}/get_clears/'
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Fehler: {response.status_code}")
            return None

def setup(bot):
    bot.add_cog(APIClient(bot))