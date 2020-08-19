from discord.ext import commands
from lib.files import update_users
import discord
import random
import json

TOKEN = json.load(open('token.json'))

users = json.load(open('data/users.json'))

client = commands.Bot(command_prefix='+')

@client.event
async def on_ready():
    print('Bot is online.')


@client.command()
async def submit(ctx, user, *, question):
    """Submits a question to 'user's questions."""

    if user not in users.keys():
        users[user] = {'questions': []}

    users[user]['questions'].append(question)

    update_users(users)

    await ctx.send(':white_check_mark: Added your question.')


@client.command()
async def get(ctx):
    """Returns a random question."""

    user = '<@' + str(ctx.author.id) + '>'

    if user not in users.keys() or users[user]['questions'] == []:
        await ctx.send(':x: You have no questions.')

    else:
        question = random.choice(users[user]['questions'])

        users[user]['questions'].remove(question)

        await ctx.send(question)


client.run(TOKEN)
