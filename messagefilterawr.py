#https://discordapp.com/oauth2/authorize?client_id=768891624058126366&scope=bot&permissions=206848

import discord
import re

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    regex = re.search("^[!-][a-zA-Z]+\s*[a-zA-Z0-9]*", message.content.lower())

    if message.channel.name != "play-a-song":
        if regex:
                await message.delete()
                await message.channel.send("The song will be played in your voice channel.")
                await message.channel.send("However, in order to have your song name recorded, please play a song in play-a-song channel, thank you!")
                await message.channel.send(message.author.mention)

        if message.author.id == 235088799074484224 or message.author.id == 234395307759108106:
            await message.delete()

    if message.channel.name == "play-a-song":
        if message.author.id == 235088799074484224 or message.author.id == 234395307759108106:
            return
        if not regex:
                await message.delete()
                await message.channel.send("Please chat in other channels.")
                await message.channel.send("This channel is reserved for playing music, thank you!")
                await message.channel.send(message.author.mention)

client.run("NzY4ODkxNjI0MDU4MTI2MzY2.X5HEIA.Gy662LfOkcOi3o_1QvYqh4-wX4c")