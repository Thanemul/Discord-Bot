import discord
import os
import requests 
import json
from replit import db
import random
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$boys'):
    await message.channel.send(file=discord.File(random.choice(('20210205_004916_IMG_3166.JPG','WhatsApp Image 2021-12-26 at 12.58.42 AM.jpeg','WhatsApp Image 2021-12-16 at 12.31.40 PM.jpeg','WhatsApp Image 2021-12-26 at 12.34.47 AM.jpeg','WhatsApp Image 2021-12-26 at 12.33.03 AM.jpeg','WhatsApp Image 2021-12-23 at 12.07.35 AM.jpeg','WhatsApp Image 2021-12-23 at 12.13.42 AM.jpeg'))))

keep_alive()
client.run(os.getenv('token2'))
