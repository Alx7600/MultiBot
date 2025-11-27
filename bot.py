import discord
from dotenv import load_dotenv
import os
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Lancement du bot discord...")
    print(f"Loggé en tant que {client.user}.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!ping"):
        await message.channel.send("pong")

client.run(os.getenv("Discord_TOKEN"))