# Work with Python 3.6
import discord
import urllib3
import random
import os

# TOKEN = '__GET_AND_CREATE_A_DISCORD_BOT_TOKEN__'

urllib3.disable_warnings()
client = discord.Client()

@client.event
async def on_message(message):
    # Just a catch so that it doesn't reply to itself in an infite loop
    if message.author == client.user:
        return

    if message.content.lower() == "bothelp":
        await client.send_message(message.channel, """Here are all the commands I have:
        bothelp - Provides this help tool tip.
        dickbutt - Here's a dickbutt picture.
        botrps {rock|paper|scissors} - Play rock paper scissorsself. eg `rgrps rock`""")

    if message.content.lower().startswith('dickbutt'):
        embed = discord.Embed(description=message.author.mention + " wants you to look at this dick butt.", color=0xFFC0CB)
        embed.set_image(url="https://images-na.ssl-images-amazon.com/images/I/41q1QAln%2BQL.jpg")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('botrps'):
        rps = [
            "rock",
            "paper",
            "scissors"
        ]
        splitmsg = message.content.split()
        cpu = random.choice(rps)
        if len(splitmsg) < 2:
            await client.send_message(message.channel, "To play you need to select rock|paper|scissors.  eg. `rgrps rock`")
        elif splitmsg[1] == "rock":
            if cpu == "rock":
                await client.send_message(message.channel, "YOU TIED!" + "\nComputer picked: " + cpu)
            if cpu == "paper":
                await client.send_message(message.channel, "YOU LOSE!" + "\nComputer picked: " + cpu)
            if cpu == "scissors":
                await client.send_message(message.channel, "YOU WIN!" + "\nComputer picked: " + cpu)
        elif splitmsg[1] == "paper":
            if cpu == "paper":
                await client.send_message(message.channel, "YOU TIED!" + "\nComputer picked: " + cpu)
            if cpu == "scissors":
                await client.send_message(message.channel, "YOU LOSE!" + "\nComputer picked: " + cpu)
            if cpu == "rock":
                await client.send_message(message.channel, "YOU WIN!" + "\nComputer picked: " + cpu)
        elif splitmsg[1] == "scissors":
            if cpu == "scissors":
                await client.send_message(message.channel, "YOU TIED!" + "\nComputer picked: " + cpu)
            if cpu == "rock":
                await client.send_message(message.channel, "YOU LOSE!" + "\nComputer picked: " + cpu)
            if cpu == "paper":
                await client.send_message(message.channel, "YOU WIN!" + "\nComputer picked: " + cpu)
        else:
            await client.send_message(message.channel, "You didn't pick rock paper or scriccors. Try again.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot set to: ' + TOKEN)
    print('------')

client.run(TOKEN)