#https://discordapp.com/oauth2/authorize?client_id={CLIENTID}&scope=bot&permissions={PERMISSIONINT}

import discord
import random

client = discord.Client()
swear_words = ["lee", "loe", "mml", "kmkl", "nlmt", "mmsp", "sat"]
reply_words = [
    "Lee moh Sel Nay Dr lr?",
    "May Loe Ma Sel nae'",
    "Ma yine nae' ly Lee lr?",
    "D Mhar Lar Ma Yine Nae' Lee Pl"
]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for i in swear_words:
        if i in message.content.lower():
            await message.channel.send(reply_words[random.randint(0,3)])
            await message.channel.send("Ae' Lal")

client.run("token")