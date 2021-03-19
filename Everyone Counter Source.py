# Discord Bot - "@everyone Counter"
# by Laikaru
    # Count and display the number of times someone uses an "@everyone" in a Discord server.
    # Anytime someone uses "@everyone", the bot will activate and respond.
        # ""@everyone" has been said [X] times!"

import discord
import os
client = discord.Client() # Creates connection to Discord.

counter_variable = 0

@client.event
async def on_ready(): # Bot login and setup.
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # Trigger for every message recieved.
    if message.author == client.user: # Check author is same as user.
        return

    if '@everyone' in message.content:
        global counter_variable
        counter_variable += 1
        if counter_variable == 1:
            await message.channel.send(f'*@*everyone has been sent {counter_variable} time!') # @/everyone = 1, singular
        else:
            await message.channel.send(f'*@*everyone has been sent {counter_variable} times!') # @/everyone > 1, plural

client.run('') # Bot ID goes here. 