# This example requires the 'message_content' intent.

import discord
from io import BytesIO
from wand import image

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!magik'):
        # await message.channel.send('TODO')
        if message.attachments:
            #await message.channel.send('Received message with attachment')
            fd = BytesIO()
            await message.attachments[0].save(fp=fd)
            print(message.attachments)
            try:
                img = image.Image(file=fd)
            except Exception as e:
                print(e)
                raise e

            if img.animation:
                img = img.convert('png')
            img.transform(resize='400x400')

            try:
                multiplier = int(1)
            except ValueError:
                multiplier = 1
            else:
                multiplier = max(min(multiplier, 10), 1)

            img.liquid_rescale(width=int(img.width * 0.5),
                               height=int(img.height * 0.5),
                               delta_x=0.5 * multiplier,
                               rigidity=0)
            img.liquid_rescale(width=int(img.width * 1.5),
                               height=int(img.height * 1.5),
                               delta_x=2 * multiplier,
                               rigidity=0)

            img.save(filename="magiked.png")
            discordFile = discord.File(fp="magiked.png")
            await message.channel.send(file=discordFile)


# TODO: Use secrets or ENV
client.run('insert token here')



