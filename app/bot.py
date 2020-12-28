import discord
import os
from discord.ext import commands
from coin import Coin, RiggedCoin

coin = Coin() # instantiate coin from Coin class
riggedCoin = RiggedCoin() # instantiate riggedCoin from Coin class

client = commands.Bot(command_prefix = 'f!')

@client.event 
async def on_ready(): # when the bot is ready (has all the info from discord)
    await client.change_presence(activity=discord.Game(name='Type f!help for usage'))
    print('Bot is ready.')


@client.command(brief="Outputs 'Pong!' and the ping. This is for testing purposes. ")
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command(brief="flip coin")
async def flip(ctx):
    result = coin.flip()
    await ctx.send(result)


@client.command(brief="James flips a legit coin!")
async def jamesflip(ctx):
    result = riggedCoin.rig()
    await ctx.send(result) # when rigged it is always "Heads"
    

@client.command(brief="Change legitimacy of james coin")
async def rig(ctx, status):
    status.lower()
    status.strip()

    riggedCoin.changeStatus(status)
    riggedStatus = riggedCoin.rigged

    commands = ["james", "rigged", "rig", "fair", "good"]
    if status not in commands:
        await ctx.send("try one of these commands: james, rigged, rig, fair, good")

    if riggedStatus == True:
        await ctx.send("James is rigged") # when rigged it is always "Heads"
    elif riggedStatus == False:
        await ctx.send("James is not rigged")

discord_token = os.environ.get('COINBOT_TOKEN')
client.run(discord_token)
