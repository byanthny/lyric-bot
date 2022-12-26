import discord
import lyricsgenius

def run(discord_token, genius_token):
    bot = discord.Bot()
    genius = lyricsgenius.Genius(genius_token)

    @bot.event
    async def on_ready():
        print(f"{bot.user} connected!")

    @bot.slash_command(name = "lyric", description = "grab a random lyric from a song")
    async def hello(ctx):
        await ctx.respond("> Lyric goes here")

    bot.run(discord_token)