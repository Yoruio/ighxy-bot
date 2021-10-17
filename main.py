from discord.ext.commands import Bot
import discord
import os
from dotenv import load_dotenv
import asyncio

client = Bot("!")

@client.event
async def on_ready():
    print("READY TO BELIEVE")

@client.command(
    name='believe',
    description='start 24/7 believe it or not music',
    pass_context=True,
)
async def believe(ctx):
    vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)

    if vc is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if vc.is_playing():
            vc.stop()
        await vc.disconnect()

    vc = None

    user = ctx.message.author
    if user.voice is not None:
        voice_channel=user.voice.channel
        if voice_channel!= None:
            # grab user's voice channel
            channel=voice_channel.name
            await ctx.send('Playing believe it or not in channel '+ channel)
            print('Playing believe it or not in channel '+ channel)

            # create StreamPlayer
            vc = await voice_channel.connect()
            while vc.is_connected():
                vc.play(discord.FFmpegPCMAudio('believe.mp3'), after=lambda e: print('done'))
                while vc.is_connected() and vc.is_playing():
                    await asyncio.sleep(1)

            # disconnect after the player has finished
            print("disconnected")
            vc = None
    else:
        await ctx.send('You need to be in a voice channel to use this command')
    
@client.command(
    name='stop_believing',
    description='stop 24/7 believe it or not music',
    pass_context=True,
)
async def stop_believing(ctx):
    
    print("disconnecting vc")

    # create StreamPlayer
    vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    if vc is None:
        await ctx.send('Believe not currently playing')
    else:
        await ctx.send('Stopping believe')
        vc.stop()
        await vc.disconnect()

load_dotenv()
client.run(os.getenv('TOKEN'))