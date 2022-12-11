import discord
import responses


async def send_message(message, user_message, private):
    print("Sending Message")

def run(token):
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print('Hello, World!')

    client.run(token)