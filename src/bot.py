import discord


async def send_message(message, user_message, private):
    print("Sending Message")

def run(token):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'Connected as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$lyric'):
            await message.channel.send('> Something')

    client.run(token)