from discord.ext.commands import Bot
import discord
import os
from dotenv import load_dotenv
import asyncio

client = Bot("!")

vc = None
playing_believe = False

@client.event
async def on_ready():
    print("FUCK YEA")

@client.command(
    name='believe',
    description='start 24/7 believe it or not music',
    pass_context=True,
)
async def believe(ctx):
    
    global vc
    playing_believe = True
    user = ctx.message.author
    voice_channel=user.voice.channel
    channel=None
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('Playing believe it or not in channel '+ channel)
        print('Playing believe it or not in channel '+ channel)

        # create StreamPlayer
        vc = await voice_channel.connect()
        while playing_believe and vc.is_connected():
            vc.play(discord.FFmpegPCMAudio('believe.mp3'))
            while vc.is_connected() and vc.is_playing() and playing_believe:
                await asyncio.sleep(1)

        # disconnect after the player has finished
        print("disconnected")
    
@client.command(
    name='stop_believing',
    description='stop 24/7 believe it or not music',
    pass_context=True,
)
async def stop_believing(ctx):
    global vc
    await ctx.send('stopping believe')
    playing_believe = False
    print("disconnecting vc")
    vc.stop()
    await vc.disconnect()

load_dotenv()
client.run(os.getenv('TOKEN'))