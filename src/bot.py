import discord

def run(token):
    bot = discord.Bot()

    @bot.event
    async def on_ready():
        print(f"{bot.user} connected!")

    @bot.slash_command(name = "lyric", description = "grab a random lyric from a song")
    async def hello(ctx):
        await ctx.respond("> Lyric goes here")

    bot.run(token)