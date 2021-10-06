import discord
import os
from dotenv import load_dotenv

client = discord.Client()

@client.event
async def on_ready():
    print("FUCK YEA")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if str(message.author) == "Kiggs#5770" and message.channel.id == 885224001247543337:
        print("reacting")
        await message.add_reaction("<:piazza_endorsed:895420469199642687>")
        await message.add_reaction("<:class_endorsed:895420486748614676>")
    
    print(message.author)

load_dotenv()
client.run(os.getenv('TOKEN'))