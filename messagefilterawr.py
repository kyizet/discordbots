#https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}

import discord

client = discord.Client()

msg_to_be_filtered = [
    "!p",
    "!p",
    "!skip",
    "!fs",
    "!remove",
    "!rm",
    "!q",
    "!queury",
    "-p",
    "-skip",
]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name != "play-a-song":
        for i in msg_to_be_filtered:
                if i in message.content.lower():
                    await message.delete()
                    await message.channel.send("The song will be played in your voice channel.")
                    await message.channel.send("However, in order to have your song name recorded, please play a song in play-a-song channel, thank you!")
                    await message.channel.send(message.author.mention)

        if message.author.id == 235088799074484224:
            await message.delete()

client.run("token")